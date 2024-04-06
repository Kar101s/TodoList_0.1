import tkinter as tk
from tkinter import simpledialog, messagebox
from classes import Task, TodoList

class TodoApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Менеджер задач")
        self.todo_list = TodoList()
        self.create_widgets()

    def create_widgets(self):
        # Основной фрейм
        self.main_frame = tk.Frame(self)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Фрейм для меню
        self.menu_frame = tk.Frame(self.main_frame)
        self.menu_frame.pack(side=tk.RIGHT, padx=10, pady=10)

        self.label = tk.Label(self.menu_frame, text="Основне меню:")
        self.label.pack(pady=20)

        self.button_load = tk.Button(self.menu_frame, text="Завантажити файл", command=self.load_from_file)
        self.button_load.pack(pady=5)

        self.button_save = tk.Button(self.menu_frame, text="Зберегти файл", command=self.save_to_file)
        self.button_save.pack(pady=5)

        self.button_add = tk.Button(self.menu_frame, text="Додати задачу", command=self.add_task)
        self.button_add.pack(pady=5)

        self.button_add_subtask = tk.Button(self.menu_frame, text="Додати підзадачу", command=self.add_subtask)
        self.button_add_subtask.pack(pady=5)

        self.button_remove = tk.Button(self.menu_frame, text="Видалити задачу", command=self.remove_task)
        self.button_remove.pack(pady=5)

        self.button_complete = tk.Button(self.menu_frame, text="Позначити задачу як виконану", command=self.complete_task)
        self.button_complete.pack(pady=5)

        self.button_add_deadline = tk.Button(self.menu_frame, text="Встановити дедлайн", command=self.add_deadline)
        self.button_add_deadline.pack(pady=5)

        self.button_change_deadline = tk.Button(self.menu_frame, text="Змінити дедлайн", command=self.change_deadline)
        self.button_change_deadline.pack(pady=5)

        self.button_exit = tk.Button(self.menu_frame, text="Вихід", command=self.quit)
        self.button_exit.pack(pady=20)

        self.tasks_frame = tk.Frame(self.main_frame)
        self.tasks_frame.pack(side=tk.LEFT, padx=10, pady=10, fill=tk.BOTH, expand=True)

        self.text_tasks = tk.Text(self.tasks_frame, width=60, height=40)
        self.text_tasks.pack(pady=20)

    def load_from_file(self):
        self.todo_list.load_from_file()
        self.update_tasks_text()

    def save_to_file(self):
        self.todo_list.save_to_file()
        self.update_tasks_text()

    def add_task(self):
        self.todo_list.add_task()
        self.update_tasks_text()

    def add_subtask(self):
        self.todo_list.add_subtask()
        self.update_tasks_text()

    def remove_task(self):
        self.todo_list.remove_task()
        self.update_tasks_text()

    def complete_task(self):
        self.todo_list.complete_task()
        self.update_tasks_text()

    def add_deadline(self):
        self.todo_list.add_deadline()
        self.update_tasks_text()

    def change_deadline(self):
        self.todo_list.change_deadline()
        self.update_tasks_text()

    def update_tasks_text(self):
        tasks_text = "\n".join(str(task) for task in self.todo_list.tasks)
        self.text_tasks.delete("1.0", tk.END)
        self.text_tasks.insert(tk.END, tasks_text)

if __name__ == "__main__":
    app = TodoApp()
    app.mainloop()
