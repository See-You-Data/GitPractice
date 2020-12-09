# We can all work on a simple printing function here to get used to Git.
# We could all add different functionality to the function, i.e. the ability for user to input various parameters to alter output, etc.
# Just do whatever, following a nice (Atlassian-approved) Git workflow.
# Would be good to include function documentation (would be good to agree on a documentation standard i.e. NumPy's style).
# Also it'd be best if our changes edit the code of others as this will cause merge conflicts which are presumably a bit trickier to fix & thus good practice. 

#JS Commented out lines of code to force conflict, this can happen with improper git workflow

# def printer(input,case=None):
#     if case == 'title':
#         print(input.title())
#     elif case == 'upper':
#         print(input.upper())
#     else:
#         print(input)
#
# printer('hello',case='upper')


def print_func(input_string, case=None):
    """Function prints an input string with optional argument to specify the case of the printed string.

    Parameters
    ----------
    input_string : str
        The string to be printed to screen.
    case : str / None (Optional)
        Pass 'title', 'upper' or 'lower' to apply the corresponding string function to the input string before printing.
    """
    if case == 'title':
        print(2 * input_string.title())  # sets the first letter of each word to upper case
    elif case == 'upper':
        print(2 * input_string.upper())  # sets string to all upper case
    elif case == 'lower':
        print(2 * input_string.lower())  # sets string to all lower case
    else:
        print(2 * input_string)  # if no 'case' argument is passed, returns the raw input string printed twice


print_func('hello', case='upper')
