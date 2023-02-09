FILEPATH = "todos.txt"

def get_todos():
    """Function to read data from a text file and
     returning it stored in a list
     """
    with open(FILEPATH, 'r') as file:
        todos = file.readlines()
    return todos

#print(help(get_todos))

def write_todos(todos):
    with open(FILEPATH, 'w') as file:
        file.writelines(todos)


if __name__ == "__main__":
    print("Hello")
    print("This is a testament to the fact that only when this 'functions.py'\
    is run, does the if condition get executed here. Otherwise \
    if the main.py file is run then the __name__ is funtions nd not '__main__'")