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
            item_list.append(str(item[i]))
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
    
    i = 0
    while i < len(table[0]):
        for row in table:
            row[i] = row[i].lstrip(" ")
        i += 1

def print_result(result, label):
    """
    Displays results of the special functions.

    Args:
        result: result of the special function (string, list or dict)
        label (str): label of the result

    Returns:
        None: This function doesn't return anything it only prints to console.
    """

    print(f"{label}: ")
    print(result)

def print_menu(title, list_options, exit_message):
    print(f"{title}: ")
    for index, option in enumerate(list_options):
        print(f"    ({index+1}) {option}")
    print(f"    (0) {exit_message}")


def get_inputs(list_labels, title):
    inputs = []

    for label in list_labels:
        user_input = input(label)
        inputs.append(user_input)

    return inputs

def get_choice(options):
    print_menu("Main menu",options, "Exit program")
    inputs = get_inputs(["Please enter a number: "], "")
    return inputs[0]

def print_error_message(message):
    print(f"``Error: {message}``")
