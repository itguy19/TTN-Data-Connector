'''ReadData
    Author: Andras Tarlos
    Date: 03/04/23
    Version: 1.0

Description:

This short Python file reads important data from the data directory.
It is always best practices, not to hardcode passwords. :)

'''


def read_file(file):
    """_summary_

    Args:
        file : A oneliner file with a key

    Raises:
        Exception: Input / Output Error

    Returns:
        str: Returns the key from the selected file
    """    
    try:
        with open("data/" + file, 'r') as fd:
            lines = fd.readline()
            fd.close()
            return lines
    except IOError:
        raise Exception("Can't open password file for reading.") 
    
def read_api_key():
    return read_file("api_key")

def read_app_id():    
    return read_file("app_id")

def read_iot_api_key():
    return read_file("iot_api_key")