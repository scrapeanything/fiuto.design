"""`python -m fiuto_design`: writing and checking the generated files."""

import runpy
import shutil
import sys
from pathlib import Path

import pytest

from fiuto_design import __main__ as cli

ROOT = Path(__file__).resolve().parents[1]


@pytest.fixture
def copy(tmp_path):
    shutil.copytree(ROOT / "tokens", tmp_path / "tokens")
    shutil.copytree(ROOT / "assets", tmp_path / "assets")
    return tmp_path


def test_the_committed_files_are_up_to_date():
    assert cli.main(["--check"]) == 0


def test_write_then_check(copy, capsys):
    assert cli.main(["--check"], root=copy) == 1
    assert "out of date" in capsys.readouterr().err

    assert cli.main([], root=copy) == 0
    written = capsys.readouterr().out
    assert "written web/tokens.css" in written
    assert "written flutter/assets/logos/fiuto-mark.svg" in written
    assert cli.main(["--check"], root=copy) == 0
    # Nothing to do the second time.
    assert cli.main([], root=copy) == 0
    assert capsys.readouterr().out == ""
    assert (copy / "web/tokens.css").read_text() == (ROOT / "web/tokens.css").read_text()


def test_python_dash_m(monkeypatch):
    monkeypatch.setattr(sys, "argv", ["python -m fiuto_design", "--check"])
    monkeypatch.delitem(sys.modules, "fiuto_design.__main__", raising=False)

    with pytest.raises(SystemExit) as exit_info:
        runpy.run_module("fiuto_design", run_name="__main__")

    assert exit_info.value.code == 0
