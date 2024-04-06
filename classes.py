# from tkinter import simpledialog, messagebox
#
# class Task:
#     def __init__(self, name, description):
#         self.name = name
#         self.description = description
#         self.completed = False
#         self.deadline = None
#         self.subtask = None
#
#     def complete(self):
#         self.completed = True
#
#     def __str__(self):
#         completed_status = 'Завершено' if self.completed else 'Не завершено'
#         deadline_status = f'Дедлайн: {self.deadline}' if self.deadline else 'Дедлайн не встановлено'
#         subtask_status = f'Підзадача: {self.subtask}' if self.subtask else 'Підзадачі не має'
#         return f"{self.name} - {self.description}- {subtask_status} - {completed_status} - {deadline_status} "
#
# class TodoList:
#     def __init__(self):
#         self.tasks = []
#
#     def view_tasks(self):
#         print("Наявні задачі")
#         for task in self.tasks:
#             print(task)
#
#     def add_deadline(self):
#         name = simpledialog.askstring("Встановити дедлайн", "Введіть назву задачі для встановлення дедлайну:")
#         deadline = simpledialog.askstring("Встановити дедлайн", "Введіть дату дедлайну (формат: ДД-ММ-РРРР):")
#         if name and deadline:
#             for task in self.tasks:
#                 if task.name == name:
#                     task.deadline = deadline
#                     break
#             self.view_tasks()
#
#     def add_subtask(self):
#         # name = simpledialog.askstring("Додати підзадачу", "Введіть назву задачі для підзадачі:")
#         # subtask = simpledialog.askstring("Додати підзадачу", "Введіть підзадачу:")
#         # if name and subtask:
#         #     for task in self.tasks:
#         #         if task.name == name:
#         #             task.subtask = subtask
#         #             break
#         # self.view_tasks()
#
#         name = simpledialog.askstring("Додати підзадачу", "Введіть назву задачі для підзадачі:")
#         subtask = simpledialog.askstring("Додати підзадачу", "Введіть підзадачу:")
#         if name and subtask:
#             for task in self.todo_list.tasks:
#                 if task.name == name:
#                     if not hasattr(task, 'subtasks'):
#                         task.subtasks = []  # Создаем список подзадач, если его еще нет
#                     task.subtasks.append(subtask)  # Добавляем подзадачу в список
#                     break
#         self.update_tasks_text()
#
#     def change_deadline(self):
#         name = simpledialog.askstring("Змінити дедлайн", "Введіть назву задачі для зміни дедлайну:")
#         newdeadline = simpledialog.askstring("Змінити дедлайн", "Введіть нову дату дедлайну (формат: ДД-ММ-РРРР):")
#         if name and newdeadline:
#             for task in self.tasks:
#                 if task.name == name:
#                     task.deadline = newdeadline
#                     break
#             self.view_tasks()
#     def add_task(self):
#         name = simpledialog.askstring("Додати задачу", "Введіть назву задачі:")
#         description = simpledialog.askstring("Додати задачу", "Введіть опис задачі:")
#         if name and description:
#             task = Task(name, description)
#             self.tasks.append(task)
#             self.view_tasks()
#
#     def remove_task(self):
#         self.view_tasks()
#         name = simpledialog.askstring("Видалити задачу", "Введіть назву задачі для видалення:")
#         if name:
#             self.tasks = [task for task in self.tasks if task.name != name]
#             self.view_tasks()
#     def complete_task(self):
#         name = simpledialog.askstring("Позначити задачу як виконану", "Введіть назву задачі для позначення виконаною:")
#         if name:
#             for task in self.tasks:
#                 if task.name == name:
#                     task.complete()
#                     self.view_tasks()
#                     break
#
#     def save_to_file(self):
#         save_or_not = messagebox.askyesno("Збереження файлу", "Зберегти файл?")
#         if save_or_not:
#             filename = simpledialog.askstring("Збереження файлу","Введіть ім'я файла з розширенням: ")
#             #filename += ".txt"
#             with open(filename, 'w') as file:
#                 for task in self.tasks:
#                     file.write(f"Задача: {task.name}\n")
#                     file.write(f"Опис: {task.description}\n")
#                     if hasattr(task, 'subtask'):
#                         file.write(f"Підзадача: {task.subtask}\n")
#                     file.write(f"Статус: {'Готово' if task.completed else 'Не готово'}\n")
#                     if hasattr(task, 'deadline'):
#                         file.write(f"Дедлайн: {task.deadline}\n")
#                     file.write("-" * 30 + "\n")
#             messagebox.showinfo("Збереження файлу", f"Задачі збережено в файлі {filename}")
#         else:
#             messagebox.showinfo("Скасовано", "Збереження файлу скасовано")
#
#     def load_from_file(self):
#         filename = simpledialog.askstring("Завантажити файл", "Введіть ім'я файла з розширенням:")
#         if filename:
#             try:
#                 with open(filename, 'r') as file:
#                     lines = file.readlines()
#                     i = 0
#                     while i < len(lines):
#                         name = lines[i].split(": ")[1].strip()
#                         description = lines[i + 1].split(": ")[1].strip()
#                         subtask = lines[i + 2].split(": ")[1].strip() if "Підзадача" in lines[i + 2] else None
#                         completed = True if "Готово" in lines[i + 3] else False
#                         deadline = lines[i + 4].split(": ")[1].strip() if "Дедлайн" in lines[i + 4] else None
#                         task = Task(name, description)
#                         task.subtask = subtask
#                         task.completed = completed
#                         task.deadline = deadline
#                         self.tasks.append(task)
#                         i += 6
#                 print(f"Задачі завантажено з файлу {filename}")
#                 self.view_tasks()
#             except FileNotFoundError:
#                 print(f"Файл {filename} не знайдено.")
#             except Exception as e:
#                 print(f"Помилка при завантаженні з файлу {filename}: {e}")


from tkinter import simpledialog, messagebox

class Task:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.completed = False
        self.deadline = None
        self.subtasks = []

    def complete(self):
        self.completed = True

    def __str__(self):
        completed_status = 'Завершено' if self.completed else 'Не завершено'
        deadline_status = f'Дедлайн: {self.deadline}' if self.deadline else 'Дедлайн не встановлено'
        subtask_status = f'Підзадачі: {", ".join(self.subtasks)}' if self.subtasks else 'Підзадачі не має'
        return f"{self.name} - {self.description} - {subtask_status} - {completed_status} - {deadline_status}"

class TodoList:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        print("Наявні задачі")
        for task in self.tasks:
            print(task)

    def add_deadline(self):
        name = simpledialog.askstring("Встановити дедлайн", "Введіть назву задачі для встановлення дедлайну:")
        deadline = simpledialog.askstring("Встановити дедлайн", "Введіть дату дедлайну (формат: ДД-ММ-РРРР):")
        if name and deadline:
            for task in self.tasks:
                if task.name == name:
                    task.deadline = deadline
                    break
            self.view_tasks()

    def add_subtask(self):
        name = simpledialog.askstring("Додати підзадачу", "Введіть назву задачі для підзадачі:")
        subtask = simpledialog.askstring("Додати підзадачу", "Введіть підзадачу:")
        if name and subtask:
            for task in self.tasks:
                if task.name == name:
                    task.subtasks.append(subtask)
                    break
        self.view_tasks()

    def change_deadline(self):
        name = simpledialog.askstring("Змінити дедлайн", "Введіть назву задачі для зміни дедлайну:")
        newdeadline = simpledialog.askstring("Змінити дедлайн", "Введіть нову дату дедлайну (формат: ДД-ММ-РРРР):")
        if name and newdeadline:
            for task in self.tasks:
                if task.name == name:
                    task.deadline = newdeadline
                    break
            self.view_tasks()

    def add_task(self):
        name = simpledialog.askstring("Додати задачу", "Введіть назву задачі:")
        description = simpledialog.askstring("Додати задачу", "Введіть опис задачі:")
        if name and description:
            task = Task(name, description)
            self.tasks.append(task)
            self.view_tasks()

    def remove_task(self):
        self.view_tasks()
        name = simpledialog.askstring("Видалити задачу", "Введіть назву задачі для видалення:")
        if name:
            self.tasks = [task for task in self.tasks if task.name != name]
            self.view_tasks()

    def complete_task(self):
        name = simpledialog.askstring("Позначити задачу як виконану", "Введіть назву задачі для позначення виконаною:")
        if name:
            for task in self.tasks:
                if task.name == name:
                    task.complete()
                    self.view_tasks()
                    break

    def save_to_file(self):
        save_or_not = messagebox.askyesno("Збереження файлу", "Зберегти файл?")
        if save_or_not:
            filename = simpledialog.askstring("Збереження файлу","Введіть ім'я файла з розширенням: ")
            with open(filename, 'w') as file:
                for task in self.tasks:
                    file.write(f"Задача: {task.name}\n")
                    file.write(f"Опис: {task.description}\n")
                    for subtask in task.subtasks:
                        file.write(f"Підзадача: {subtask}\n")
                    file.write(f"Статус: {'Готово' if task.completed else 'Не готово'}\n")
                    if task.deadline:
                        file.write(f"Дедлайн: {task.deadline}\n")
                    file.write("-" * 30 + "\n")
            messagebox.showinfo("Збереження файлу", f"Задачі збережено в файлі {filename}")
        else:
            messagebox.showinfo("Скасовано", "Збереження файлу скасовано")

    # def load_from_file(self):
    #     filename = simpledialog.askstring("Завантажити файл", "Введіть ім'я файла з розширенням:")
    #     if filename:
    #         try:
    #             with open(filename, 'r') as file:
    #                 lines = file.readlines()
    #                 i = 0
    #                 while i < len(lines):
    #                     name = lines[i].split(": ")[1].strip() if "Задача" in lines[i] else None
    #                     description = lines[i + 1].split(": ")[1].strip() if "Опис" in lines[i + 1] else None
    #                     subtask = lines[i + 2].split(": ")[1].strip() if "Підзадача" in lines[i + 2] else None
    #                     completed = True if "Готово" in lines[i + 3] else False
    #                     deadline = lines[i + 4].split(": ")[1].strip() if "Дедлайн" in lines[i + 4] else None
    #                     task = Task(name, description)
    #                     if subtask:
    #                         if not hasattr(task, 'subtasks'):
    #                             task.subtasks = []
    #                         task.subtasks.append(subtask)
    #                     task.completed = completed
    #                     task.deadline = deadline
    #                     self.tasks.append(task)
    #                     i += 6
    #             print(f"Задачі завантажено з файлу {filename}")
    #             self.view_tasks()
    #         except FileNotFoundError:
    #             print(f"Файл {filename} не знайдено.")
    #         except Exception as e:
    #             print(f"Помилка при завантаженні з файлу {filename}: {e}")


    def load_from_file(self):
        filename = simpledialog.askstring("Завантажити файл", "Введіть ім'я файла з розширенням:")
        if filename:
            try:
                with open(filename, 'r') as file:
                    lines = file.readlines()

                    i = 0
                    while i < len(lines):
                        if "Задача" in lines[i]:
                            name = lines[i].split(": ")[1].strip()
                            description = lines[i + 1].split(": ")[1].strip()
                            subtasks = []
                            j = i + 2
                            while j < len(lines) and "Підзадача" in lines[j]:
                                subtasks.append(lines[j].split(": ")[1].strip())
                                j += 1
                            completed = "Готово" in lines[j]
                            if "Дедлайн" in lines[j + 1]:
                                deadline = lines[j + 1].split(": ")[1].strip()
                                i = j + 2
                            else:
                                deadline = None
                                i = j + 1
                            task = Task(name, description)
                            task.subtasks = subtasks
                            task.completed = completed
                            task.deadline = deadline
                            self.tasks.append(task)
                        else:
                            i += 1
                print(f"Задачі завантажено з файлу {filename}")
                self.view_tasks()
            except FileNotFoundError:
                print(f"Файл {filename} не знайдено.")
            except Exception as e:
                print(f"Помилка при завантаженні з файлу {filename}: {e}")



