import argparse

def load_todo_list():
    # Load the to-do list from a text file and return it as a list of strings
    with open('todo.txt', 'r') as f:
        todo_list = [line.strip() for line in f]
    return todo_list

def save_todo_list(todo_list):
    # Save the to-do list to a text file
    with open('todo.txt', 'w') as f:
        for item in todo_list:
            f.write(item + '\n')

def add_item(todo_list, item):
    # Add an item to the to-do list
    todo_list.append(item)
    save_todo_list(todo_list)

def mark_done(todo_list, index):
    # Mark an item as done by removing it from the list
    del todo_list[index]
    save_todo_list(todo_list)

def list_items(todo_list):
    # Print the to-do list
    for i, item in enumerate(todo_list):
        print(f'{i+1}. {item}')

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', help='add a new item to the to-do list')
    parser.add_argument('--done', type=int, help='mark an item as done')
    args = parser.parse_args()

    # Load the to-do list
    todo_list = load_todo_list()

    # Add a new item or mark an item as done, if specified
    if args.add:
        add_item(todo_list, args.add)
    elif args.done:
        mark_done(todo_list, args.done - 1)

    # Print the to-do list
    list_items(todo_list)

if __name__ == '__main__':
    main()
