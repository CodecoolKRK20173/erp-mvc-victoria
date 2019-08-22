# everything you'll need is imported:
from model.hr import hr
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
               "Who is the oldest person?",
               "Who is the closest to the average age?"]
    choice = None
    while choice != "0":
        terminal_view.print_menu("Human resources menu ", options, "Go back to main menu")
        inputs = terminal_view.get_inputs(["Please enter a number: "], "")
        choice = inputs[0]
        table_titles = ["id", "name", "year of birth"]
        #reading data from file
        data_table = data_manager.get_table_from_file("model/hr/persons.csv")
        if choice == "1":
            terminal_view.print_table(data_table, table_titles)
        elif choice == "2":
            table_titles.pop(0)
            hr.add(data_table, table_titles)
        elif choice == "3":
            hr.remove(data_table, get_user_id("remove"))
        elif choice == "4":
            hr.update(data_table, get_user_id("update"), common.get_user_record(table_titles[1:]))
        elif choice == "5":
            sales_controller.run()
        elif choice == "6":
            crm_controller.run()
        elif choice == "0":
            root_controller.run()
        else:
            terminal_view.print_error_message("There is no such choice.")
