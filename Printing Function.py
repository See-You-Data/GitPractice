# We can all work on a simple printing function here to get used to Git.
# We could all add different functionality to the function, i.e. the ability for user to input various parameters to alter output, etc.
# Just do whatever, following a nice (Atlassian-approved) Git workflow.
# Would be good to include function documentation (would be good to agree on a documentation standard i.e. NumPy's style).
# Also it'd be best if our changes edit the code of others as this will cause merge conflicts which are presumably a bit trickier to fix & thus good practice. 

def printer(input,case=None):
    if case == 'title':
        print(input.title())
    elif case == 'upper':
        print(input.upper())
    else:
        print(input)
  
printer('hello',case='upper')
