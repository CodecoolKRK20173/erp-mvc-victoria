""" Common functions for models
implement commonly used functions here
"""
import random
from controller.common import get_user_record

def generate_random(table):
    """
    Generates random and unique string. Used for id/key generation:
         - at least 2 special characters (except: ';'), 2 number, 2 lower and 2 upper case letter
         - it must be unique in the table (first value in every row is the id)

    Args:
        table (list): Data table to work on. First columns containing the keys.

    Returns:
        string: Random and unique string
    """

    generated = []

    # getting list of existing ids in the table
    id_list = []
    for item in table:
        id_list.append(item[0])
    special_characters = list(map(chr, range(33, 48))) + list(map(chr, range(58, 59))) + list(map(chr, range(60, 65))) + list(map(chr, range(123, 127)))
    numbers = list(map(chr, range(48, 58)))
    lower_case_letters = list(map(chr, range(97, 123)))
    upper_case_letters = list(map(chr, range(65, 91)))
    is_generating = True
    while is_generating:
        i = 0
        while i < 2:
            generated.append(random.choice(lower_case_letters))
            generated.append(random.choice(upper_case_letters))
            generated.append(random.choice(numbers))
            generated.append(random.choice(special_characters))
            i += 1
        if "".join(generated) not in id_list:
            is_generating = False
        else:
            generated = []
    random.shuffle(generated)

    return "".join(generated)

def add_new_record(table, labels):
    record = get_user_record(labels)
    record.insert(0, generate_random(table))
    table.append(record)
    print(table)
    return table
    