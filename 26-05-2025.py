from tempfile import TemporaryFile

with TemporaryFile() as temp_file:
    # Write some data to the temporary file
    temp_file.write(b'This is a temporary file.\n')
    
    # Move the cursor to the beginning of the file
    temp_file.seek(0)
    
    # Read the data back from the temporary file
    data = temp_file.read()
    print(data.decode('utf-8'))  # Output: This is a temporary file.


def my_function(*,    param1=None,
                 param2=None):
    """    Example function that takes keyword-only parameters.
    Args:
        param1 (str): First parameter
        param2 (str): Second parameter
    """ 
    print("Function called!")

def my_functions_2(/param1=None, param2=None):
    """Example function that takes positional-only parameters.
    
    Args:
        param1 (str): First parameter
        param2 (str): Second parameter
    """
    print("Function called with positional-only parameters!")