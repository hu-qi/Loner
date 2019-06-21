# def get_formatted_name(first, last):
#     """Generate a neatly formatted full name."""
#     full_name = first + ' ' + last
#     return full_name.title()

# def get_formatted_name(first, middle, last):
#     """生成整洁的姓名"""
#     full_name = first + ' ' + middle + ' ' + last
#     return full_name.title()


def get_formatted_name(first, last, middle=''):
    """生成整洁的姓名"""
    if middle:
        full_name = first + ' ' + middle + ' ' + last
    else:
        full_name = first + ' ' + last
    return full_name.title()