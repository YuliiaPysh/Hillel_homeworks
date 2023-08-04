def argument_type(item1, item2):
    if isinstance(item1, (int, float)) and isinstance(item2, (int, float)):
        return item1 * item2
    elif isinstance(item1, str) and isinstance(item2, str):
        return item1 + item2
    else:
        return item1, item2
