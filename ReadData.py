def read_file(file):
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