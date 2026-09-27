"""Token names in the style of each target language."""


def camel(name: str) -> str:
    """surface-raised -> surfaceRaised, figure-xl -> figureXl, space-1 -> space1."""
    first, *rest = name.split("-")
    return first + "".join(part[:1].upper() + part[1:] for part in rest)


def without_prefix(name: str, prefix: str) -> str:
    """radius-sm -> sm; names without the prefix are kept."""
    return name[len(prefix) :] if name.startswith(prefix) else name


def font_stack(stack: str) -> list[str]:
    """'"Barlow", Arial, sans-serif' -> ['Barlow', 'Arial', 'sans-serif']."""
    return [family.strip().strip('"').strip("'") for family in stack.split(",") if family.strip()]


def number(value: float) -> str:
    """4.0 -> '4', 0.4 -> '0.4': numbers as a person would write them."""
    return str(int(value)) if value == int(value) else repr(round(value, 4))
