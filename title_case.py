def format_name(f_name, l_name):
    """Takes the first and last name
    and exports both in title case"""
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


print(format_name("AnGEla", "YU"))
