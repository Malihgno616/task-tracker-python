"""
Requirements

- [] Add, Update, and Delete tasks
- [x] Created a function to add a task

- [] Mark a task as in progress or done

- [] List all tasks

- [] List all tasks that are done

- [] List all tasks that are not done

- [] List all tasks that are in progress

"""
import os 
import json
from datetime import datetime as date

class TaskCLI:
    
    def clear_cli(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def generate_title(self):
        print("------Welcome to the Task Tracker------")

    def generate_interface(self):
        self.clear_cli()
        self.generate_title()
        print("1. Create Task")
        print("\n2. View your Tasks")
        print("\n3. Exit\n")   
        input_option = int(input("Select an option (1, 2 or 3): " ))
        if input_option == 1:
            self.create_tasks()
        elif input_option == 2:
            self.view_tasks()
        elif input_option == 3:
            self.exit_task_cli()  
        else:
            print("Opção inválida")
            return self.generate_interface()
            
    def create_tasks(self):
        self.clear_cli()
        print("\n---Create a task---")
        
        while True:
            title = str(input("Title: ")).strip()
            description = str(input("Description: ")).strip()
            if not title or not description:
                self.clear_cli()
                message = {"message": "Title and description cannot be empty"}
                print("\n" + message["message"])
            else:
                break

        created_at = date.now().isoformat()
        updated_at = date.now().isoformat()
        
        tasks = []
        if os.path.exists("task.json"):
            with open("task.json", "r", encoding="utf-8") as f:
                try:
                    tasks = json.load(f)

                    if isinstance(tasks, dict):
                        tasks = [data]
                    
                    if not isinstance(tasks, list):
                        tasks = []
                        
                except json.JSONDecodeError:
                    tasks = []
        else:
            with open("task.json", "w", encoding="utf-8") as f:
                json.dump([], f, indent=5, ensure_ascii=False)
            tasks = []

        if tasks:
            max_id = max(task.get("id", 0) for task in tasks)
            new_id = max_id + 1
        else:
            new_id = 1

        data = {
            "id": new_id,
            "title": title,
            "description": description,
            "status": "todo",
            "createdAt": created_at,
            "updatedAt": updated_at
        }       
        
        tasks.append(data)

        with open("task.json", "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=5, ensure_ascii=False)
        
        message = {
            "message": "Task created successfully!!",
            "task": {
                "title": data["title"],
                "description": data["description"],
                "status": data["status"],
                "createdAt": data["createdAt"],
                "updatedAt": data["updatedAt"] 
            }
        }
        self.clear_cli()
        
        print(json.dumps(message, indent=4, ensure_ascii=False))
        
        while True:
            question_input = str(input("Do you want to add a new task? (y/n): ")).strip().lower()
            if question_input == "y":
                self.create_tasks()
            elif question_input == "n":
                self.exit_task_cli()
                break
            else:
                print("Please, y or n")

        return message

    def update_tasks(self):
        self.clear_cli()
        print("Update a task")
        
    def view_tasks(self):
        self.clear_cli()
        print("\n---View your tasks---")
        print("\nView yours task's status")
        print("\n1. Todo, 2. In-Progress, 3. Done or 4. Pending")
        status = int(input("Type 1, 2, 3 or 4:"))
        
        if status == 1:
            self.all_tasks()
        elif status == 2:
            self.tasks_in_progress()
        elif status == 3:  
            self.done_tasks()
        elif status == 4:
            self.tasks_pending()
        else: 
            print("Opção inválido")
            return self.view_tasks()

    def all_tasks(self):
        self.clear_cli()
        print("\nAll tasks")

    def tasks_pending(self):
        self.clear_cli()
        print("\nPending tasks...")

    def tasks_in_progress(self):
        self.clear_cli()
        print("\nIn-Progress tasks...")

    def done_tasks(self):
        self.clear_cli()
        print("\nDone tasks")
    
    def exit_task_cli(self):
        self.clear_cli()
        print("Goodbye!!!")
        
interface = TaskCLI()

while True:
    interface.generate_interface()
    break