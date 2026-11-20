"""Tests for the ``qkrun.__main__`` module.

The module is a thin wrapper around ``qkrun._cli.main`` that is executed
when the package is run with ``python -m qkrun``. Importing the module
runs ``_run_main()`` at module level, but the ``if __name__ == "__main__"``
guard is skipped because ``__name__`` is not ``"__main__"`` when imported.
"""

import qkrun.__main__ as qkrun_main


def test_run_main_forwards_argv_to_cli_main(mocker):
    """``_run_main()`` forwards ``sys.argv[1:]`` to ``qkrun._cli.main``."""
    # ``__main__`` does ``from ._cli import main``, so patch the reference
    # already bound on the module rather than ``qkrun._cli.main``.
    mock_main = mocker.patch.object(qkrun_main, "main")
    mocker.patch("sys.argv", ["qkrun", "hello", "--flag"])
    # Simulate execution as ``python -m qkrun`` so the guard body runs.
    mocker.patch.object(qkrun_main, "__name__", "__main__")

    qkrun_main._run_main()

    mock_main.assert_called_once_with(["hello", "--flag"])
