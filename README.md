# Command-Line To-Do List Manager

This is a simple command-line tool for managing a to-do list. It allows the user to create, view, and mark off items on their to-do list using a set of command-line arguments.

## Features

- Add new items to the to-do list using the `--add` argument
- Mark items as done by specifying their index using the `--done` argument
- View the current to-do list by running the script without any arguments

## Requirements

- Python 3.x

## Usage

To use the script, save it to a file and run it from the command line. Here are some example usage scenarios:
```
# Add a new item to the to-do list
python todo.py --add "Buy milk"

# Mark the second item as done
python todo.py --done 2

# View the to-do list
python todo.py
```
## Documentation

The to-do list manager is implemented as a single Python script, `todo.py`. It uses the `argparse` module to parse command-line arguments and a simple text file to store the to-do list.

The script defines several functions to load and save the to-do list, add new items, mark items as done, and list the items. The `main` function uses these functions to perform the desired actions based on the command-line arguments.

### `load_todo_list()`

This function loads the to-do list from a text file and returns it as a list of strings.

### `save_todo_list(todo_list)`

This function saves the to-do list to a text file.

### `add_item(todo_list, item)`

This function adds a new item to the to-do list and saves the updated list to the text file.

### `mark_done(todo_list, index)`

This function removes the item at the specified index from the to-do list and saves the updated list to the text file.

### `list_items(todo_list)`

This function prints the to-do list to the console.

## Limitations

- The to-do list is stored in a simple text file, so it will be lost if the file is deleted or the script is run on a different machine.
