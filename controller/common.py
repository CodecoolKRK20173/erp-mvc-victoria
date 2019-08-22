from view.terminal_view import get_inputs

def get_user_record(labels):
    user_inputs = []
    record = []
    for label in labels:
        user_inputs.append(get_inputs([f"{label}: "], ""))
    for user_input in user_inputs:
        record.append(user_input[0])
    return record
