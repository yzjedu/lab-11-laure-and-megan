
def read_file_to_dict(filename):
    # Open the file for reading

    morse_dict = {}
    morse_data = open(filename, 'r')

    # Read each line, convert to integer, and append to the grades list
    for line in morse_data:
        items = line.split('  ')
        key = items[1]
        value = items[0]
        morse_dict[key] = value
    morse_data.close()
    return morse_data

def get_morse_file():
    morse_file = input('What is the file in morse code you would like to convert?')
    return morse_file

def convert_file(morse_file, morse_dict):
    morse_file_data = open(morse_file, 'r')



def main():
    print(read_file_to_dict('morsecode.txt'))

