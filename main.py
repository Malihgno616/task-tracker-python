"""
Requirements

- [] Add, Update, and Delete tasks

- [] Mark a task as in progress or done

- [] List all tasks

- [] List all tasks that are done

- [] List all tasks that are not done

- [] List all tasks that are in progress

"""
import os 

class TaskCLI:
    
    def generate_title(self):
        print("------Task Tracker------")

    def generate_interface(self):
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
        print("\n---Create a task---")
        input("Title: ")
        input("Description: ")

    def update_tasks(self):
        print("Update a task")
        
    def view_tasks(self):
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
        print("\nAll tasks")

    def tasks_pending(self):
        print("\nPending tasks...")

    def tasks_in_progress(self):
        print("\nIn-Progress tasks...")

    def done_tasks(self):
        print("\nDone tasks")
    
    def exit_task_cli(self):
        print("Goodbye!!!")
        
interface = TaskCLI()

while True:
    interface.generate_title()
    interface.generate_interface()
    break