Running tasks in sequence
=========================

Group tasks are used to run multiple tasks in sequence.
The simplest way is to use the :func:`qkrun.group` decorator to define a group task, which should return a list of tasks:

.. code-block:: python

    from qkrun import group

    @task
    def task1():
        print("Task 1")

    @task
    def task2():
        print("Task 2")

    @group
    def my_group():
        return [task1, task2]


This will return a :class:`qkrun.tasks.Group` instance, equivalent to:

.. code-block:: python

    from qkrun import Group

    ...

    @task
    class MyGroup(Group):
        def get_tasks(self):
            return [task1, task2]

If one of these tasks fails, no further tasks will be run.
