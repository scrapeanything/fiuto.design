"""Flutter theme code: colors as a ThemeExtension, text styles, spacing, radii and shadows."""

import re

from fiuto_design.names import camel, font_stack, number, without_prefix
from fiuto_design.tokens import TokenError, Tokens

HEADER = "// Generated from tokens/tokens.json by `python -m fiuto_design`. Do not edit.\n"
GENERIC_FAMILIES = {"serif", "sans-serif", "monospace", "system-ui"}
_SHADOW = re.compile(
    r"^(-?[\d.]+)(?:px)?\s+(-?[\d.]+)(?:px)?\s+([\d.]+)(?:px)?\s+"
    r"rgba\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*([\d.]+)\s*\)$"
)
WEIGHTS = {100, 200, 300, 400, 500, 600, 700, 800, 900}


def color(hex_color: str) -> str:
    """#f2a516 -> Color(0xFFF2A516)."""
    return f"Color(0xFF{hex_color[1:].upper()})"


def box_shadow(css: str) -> str:
    """'0 -8px 24px rgba(15, 19, 17, 0.10)' -> a Dart BoxShadow."""
    match = _SHADOW.match(css.strip())
    if match is None:
        raise TokenError(f"unsupported shadow: {css!r}")
    x, y, blur, red, green, blue, alpha = match.groups()
    return (
        f"BoxShadow(offset: Offset({number(float(x))}, {number(float(y))}), "
        f"blurRadius: {number(float(blur))}, "
        f"color: Color.fromRGBO({red}, {green}, {blue}, {number(float(alpha))}))"
    )


def _colors_class(tokens: Tokens) -> str:
    fields = [camel(c.name) for c in tokens.colors]
    out = [
        "/// The Fiuto colors, for both themes: `Theme.of(context).extension<FiutoColors>()!`.\n",
        "@immutable\n",
        "class FiutoColors extends ThemeExtension<FiutoColors> {\n",
        "  const FiutoColors({\n",
        "".join(f"    required this.{field},\n" for field in fields),
        "  });\n\n",
    ]
    for token, field in zip(tokens.colors, fields, strict=True):
        out.append(f"  /// {token.usage}\n" if token.usage else "")
        out.append(f"  final Color {field};\n")
    for theme in ("light", "dark"):
        out.append(f"\n  static const {theme} = FiutoColors(\n")
        for token, field in zip(tokens.colors, fields, strict=True):
            out.append(f"    {field}: {color(getattr(token, theme))},\n")
        out.append("  );\n")
    out.append("\n  @override\n  FiutoColors copyWith({\n")
    out.append("".join(f"    Color? {field},\n" for field in fields))
    out.append("  }) {\n    return FiutoColors(\n")
    out.append("".join(f"      {field}: {field} ?? this.{field},\n" for field in fields))
    out.append("    );\n  }\n")
    out.append(
        "\n  @override\n  FiutoColors lerp(ThemeExtension<FiutoColors>? other, double t) {\n"
    )
    out.append(
        "    if (other is! FiutoColors) {\n      return this;\n    }\n    return FiutoColors(\n"
    )
    out.append(
        "".join(f"      {field}: Color.lerp({field}, other.{field}, t)!,\n" for field in fields)
    )
    out.append("    );\n  }\n}\n")
    return "".join(out)


def _text_styles(tokens: Tokens) -> str:
    out = [
        "/// Text styles. Flutter has no text-transform: uppercase the overline text yourself.\n"
    ]
    out.append("abstract final class FiutoTextStyles {\n")
    for style in tokens.text_styles:
        if style.weight not in WEIGHTS:
            raise TokenError(f"{style.name}: unsupported font weight {style.weight}")
        stack = [f for f in font_stack(tokens.families[style.family]) if f not in GENERIC_FAMILIES]
        family, fallback = stack[0], stack[1:]
        args = [
            f"fontFamily: '{family}'",
            f"fontFamilyFallback: [{', '.join(repr(f) for f in fallback)}]",
            f"fontSize: {number(style.size_px)}",
            f"height: {number(style.line_height_px / style.size_px)}",
            f"fontWeight: FontWeight.w{style.weight}",
        ]
        if style.letter_spacing_em:
            args.append(f"letterSpacing: {number(style.letter_spacing_em * style.size_px)}")
        if "tabular figures" in style.usage.lower():
            args.append("fontFeatures: [FontFeature.tabularFigures()]")
        out.append(f"  /// {style.usage}\n" if style.usage else "")
        out.append(f"  static const {camel(style.name)} = TextStyle(\n")
        out.append("".join(f"    {arg},\n" for arg in args))
        out.append("  );\n")
    out.append("}\n")
    return "".join(out)


def _scale(class_name: str, doc: str, values: dict[str, float], prefix: str) -> str:
    out = [f"/// {doc}\n", f"abstract final class {class_name} {{\n"]
    for name, px in values.items():
        out.append(f"  static const double {camel(without_prefix(name, prefix))} = {number(px)};\n")
    out.append("}\n")
    return "".join(out)


def _shadows(tokens: Tokens) -> str:
    out = ["/// Shadows, per theme.\n", "abstract final class FiutoShadows {\n"]
    for shadow in tokens.shadows:
        field = camel(without_prefix(shadow.name, "shadow-"))
        for theme in ("light", "dark"):
            value = box_shadow(getattr(shadow, theme))
            out.append(f"  static const {field}{theme.title()} = [{value}];\n")
    out.append("}\n")
    return "".join(out)


def render(tokens: Tokens) -> str:
    return "\n".join(
        [
            HEADER + "\nimport 'package:flutter/material.dart';\n",
            _colors_class(tokens),
            _text_styles(tokens),
            _scale(
                "FiutoSpacing",
                "Spacing in logical pixels (4px grid).",
                tokens.spacing,
                "",  # space-1 -> space1: a bare "1" is not a Dart name
            ),
            _scale(
                "FiutoRadius",
                "Corner radii in logical pixels.",
                tokens.radius,
                "radius-",
            ),
            _shadows(tokens),
        ]
    )
