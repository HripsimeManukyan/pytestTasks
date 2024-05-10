import pytest
from source.todo_list import TodoList


@pytest.fixture
def todo_list_instance():
    return TodoList()


def test_add_task(todo_list_instance):
    todo_list_instance.add_task("Task 1")
    assert "Task 1" in todo_list_instance.get_tasks()


def test_delete_task(todo_list_instance):
    todo_list_instance.add_task("Task 1")
    todo_list_instance.delete_task("Task 1")
    assert "Task 1" not in todo_list_instance.get_tasks()


def test_mark_task_completed(todo_list_instance):
    todo_list_instance.add_task("Task 1")
    todo_list_instance.mark_task_completed("Task 1")
    assert "Task 1 (completed)" in todo_list_instance.get_tasks()


def test_get_tasks(todo_list_instance):
    todo_list_instance.add_task("Task 1")
    todo_list_instance.add_task("Task 2")
    assert len(todo_list_instance.get_tasks()) == 2
