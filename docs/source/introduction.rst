Introduction
============

qkrun is a simple task runner, inspired on tools like `celery <https://docs.celeryproject.org/en/stable/index.html>`_,
`cargo-make <https://github.com/sagiegurari/cargo-make>`_, `Task <https://taskfile.dev>`_, and `invoke <https://www.pyinvoke.org>`_.
It aims to be simple to use, easy to extend, and to provide a good experience for developers and teams.

Unlike other task runners that define tasks in YAML, TOML or specialized formats, qkrun uses the Python programming language
directly, leveraging the power of the language and the ecosystem around it. This means for example, that syntax highlighting,
errors, and auto completion in most code editors will work out of the box.

qkrun is not limited to Python projects, you can for example define a virtual environment with qkrun and other dependencies
alongside a project that is not using Python at all, similar to how make can be used in non C/C++ projects.

Some features include:

* Run python, shell scripts, and subprocesses as tasks.
* Powerful arguments parsing, by wrapping `argparse <https://docs.python.org/3/library/argparse.html>`_.
* Autocompletion both for the CLI and tasks, thanks to `argcomplete <https://pypi.org/project/argcomplete/>`_.
* Custom autocompletion for task arguments.
* Conditions to run tasks only if certain conditions are met.
* Dependencies between tasks.
* Namespaces to organize tasks.
* Watch mode to re-run tasks automatically on file changes.

Requirements
--------------

qkrun has been tested on macOs, but should work on Linux and Windows as well. If you find any issues, please open an issue on GitHub.


Per Project Installation
------------------------

The recommended way to use qkrun is to install it per-project in a virtual environment. This allows each project to pin its own version of qkrun and avoids version conflicts across projects.

**With automatic launcher (recommended):**

Once you have qkrun installed in a project virtual environment, you can run tasks from anywhere without manual virtual environment activation. The global ``qk`` command will automatically discover your project and delegate to the project-specific version:

.. code-block:: bash

    cd my-project
    python -m venv .venv
    .venv/bin/pip install qkrun
    qk task-name  # Automatically uses project-specific qkrun!

The launcher will search for a ``_qk`` directory or ``_qk.py`` file starting from your current directory and traveling up the directory tree. Once found, it delegates to the qkrun installation in that project's virtual environment.

**Traditional manual activation (still supported):**

If preferred, you can still manually activate the virtual environment:

.. code-block:: bash

    cd my-project
    python -m venv .venv
    source .venv/bin/activate
    pip install qkrun
    qk --help


Global installation
-------------------

While qkrun allows you to run tasks defined within a project, sometimes it is useful to have global tasks accessible from anywhere. Install ``qkrun`` globally (e.g. with pipx) and use the ``--global`` (or ``-g``) flag:

.. code-block:: bash

    qk --global task-name

Global tasks are stored in ``~/_qkg`` and are only used when explicitly requested with ``--global`` (or ``-g``).

**Installation with pipx (recommended for global tools):**

.. code-block:: bash

    pipx install qkrun
    qk --global task-name

.. TIP::
    If installing via pipx and you need to add extra dependencies, you can inject them:

    .. code-block:: bash

        pipx inject qkrun my-extra-dependency


Upgrading
---------

You can also upgrade via ``pip``:

.. code-block:: bash

    pip install --upgrade qkrun


Or ``pipx``:

.. code-block:: bash

    pipx upgrade qkrun


Auto completion
---------------
qkrun provides auto completion for tasks and arguments via the `argcomplete <https://pypi.org/project/argcomplete/>`_ package.

To enable it, you need to install `argcomplete <https://pypi.org/project/argcomplete/>`_ globally and add the following line to your shell configuration file:

.. code-block:: bash

    eval "$(register-python-argcomplete qk)"

This is sufficient for both project tasks and global tasks. When tab completing inside a project directory, the smart launcher delegates to the project-local qkrun installation, so completions reflect that project's tasks and version.

You can also call ``qk --autocomplete bash`` or ``qk --autocomplete zsh`` for instructions on how to enable auto completion for your shell.


Quick(ie)start
--------------

Defining tasks
^^^^^^^^^^^^^^

Tasks can be defined in a ``_qk`` Python module, be it a single file or a package, usually at the
root of the project. For global tasks they can be defined in the same way at ``~/_qkg``. They can also
be defined at an arbitrary Python module, and passed to the runner using the ``--module`` or ``-m`` argument.

For example:

.. code-block:: python

    # MyProject/_qk.py
    from qkrun import Arg, task, script, command

    @task
    def hello():
        print("Hello, World!")

    @script(
        args=[
            Arg("--name", help="Your name"),
        ],
    )
    def hello_script(name):
        return f"echo 'Hello, {name}!'"

    @command(extra_args=True)
    def some_command(*args):
        return ["my_command", *args]

Now you can run the tasks from anywhere in the project, even from a subdirectory.

.. code-block:: bash

    $ qk hello
    Hello, World!

    $ qk hello-script --name Alice
    Hello, Alice!

    $ qk some-command arg1 arg2
    my_command arg1 arg2


Defining tasks in a package
^^^^^^^^^^^^^^^^^^^^^^^^^^^

For more complex projects, or teams, it is recommended to define tasks in a package.
This allows to better organize the tasks and to have private tasks that are not
committed to the repository.

For example:

.. code-block:: bash

    MyProject/
    ├── _qk
    │   ├── __init__.py
    │   ├── public.py
    │   ├── private.py  # might not exist
    │   └── ...        # more files
    └── ...


Then in the ``__init__.py`` file you can import the tasks from the other files.

.. code-block:: python

    # MyProject/_qk/__init__.py
    from qkrun import namespace
    from . import public

    @namespace
    def _():
        tasks = [public]
        try:
            from . import private
            tasks.append(private)
            return {"": tasks, "private": [private]}
        except ImportError:
            return tasks

Because ``@namespace`` is lazy, the optional ``private`` module is only imported when qkrun
actually needs one of the tasks in this namespace.


For most of of the documentation, we will assume tasks are defined in a package.
