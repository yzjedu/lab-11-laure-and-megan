
def read_file_to_dictionary(filename):
    # Open the file for reading
    file_data = open(filename, 'r')
    morse_dict = {}

    # Read each line, convert to integer, and append to the grades list
    for line in file_data:
        key, value = line.split('\t')
        morse_dict[key] = value

    # Close the file
    file_data.close()

    # Return the list of grades
    return morse_dict

def get_morse_file():
    morse_file = input('What is the file in morse code you would like to convert?')
    return morse_file

def main():
    filename = morsecode.txt
    read_file_to_dictionary(filename)
    get_morse_file()
