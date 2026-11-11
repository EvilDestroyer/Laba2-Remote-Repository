import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from ToDoList import TaskManager


@pytest.fixture
def manager(tmp_path):
    test_file = tmp_path / "test_tasks.json"
    return TaskManager(filename=str(test_file))

def test_add_task(manager):
    manager.add_task("Сделать лабу")
    tasks = manager.get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Сделать лабу"
    assert tasks[0]["done"] is False

def test_add_empty_task(manager):
    with pytest.raises(ValueError):
        manager.add_task("   ")

def test_complete_task(manager):
    manager.add_task("Подготовиться к экзамену")
    manager.complete_task(0)
    assert manager.get_tasks()[0]["done"] is True

def test_delete_task(manager):
    manager.add_task("Задача 1")
    manager.add_task("Задача 2")
    manager.delete_task(0)
    tasks = manager.get_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Задача 2"

def test_invalid_index(manager):
    with pytest.raises(IndexError):
        manager.complete_task(99)


def test_get_tasks_by_status(manager):
    manager.add_task("Активная задача")
    manager.add_task("Выполненная задача")
    manager.complete_task(1)

    active_tasks = manager.get_tasks_by_status(False)
    completed_tasks = manager.get_tasks_by_status(True)

    assert len(active_tasks) == 1
    assert active_tasks[0]["task"] == "Активная задача"

    assert len(completed_tasks) == 1
    assert completed_tasks[0]["task"] == "Выполненная задача"


def test_clear_completed(manager):
    manager.add_task("Задача 1")
    manager.add_task("Задача 2")
    manager.add_task("Задача 3")

    manager.complete_task(0)
    manager.complete_task(2)

    assert len(manager.get_tasks()) == 3

    manager.clear_completed()


    tasks_after = manager.get_tasks()
    assert len(tasks_after) == 1
    assert tasks_after[0]["task"] == "Задача 2"
    assert tasks_after[0]["done"] is False