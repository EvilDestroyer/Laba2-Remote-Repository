import json
import os

class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        """Загружает задачи из файла, если он есть."""
        if os.path.exists(self.filename):
            with open(self.filename, "r", encoding="utf-8") as f:
                return json.load(f)
        return []

    def _save_tasks(self):
        """Сохраняет задачи в файл."""
        with open(self.filename, "w", encoding="utf-8") as f:
            json.dump(self.tasks, f, ensure_ascii=False, indent=4)

    def add_task(self, task):
        """Добавляет новую задачу."""
        if not task or not task.strip():
            raise ValueError("Задача не может быть пустой")
        self.tasks.append({"task": task.strip(), "done": False})
        self._save_tasks()

    def complete_task(self, index):
        """Помечает указанную задачу как выполненную."""
        if 0 <= index < len(self.tasks):
            self.tasks[index]["done"] = True
            self._save_tasks()
        else:
            raise IndexError("Неверный индекс задачи")

    def delete_task(self, index):
        """Удаляет выбранную."""
        if 0 <= index < len(self.tasks):
            del self.tasks[index]
            self._save_tasks()
        else:
            raise IndexError("Неверный индекс задачи")

    def get_tasks(self):
        """Отображает все задачи."""
        return self.tasks

    def get_tasks_by_status(self, done_status):
        """Показывает только выполненные или не выполненные задачи."""
        return [t for t in self.tasks if t["done"] == done_status]

    def clear_completed(self):
        """Удаляет все выполненные задачи."""
        self.tasks = [t for t in self.tasks if not t["done"]]
        self._save_tasks()