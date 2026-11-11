import pytest
import os
from ToDoList import TaskManager

# Фикстура создает временный файл для тестов, чтобы не засорять основной
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