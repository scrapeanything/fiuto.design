"""Typed token values for the website's TypeScript code."""

import json

from fiuto_design.names import camel, number
from fiuto_design.tokens import Tokens

HEADER = "// Generated from tokens/tokens.json by `python -m fiuto_design`. Do not edit.\n"


def _object(values: dict[str, str | float], indent: str = "  ") -> str:
    lines = "".join(
        f"{indent}{json.dumps(key)}: {json.dumps(value)},\n" for key, value in values.items()
    )
    return "{\n" + lines + indent[:-2] + "}"


def render(tokens: Tokens) -> str:
    out = [HEADER, "\n"]
    for theme in ("light", "dark"):
        values = {c.name: getattr(c, theme) for c in tokens.colors}
        out.append(f"export const {theme}Colors = {_object(values)} as const;\n\n")
    out.append("export type ColorToken = keyof typeof lightColors;\n\n")
    out.append("/** The CSS variable of a color, which follows the active theme. */\n")
    out.append("export const color = (token: ColorToken): string => `var(--color-${token})`;\n\n")
    out.append(f"export const fonts = {_object(dict(tokens.families))} as const;\n\n")
    spacing = {name: f"{number(px)}px" for name, px in tokens.spacing.items()}
    out.append(f"export const spacing = {_object(spacing)} as const;\n\n")
    radius = {name: f"{number(px)}px" for name, px in tokens.radius.items()}
    out.append(f"export const radius = {_object(radius)} as const;\n\n")
    out.append("export type TextStyleToken =\n")
    out.append("".join(f'  | "{style.name}"\n' for style in tokens.text_styles))
    out.append(";\n\n")
    out.append("/** The class of a text style, defined in tokens.css. */\n")
    out.append("export const textStyle = (token: TextStyleToken): string => `type-${token}`;\n\n")
    names = {camel(style.name): style.name for style in tokens.text_styles}
    out.append(f"export const textStyles = {_object(names)} as const;\n")
    return "".join(out)
