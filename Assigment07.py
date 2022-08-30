# ------------------------------------------------- #
# Title: Lab7-1
# Description: A simple example of storing data in a binary file
# ChangeLog: (Who, When, What)
# <WeiWang>,<8.28.2022>,Created Script
# ------------------------------------------------- #

import pickle  # This imports code from another code file!

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []


# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    # Use binary mode to save data
    with (open(file_name, "wb")) as openfile:
        pickle.dump(list_of_data, openfile)


def read_data_from_file(file_name):
    # Use binary mode to read data
    with (open(file_name, "rb")) as openfile:
        return pickle.load(openfile)


def input_data_to_list():
    id = input("Enter an ID:")
    name = input("Enter an name:")
    return [id, name]


# Presentation ------------------------------------ #
# TODO: Get ID and NAME From user, then store it in a list object
lstCustomer = input_data_to_list()
# TODO: store the list object into a binary file
save_data_to_file(strFileName, lstCustomer)
print("Successfully stored the data to " + strFileName)

# TODO: Read the data from the file into a new list object and display the contents
print("\nReading the data from the file ...")
data_from_file = read_data_from_file(strFileName)
print(data_from_file)
