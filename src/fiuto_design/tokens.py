"""Reading and checking tokens/tokens.json (exported from the Fiuto design system)."""

import json
import re
from dataclasses import dataclass
from pathlib import Path

THEMES = ("light", "dark")
HEX_COLOR = re.compile(r"^#[0-9a-fA-F]{6}$")
NAME = re.compile(r"^[a-z][a-z0-9]*(-[a-z0-9]+)*$")


class TokenError(ValueError):
    """tokens.json does not have the expected shape."""


@dataclass(frozen=True)
class ColorToken:
    name: str
    light: str
    dark: str
    usage: str


@dataclass(frozen=True)
class TextStyle:
    name: str
    family: str  # key of Tokens.families
    size_px: float
    line_height_px: float
    weight: int
    letter_spacing_em: float
    usage: str


@dataclass(frozen=True)
class Shadow:
    name: str
    light: str
    dark: str
    usage: str


@dataclass(frozen=True)
class Tokens:
    colors: list[ColorToken]
    families: dict[str, str]  # CSS font stacks
    text_styles: list[TextStyle]
    spacing: dict[str, float]  # px
    radius: dict[str, float]  # px
    shadows: list[Shadow]


def _name(value: str) -> str:
    if not NAME.match(value):
        raise TokenError(f"invalid token name: {value!r}")
    return value


def _px(value: str, where: str) -> float:
    if not value.endswith("px"):
        raise TokenError(f"{where}: expected a px value, got {value!r}")
    return float(value[:-2])


def _em(value: str | None, where: str) -> float:
    if value is None:
        return 0.0
    if not value.endswith("em"):
        raise TokenError(f"{where}: expected an em value, got {value!r}")
    return float(value[:-2])


def _themed(token: dict, where: str) -> tuple[str, str]:
    value = token["value"]
    if not isinstance(value, dict) or set(value) != set(THEMES):
        raise TokenError(f"{where}: expected a value for each theme {THEMES}")
    return value["light"], value["dark"]


def parse(data: dict) -> Tokens:
    colors = []
    for token in data["color"]["tokens"]:
        name = _name(token["name"])
        light, dark = _themed(token, name)
        for color in (light, dark):
            if not HEX_COLOR.match(color):
                raise TokenError(f"{name}: expected #rrggbb, got {color!r}")
        colors.append(ColorToken(name, light.lower(), dark.lower(), token.get("usage", "")))

    families = data["type"]["families"]
    styles = []
    for group in data["type"]["groups"]:
        for style in group["styles"]:
            name = _name(style["name"])
            family = style.get("family", group["family"])
            if family not in families:
                raise TokenError(f"{name}: unknown font family {family!r}")
            styles.append(
                TextStyle(
                    name=name,
                    family=family,
                    size_px=_px(style["fontSize"], name),
                    line_height_px=_px(style["lineHeight"], name),
                    weight=int(style["fontWeight"]),
                    letter_spacing_em=_em(style.get("letterSpacing"), name),
                    usage=style.get("usage", ""),
                )
            )

    def scale(section: str) -> dict[str, float]:
        return {
            _name(token["name"]): _px(token["value"], token["name"])
            for token in data[section]["tokens"]
        }

    shadows = []
    for token in data["shadow"]["tokens"]:
        name = _name(token["name"])
        light, dark = _themed(token, name)
        shadows.append(Shadow(name, light, dark, token.get("usage", "")))

    return Tokens(colors, dict(families), styles, scale("spacing"), scale("radius"), shadows)


def load(path: Path) -> Tokens:
    return parse(json.loads(path.read_text(encoding="utf-8")))
