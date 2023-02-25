def del_multiple_keys(input_dict: dict, del_keys: [list]):
    for del_key in del_keys:
        del input_dict[del_key]


def pop_multiple_keys(input_dict: dict, pop_keys: [list]):
    for pop_key in pop_keys:
        input_dict.pop(pop_key, None)
