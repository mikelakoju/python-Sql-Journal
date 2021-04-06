from database import create_table, add_entry, get_entries

menu = """Please select one of the following options:
1) Add new entry for today.
2) View entries.
3) Exit.

Your selection: """

welcome = "Welcome to the programming diary"


def prompt_new_entry():
    entry_content = input("What have you learnt today : ")
    entry_date = input("Enter date 'DD/mm/yyyy' : ")

    add_entry(entry_content, entry_date)


def view_entries(entries):
    """
    viewing entries from the database
    """
    for entry in entries:
        print(f"{entry['date']}\n{entry['content']}\n\n")


print(welcome)
create_table()

user_input = input(menu)
while user_input != "3":
    # do something the user wants!!!
    if user_input == "1":
        prompt_new_entry()

    elif user_input == "2":
        view_entries(get_entries(entries))

    else:
        print("Invalid option please try again")

    user_input = input(menu)
