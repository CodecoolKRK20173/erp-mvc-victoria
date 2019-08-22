# everything you'll need is imported:
from model.store import store
from model.common import get_user_id
from model import data_manager
from view import terminal_view
from controller import common
from controller import root_controller

def run():
    options = ["Display data as a table",
               "Add new data",
               "Remove data",
               "Update",
               "Get amount of games by each manufactor",
               "Get amount of games by manufacture"]
    table_titles = ["id", "title", "manufacturer", "price", "in_stock"]
    choice = None
    while choice != "0":
        terminal_view.print_menu("Store manager menu ", options, "Go back to main menu")
        inputs = terminal_view.get_inputs(["Please enter a number: "], "")
        choice = inputs[0]
        #reading data from file
        data_table = data_manager.get_table_from_file("model/store/games.csv")
        if choice == "1":
            terminal_view.print_table(data_table, table_titles)
        elif choice == "2":
            table_titles.pop(0)
            store.add(data_table, table_titles)
        elif choice == "3":
            store.remove(data_table, get_user_id("remove"))
        elif choice == "4":
            store.update(data_table, get_user_id("update"), common.get_user_record(table_titles[1:]))
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        elif choice == "0":
            root_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")

