# standard.py

def colors_function():
    """
    Returns a dictionary of common terminal colors
    that can be used to print colored text.
    Usage:
        colors = get_colors()
        print(colors['red'] + "This is red text" + colors['reset'])
    """
    colors = {
        "reset": "\033[0m",
        "bold": "\033[1m",
        "black": "\033[30m",
        "red": "\033[31m",
        "green": "\033[32m",
        "yellow": "\033[33m",
        "blue": "\033[34m",
        "magenta": "\033[35m",
        "cyan": "\033[36m",
        "white": "\033[37m",
        "bright_black": "\033[90m",
        "bright_red": "\033[91m",
        "bright_green": "\033[92m",
        "bright_yellow": "\033[93m",
        "bright_blue": "\033[94m",
        "bright_magenta": "\033[95m",
        "bright_cyan": "\033[96m",
        "bright_white": "\033[97m"
    }
    return colors

colors = colors_function()

def valid_input_function(prompt_message, allow_float=False, allow_negative=True):
    """
    This function keeps prompting the user continously 
    until they enter a valid number or 'exit/back/stop' to exit.
    it only works with (int) until the coder makes allow_float=True.. then it allows float numbers!

    Paramaters:
        prompt_message (str): The message shown to the user
        allow_float (bool): True if decimal numbers are allowed. (Default: False)
        allow_negative (bool): True if negative numbers are allowed. (Default: True)

    returns:
        - int or float (depending on allow_float)
        - "exit" if user typed exit/back/stop
    """
    colors = colors_function()
    while True:
        user_input = input(prompt_message)

        if user_input.lower() in ("stop", "back", "exit", "leave", "end", "bye", "return"):
            return "exit"

        try:
            evaluated = float(eval(user_input))  # evaluate simple math expressions
            if not allow_negative and evaluated < 0:
                print(colors['bright_red']+"   **Can't have Negative Numbers!!**"+ colors['reset'])
                continue
            if not allow_float and not evaluated.is_integer():
                print(colors['bright_red']+"   **Can't have float!!**"+ colors['reset'])
                continue
            return int(evaluated) if not allow_float else evaluated
        except ZeroDivisionError:
            print(colors['bright_red'] + "   **You tried to divide by zero :( **" + colors['reset'])
        except:
            print(colors['bright_red'] + "   **Must be a number or valid expression! Please try again.**"+ colors['reset'])

def unit_choice_function(prompt, units_list):
    """
    This function was made to reduce code repetition..
    it gets the unit choice and compares it to check if its
    within the list boundaries... if not then it prompts the user to try again.

    Paramaters:
        prompt (str): The message shown to the user
        units_list (list): your list that you want to compare with

    """

    while True:
        choice = input(prompt)

        if choice.lower() == "list":
            print()
            print_list_function(units_list)
            continue

        elif choice.lower() in ("stop", "back", "exit", "leave", "end", "bye", "return"):
            return "exit"
        
        try:
            if not float(choice).is_integer():
                print(colors['red'] + "   **Can't have floats!!!***"+ colors['reset'])
                continue
            choice = int(choice) 

        except ValueError:
            print(f"{colors['bright_red']}**Please enter a number or type 'list' to show available units.**{colors['reset']}")
            continue

        if 1 <= choice <= len(units_list):
            return choice

def print_list_function(your_list,max_rows=4,spacing=12):
    """"
    This function neatly prints as tables the requested list
    its modular and adjustable.

    max rows by default is 4
    columns are added as the list needs.

    Paramaters:
        your_list (list): prints this list in a 4 row max
        max_rows (int): max rows you'd like to have
        spacing (int): spacing between each line (default 12)
    
    """
    from math import ceil

    # max_rows = 4   # max number of rows.. (default: 4)
    columns = ceil(len(your_list) / max_rows)     
    # takes number of rows divides it by length of list
    # if number of rows was 3.2 it becomes 4. cuz cant have float number as a coulmn

    for i in range(max_rows):            # each row (horizontal)
        for j in range(columns):         # each column (vertical)
            index = i + j * max_rows     # computes index for each cell
            if index < len(your_list):
                print(f" {index+1:2d}- {your_list[index]:<{spacing}}".title(), end="|")
        print()  # move to next line after each row
    print()

def print_welcome_message(info_message,category_name):
        print(
        "-" * 40 + f"{colors['bold']}{colors['bright_magenta']}\n"
        f"--Welcome to {colors['bright_blue']}{category_name}{colors['bright_magenta']} Mode--" 
        f"{colors['cyan']}\n*INFO: {colors['reset']}{colors['cyan']} {info_message}.*{colors['reset']}\n"
        + "-" * 40 + "\n" 
        )

colors = colors_function()

