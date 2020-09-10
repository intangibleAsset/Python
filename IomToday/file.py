import pickle
import datetime

def pickle_object(object, file_name):
    """Pickle object : pickle_object(object, file_name)."""
    outfile = open(file_name,'wb')
    pickle.dump(object, outfile)
    outfile.close()

def unpickle_object(file_name):
    """Unpickle object : unpickle_object(object, file_name)"""
    infile = open(file_name,'rb')
    unpickled_object = pickle.load(infile)
    infile.close()
    return(unpickled_object)

def read_from_file(file_name):
    """Read from file : read_from_file(file_name)."""
    with open(file_name,"r") as file:
        amount = file.read()
    return(amount)

def write_to_file(data, file_name):#writes the file contents to the file overwriting the last update
    """Write to file : write_to_file(data, file_name)."""
    with open(file_name,"w") as file:
        file.write(data)

def accessed_in_last_hour():
    now = datetime.datetime.now()
    last_accessed_time = unpickle_object('accessedTime')
    if last_accessed_time < (now - datetime.timedelta(minutes=60)):
        pickle_object(now,'accessedTime')
        return(False)
    else:
        return(True)
