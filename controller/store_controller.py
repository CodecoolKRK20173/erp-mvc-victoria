# everything you'll need is imported:
from model.store import store
from model import data_manager
from view import terminal_view
from controller import common
from controller import root_controller

def choose():
    #reading data from file
    data_table = data_manager.get_table_from_file("model/store/games.csv")
    #getting user inputs
    inputs = terminal_view.get_inputs(["Please enter a number: "], "")
    option = inputs[0]
    if option == "1":
        terminal_view.print_table(data_table, ["id", "title", "manufacturer", "price", "in_stock"])
    elif option == "2":
        add(data_table)
    elif option == "3":
        inputs = terminal_view.get_inputs(["Enter an id of record you'd like to delete: "], "")
        id_to_delete = inputs[0]
        remove(data_table, id_to_delete)
    elif option == "4":
        inputs = terminal_view.get_inputs(["Enter an id of record you'd like to update: "], "")
        id_to_update = inputs[0]
        update(data_table, id_to_update)
    elif option == "5":
        get_counts_by_manufacturers(data_table)
    elif option == "6":
        inputs = terminal_view.get_inputs(["By which manufacter to search? "], "")
        user_manufactor = inputs[0]
        get_average_by_manufacturer(data_table, user_manufactor)
    elif option == "0":
        root_controller.run()
    else:
        raise KeyError("There is no such option.")


def handle_menu():
    #print('\x1b[H\x1b[2J', end='')
    options = ["Display data as a table", "Add new data", "Remove data", "Update", "Get amount of games by each manufactor", "Get amount of games by manufacture"]
    terminal_view.print_menu("Store menu", options, "Exit program")


def run():
    is_running = True
    while is_running:
        handle_menu()
        try:
            choose()
            is_running = False
        except KeyError as err:
            terminal_view.print_error_message(str(err))

