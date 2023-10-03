FILEPATH = "text.txt"


def get_todos(filepath="text1.txt"):
    # to get the help in the usage of function, we use documents such as:
    """ Read the text file and return the list of to-do items."""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todo_arg, filepath="text1.txt"):
    with open(filepath, 'w') as file_local:
        file_local.writelines(todo_arg)
