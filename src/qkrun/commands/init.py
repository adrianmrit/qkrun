"""The ``:init`` command — scaffold a qkrun project."""

from __future__ import annotations

import typing
from argparse import ArgumentParser
from argcomplete.completers import FilesCompleter
from pathlib import Path

from qkrun.commands.base import CliCommand

INIT_CONTENT = """from qkrun import task

@task
def hello():
    print("Hello, World!")
"""


class InitCommand(CliCommand):
    """Initialize a qkrun project in a directory."""

    @typing.override
    def configure_parser(self, parser: ArgumentParser) -> None:
        action = parser.add_argument(
            "directory",
            nargs="?",
            default=".",
            metavar="DIR",
            help="Directory to initialize (default: current directory)",
        )
        action.completer = FilesCompleter()  # type: ignore

    @typing.override
    def execute(self, namespace: object) -> None:
        ns = typing.cast("_InitNamespace", namespace)
        target_dir = Path(f"{ns.directory}/_qk")
        if target_dir.exists():
            print("qkrun project already initialized")
            return
        target_dir.mkdir()
        with open(target_dir / "__init__.py", "w") as f:
            f.write(INIT_CONTENT)
        print("Initialized qkrun project")
        print("Run `qk hello` to test it out")
        print("Run `qk --help` for more information")


class _InitNamespace:
    """Minimal type hint for the ``:init`` namespace."""

    directory: str
