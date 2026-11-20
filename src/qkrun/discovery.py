"""Public project discovery boundary for external qkrun integrations.

These helpers share the CLI launcher's marker search and executable precedence
without exposing its private implementation or launching a task in-process.
"""

from pathlib import Path

from qkrun._launcher import Launcher


def discover_project_root(start_path: Path | None = None) -> Path | None:
    """Find the nearest ancestor containing an ``_qk`` directory or ``_qk.py``."""
    return Launcher().discover_project_root(start_path)


def resolve_executable(project_root: Path) -> Path | None:
    """Find project-local qk, then QK_EXECUTABLE, using CLI precedence."""
    return Launcher().resolve_executable(project_root)
