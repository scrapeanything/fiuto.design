"""Reading tokens.json."""

import copy
import json
from pathlib import Path

import pytest

from fiuto_design.tokens import TokenError, load, parse

SOURCE = Path(__file__).resolve().parents[1] / "tokens" / "tokens.json"


@pytest.fixture
def data():
    return json.loads(SOURCE.read_text(encoding="utf-8"))


def test_the_design_system_tokens():
    tokens = load(SOURCE)

    assert [c.name for c in tokens.colors][:3] == ["surface", "surface-raised", "surface-sunken"]
    fiuto = next(c for c in tokens.colors if c.name == "fiuto")
    assert (fiuto.light, fiuto.dark) == ("#f2a516", "#f6b23a")
    assert tokens.families["display"].startswith('"Barlow Semi Condensed"')
    figure_xl = tokens.text_styles[0]
    assert (figure_xl.name, figure_xl.family, figure_xl.size_px) == ("figure-xl", "display", 40)
    assert figure_xl.letter_spacing_em == -0.01
    title = next(s for s in tokens.text_styles if s.name == "title")
    assert title.family == "display"  # its own family, not the group's
    assert tokens.spacing["space-4"] == 16
    assert tokens.radius["radius-md"] == 10
    assert tokens.shadows[0].name == "shadow-sheet"


def test_colors_are_lowercased(data):
    data["color"]["tokens"][0]["value"] = {"light": "#ABCDEF", "dark": "#000000"}

    assert parse(data).colors[0].light == "#abcdef"


def broken(data, change):
    data = copy.deepcopy(data)
    change(data)
    return data


@pytest.mark.parametrize(
    ("change", "message"),
    [
        (lambda d: d["color"]["tokens"][0].update(name="Surface"), "invalid token name"),
        (lambda d: d["color"]["tokens"][0].update(value="#ffffff"), "each theme"),
        (lambda d: d["color"]["tokens"][0].update(value={"light": "#fff"}), "each theme"),
        (
            lambda d: d["color"]["tokens"][0].update(value={"light": "#fff", "dark": "#000000"}),
            "expected #rrggbb",
        ),
        (lambda d: d["type"]["groups"][0]["styles"][0].update(family="mono"), "unknown font"),
        (lambda d: d["type"]["groups"][0]["styles"][0].update(fontSize="2rem"), "px value"),
        (
            lambda d: d["type"]["groups"][0]["styles"][0].update(letterSpacing="1px"),
            "em value",
        ),
        (lambda d: d["spacing"]["tokens"][0].update(value="4"), "px value"),
        (lambda d: d["shadow"]["tokens"][0].update(value="none"), "each theme"),
    ],
)
def test_malformed_tokens(data, change, message):
    with pytest.raises(TokenError, match=message):
        parse(broken(data, change))
