"""CSS custom properties and text style classes for the website."""

from fiuto_design.names import number
from fiuto_design.tokens import Tokens

HEADER = "/* Generated from tokens/tokens.json by `python -m fiuto_design`. Do not edit. */\n"


def _declarations(pairs: list[tuple[str, str]], indent: str) -> str:
    return "".join(f"{indent}{name}: {value};\n" for name, value in pairs)


def _themed(tokens: Tokens, theme: str) -> list[tuple[str, str]]:
    pairs = [(f"--color-{c.name}", getattr(c, theme)) for c in tokens.colors]
    pairs += [(f"--{s.name}", getattr(s, theme)) for s in tokens.shadows]
    return pairs


def render(tokens: Tokens) -> str:
    fixed = [(f"--font-{name}", stack) for name, stack in tokens.families.items()]
    fixed += [(f"--{name}", f"{number(px)}px") for name, px in tokens.spacing.items()]
    fixed += [(f"--{name}", f"{number(px)}px") for name, px in tokens.radius.items()]

    out = [HEADER, "\n", ":root {\n", "  color-scheme: light;\n"]
    out.append(_declarations(fixed + _themed(tokens, "light"), "  "))
    out.append("}\n\n")
    # Dark theme: from the system setting unless the page forces light, or forced.
    out.append('@media (prefers-color-scheme: dark) {\n  :root:not([data-theme="light"]) {\n')
    out.append("    color-scheme: dark;\n")
    out.append(_declarations(_themed(tokens, "dark"), "    "))
    out.append("  }\n}\n\n")
    out.append(':root[data-theme="dark"] {\n  color-scheme: dark;\n')
    out.append(_declarations(_themed(tokens, "dark"), "  "))
    out.append("}\n")

    for style in tokens.text_styles:
        rules = [
            ("font-family", f"var(--font-{style.family})"),
            ("font-size", f"{number(style.size_px)}px"),
            ("line-height", f"{number(style.line_height_px)}px"),
            ("font-weight", str(style.weight)),
        ]
        if style.letter_spacing_em:
            rules.append(("letter-spacing", f"{number(style.letter_spacing_em)}em"))
        if "tabular figures" in style.usage.lower():
            rules.append(("font-variant-numeric", "tabular-nums"))
        if "uppercase" in style.usage.lower():
            rules.append(("text-transform", "uppercase"))
        out.append(f"\n.type-{style.name} {{\n")
        out.append(_declarations(rules, "  "))
        out.append("}\n")
    return "".join(out)
