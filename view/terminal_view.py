""" Terminal view module """


def print_table(table, title_list):
    table.insert(0, title_list)
    i = 1
    # list of all elements for the table (except index)
    item_list = []
    # longest item in table column
    item_length = []
    while i < len(table[0]):
        for item in table:
            item_list.append(item[i])
        i += 1
    # amount of columns for future table
    data_table_length = len(table)
    # adding length of first column (id)
    item_length.append(8)
    # getting the longest element from each column
    i = 1
    while i < len(table[0]):
        item_length.append(len(max(item_list[data_table_length*(i-1):data_table_length*i], key = len)))
        i += 1
    
    # amount of dashes for all the columns
    amount_of_dashes = 0
    for column in item_length:
        amount_of_dashes += column

    # adding spaces between columns
    amount_of_dashes += (len(table[0]) + 2) * 2
    amount_of_dashes = "-" * amount_of_dashes
    
    #printing the table
    print(f"/{amount_of_dashes}\\")
    
    i = 0
    while i < len(table[0]):
        for row in table:
            row[i] = row[i].rjust(item_length[i])
        i += 1

    for row in table:
        print("|"," | ".join(row),"|")
        print(f"{amount_of_dashes}--")


def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def print_menu(title, list_options, exit_message):
    """
    Displays a menu. Sample output:
        Main menu:
            (1) Store manager
            (2) Human resources manager
            (3) Inventory manager
            (4) Accounting manager
            (5) Sales manager
            (6) Customer relationship management (CRM)
            (0) Exit program

    Args:
        title (str): menu title
        list_options (list): list of strings - options that will be shown in menu
        exit_message (str): the last option with (0) (example: "Back to main menu")

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code


def get_inputs(list_labels, title):
    """
    Gets list of inputs from the user.
    Sample call:
        get_inputs(["Name","Surname","Age"],"Please provide your personal information")
    Sample display:
        Please provide your personal information
        Name <user_input_1>
        Surname <user_input_2>
        Age <user_input_3>

    Args:
        list_labels (list): labels of inputs
        title (string): title of the "input section"

    Returns:
        list: List of data given by the user. Sample return:
            [<user_input_1>, <user_input_2>, <user_input_3>]
    """
    inputs = []

    # your code

    return inputs

def get_choice(options):
    print_menu("Main menu",options, "Exit program")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]

def print_error_message(message):
    """
    Displays an error message (example: ``Error: @message``)

    Args:
        message (str): error message to be displayed

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    # your code
