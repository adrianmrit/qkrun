#!/usr/bin/env python
# PYTHON_ARGCOMPLETE_OK
"""A CLI tool for quick tasks."""

from __future__ import annotations

import typing

from ._meta import __author__, __copyright__, __email__, __home__, __version__

if typing.TYPE_CHECKING:
    # Static imports for type checkers (Pylance/Pyright) — never executed at runtime
    from qkrun.factories import (
        command,
        task_factory_helper,
        group,
        script,
        task,
        thread_group,
    )
    from qkrun.tasks import (
        Command,
        Group,
        OutputMode,
        Script,
        Task,
        ThreadGroup,
    )
    from qkrun._namespace import Namespace, namespace
    from qkrun.config import app, console, logger
    from qkrun import context
    from qkrun.context import Context, load_env_file
    from qkrun.utils.argparser import Arg

__all__ = [
    "__author__",
    "__copyright__",
    "__email__",
    "__home__",
    "__version__",
    "app",
    "console",
    "logger",
    "context",
    "Context",
    "load_env_file",
    "Task",
    "Script",
    "Command",
    "Group",
    "ThreadGroup",
    "OutputMode",
    "Namespace",
    "namespace",
    "task",
    "script",
    "command",
    "Arg",
    "task_factory_helper",
    "group",
    "thread_group",
]

# Lazy import mapping: symbol name -> (module_path, symbol_name)
_LAZY_IMPORTS: dict[str, tuple[str, str]] = {
    # factories
    "command": ("qkrun.factories", "command"),
    "task_factory_helper": ("qkrun.factories", "task_factory_helper"),
    "group": ("qkrun.factories", "group"),
    "script": ("qkrun.factories", "script"),
    "task": ("qkrun.factories", "task"),
    "thread_group": ("qkrun.factories", "thread_group"),
    # tasks
    "Command": ("qkrun.tasks", "Command"),
    "Group": ("qkrun.tasks", "Group"),
    "OutputMode": ("qkrun.tasks", "OutputMode"),
    "Script": ("qkrun.tasks", "Script"),
    "Task": ("qkrun.tasks", "Task"),
    "ThreadGroup": ("qkrun.tasks", "ThreadGroup"),
    # namespace
    "Namespace": ("qkrun._namespace", "Namespace"),
    "namespace": ("qkrun._namespace", "namespace"),
    # config
    "app": ("qkrun.config", "app"),
    "console": ("qkrun.config", "console"),
    "logger": ("qkrun.config", "logger"),
    # context
    "context": ("qkrun", "context"),
    "Context": ("qkrun.context", "Context"),
    "load_env_file": ("qkrun.context", "load_env_file"),
    # utils
    "Arg": ("qkrun.utils.argparser", "Arg"),
}


def __getattr__(name: str):
    if name in _LAZY_IMPORTS:
        module_path, symbol_name = _LAZY_IMPORTS[name]
        import importlib

        module = importlib.import_module(module_path)
        value = getattr(module, symbol_name)
        # Cache on the module so subsequent accesses are fast
        globals()[name] = value
        return value
    raise AttributeError(f"module 'qkrun' has no attribute {name!r}")
