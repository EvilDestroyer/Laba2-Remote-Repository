from ToDoList import TaskManager


def show_menu():
    print("\n--- МЕНЮ ---")
    print("1. Показать задачи")
    print("2. Добавить задачу")
    print("3. Отметить задачу выполненной")
    print("4. Удалить задачу")
    print("0. Выход")


def main():
    manager = TaskManager()

    while True:
        show_menu()
        choice = input("Выберите действие: ")

        if choice == "1":
            tasks = manager.get_tasks()
            if not tasks:
                print("Список задач пуст.")
            else:
                print("\nВаши задачи:")
                for i, t in enumerate(tasks):
                    status = "[x]" if t["done"] else "[ ]"
                    print(f"{i}. {status} {t['task']}")

        elif choice == "2":
            task_text = input("Введите текст задачи: ")
            try:
                manager.add_task(task_text)
                print("Задача добавлена!")
            except ValueError as e:
                print(f"Ошибка: {e}")

        elif choice == "3":
            try:
                idx = int(input("Введите номер задачи для выполнения: "))
                manager.complete_task(idx)
                print("Задача выполнена!")
            except (ValueError, IndexError):
                print("Введён некорректный номер.")

        elif choice == "4":
            try:
                idx = int(input("Введите номер задачи для удаления: "))
                manager.delete_task(idx)
                print("Задача удалена!")
            except (ValueError, IndexError):
                print("Введён некорректный номер.")

        elif choice == "0":
            print("Завершение работы!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")


if __name__ == "__main__":
    main()