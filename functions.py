print(__name__)
if __name__ == "__main__":
    print("hello, I am in functions.py file")

FILEPATH = 'todos.txt'


def get_todos(filepath_local=FILEPATH):
    """ Read a text file and returns a
    list of to-do items.
    """
    with open(filepath_local, 'r') as file_local:
        todos_local = file_local.readlines()  # read lines from file
    return todos_local


def write_todos(todos_arg, filepath_local=FILEPATH):
    """ write the to-do items list in the text file."""
    with open(filepath_local, 'w') as file_local:
        file_local.writelines(todos_arg)


