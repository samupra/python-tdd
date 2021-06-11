def handle_single_greeting(name):
    if name.isupper():
        return "HELLO {}!".format(name)

    return "Hello, {}.".format(name)


def handle_two_elements(names):
    return "Hello, {} and {}.".format(names[0], names[1])


def normal_case_names(name):
    if name.isupper():
        return False
    return True


def upper_case_names(name):
    return name.isupper()


def build_normal_case_greeting(names):
    if len(names) == 0:
        return ""
    # If after filter, we only have 1 normal case element left, its a simple greeting
    if len(names) == 2:
        return handle_two_elements(names)
    elif len(names) > 2:
        string = "Hello,"
        for i in range(0, len(names) - 1):
            string += " " + names[i] + ","
        string += " and "
        string += names[len(names) - 1]
        string += "."
        return string
    return handle_single_greeting(names[0])

def build_upper_case_greeting(prefix, names):
    if len(names) == 0:
        return ""
    if len(names) > 1:
        string = " HELLO "
        for i in range(0, len(names) - 1):
            string += names[i] + "!"
        string += " AND "
        string += names[len(names) - 1]
        string += "!"
        return string
    else:
        return prefix + handle_single_greeting(names[0])

def handle_arbitary_elements(names):
    normal_case = filter(normal_case_names, names)
    upper_case = filter(upper_case_names, names)

    # Handle special case where only one element in upper case array, and normal case exists
    if len(normal_case) >= 1 and len(upper_case) == 1:
        prefix = " AND "
    else:
        prefix = ""

    return build_normal_case_greeting(normal_case) + build_upper_case_greeting(prefix, upper_case)


def handle_commas_and_escaped_strings(names):
    split_strings = []
    for name in names:
        if '"' in name:
            split_strings.append(name.replace('"', ''))
        else:
            # Remove space
            name_without_space = name.replace(" ", "")
            split_strings.extend(name_without_space.split(","))
    return split_strings


def greet(name):
    if name is None:
        return "Hello, my friend."

    if isinstance(name, str):
        return handle_single_greeting(name)

    if isinstance(name, list):
        extracted_names = handle_commas_and_escaped_strings(name)
        if len(extracted_names) == 2:
            return handle_two_elements(extracted_names)
        else:
            return handle_arbitary_elements(extracted_names)

    raise ValueError("Input must be either string or array")

if __name__ == '__main__':
    greet('PyCharm')
