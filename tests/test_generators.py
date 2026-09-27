"""The generated CSS, TypeScript and Dart."""

from pathlib import Path

import pytest

from fiuto_design import css, dart, typescript
from fiuto_design.names import camel, font_stack, number, without_prefix
from fiuto_design.tokens import TextStyle, TokenError, load

TOKENS = load(Path(__file__).resolve().parents[1] / "tokens" / "tokens.json")


@pytest.mark.parametrize(
    ("name", "expected"),
    [("surface", "surface"), ("surface-raised", "surfaceRaised"), ("space-1", "space1")],
)
def test_camel(name, expected):
    assert camel(name) == expected


def test_helpers():
    assert without_prefix("radius-sm", "radius-") == "sm"
    assert without_prefix("sm", "radius-") == "sm"
    assert font_stack("\"Barlow\", 'Arial Narrow', sans-serif,") == [
        "Barlow",
        "Arial Narrow",
        "sans-serif",
    ]
    assert (number(4.0), number(0.4), number(1 / 3)) == ("4", "0.4", "0.3333")


def test_css():
    text = css.render(TOKENS)

    assert text.startswith("/* Generated from tokens/tokens.json")
    light, dark_media, dark_forced = text.split("\n\n")[1:4]
    assert "--color-surface: #f4f5f2;" in light
    assert "--space-4: 16px;" in light
    assert "--radius-md: 10px;" in light
    assert "--font-display: " in light
    assert "--shadow-sheet: 0 -8px 24px rgba(15, 19, 17, 0.10);" in light
    assert ':root:not([data-theme="light"])' in dark_media
    assert "--color-surface: #0d0f0e;" in dark_media
    assert ':root[data-theme="dark"]' in dark_forced
    assert "--space-4" not in dark_forced
    assert ".type-figure-xl {" in text
    assert "letter-spacing: -0.01em;" in text
    assert "font-variant-numeric: tabular-nums;" in text
    assert "text-transform: uppercase;" in text


def test_typescript():
    text = typescript.render(TOKENS)

    assert 'export const lightColors = {\n  "surface": "#f4f5f2",' in text
    assert '"surface": "#0d0f0e"' in text
    assert "export const color = (token: ColorToken): string =>" in text
    assert '"space-4": "16px"' in text
    assert '| "overline"' in text
    assert '"figureXl": "figure-xl"' in text


def test_dart():
    text = dart.render(TOKENS)

    assert "import 'package:flutter/material.dart';" in text
    assert "class FiutoColors extends ThemeExtension<FiutoColors>" in text
    assert "    surfaceRaised: Color(0xFFFFFFFF)," in text
    assert "    surfaceRaised: Color(0xFF161A18)," in text
    assert "      surfaceRaised: Color.lerp(surfaceRaised, other.surfaceRaised, t)!," in text
    assert "  static const double space4 = 16;" in text
    assert "  static const double md = 10;" in text
    assert "fontFamilyFallback: ['Barlow', 'Arial Narrow']" in text
    assert "letterSpacing: -0.4" in text
    assert "static const sheetLight = [BoxShadow(offset: Offset(0, -8), blurRadius: 24," in text


def test_box_shadow():
    assert dart.box_shadow("2px 4px 8px rgba(0, 0, 0, 0.5)") == (
        "BoxShadow(offset: Offset(2, 4), blurRadius: 8, color: Color.fromRGBO(0, 0, 0, 0.5))"
    )
    with pytest.raises(TokenError, match="unsupported shadow"):
        dart.box_shadow("0 0 4px #000")


def test_unsupported_weight():
    odd = TextStyle("odd", "sans", 10, 12, 450, 0, "")
    tokens = type(TOKENS)(
        TOKENS.colors, TOKENS.families, [odd], TOKENS.spacing, TOKENS.radius, TOKENS.shadows
    )

    with pytest.raises(TokenError, match="font weight 450"):
        dart.render(tokens)


def test_style_without_usage_or_spacing():
    plain = TextStyle("plain", "sans", 10, 12, 400, 0, "")
    tokens = type(TOKENS)(
        TOKENS.colors, TOKENS.families, [plain], TOKENS.spacing, TOKENS.radius, TOKENS.shadows
    )

    dart_text = dart.render(tokens)
    css_text = css.render(tokens)

    assert "static const plain = TextStyle(" in dart_text
    assert "letterSpacing" not in dart_text.split("static const plain")[1]
    assert "letter-spacing" not in css_text.split(".type-plain")[1]
