# task_bot.py
tasks = []

def add_task(task):
    tasks.append(task)
    return f"Task '{task}' added!"

def main():
    print("Welcome to TaskBot! Type 'quit' to exit.")
    while True:
        user_input = input("Please enter your task: ")
        
        if user_input.lower() == "quit":
            print("Goodbye!")
            break

        print("ChatGPT analyzing...")
        feedback = add_task(user_input)
        
        confirmation = input(f"{feedback} Confirm? (yes/no): ")

        if confirmation.lower() == "yes":
            print("ChatGPT: Task confirmed!")
        else:
            tasks.remove(user_input)
            print("ChatGPT: Task removed.")

        print(f"Current Tasks: {tasks}")

if __name__ == "__main__":
    main()
