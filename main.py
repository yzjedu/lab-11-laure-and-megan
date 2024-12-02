#Programmers Laure and Megan
# Course: CS151, Dr Zelalem Yalew
# Due Date: 2/12/24
# Lab Assignemnt 11
# Problem Statement: Make a program to converse ciphers into plain English
# Data In: User input, morse code data
# Data Out:  plain English
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
    with open(morse_file, 'r') as morse_file_data:
        decoded_message = []
        for line in morse_file_data:
            morse_words = line.strip().split(' ')
            decoded_words = [
                morse_dict.get(morse_char, '?')  # Replace unknown characters with '?'
                for morse_char in morse_words
            ]
            decoded_message.append(''.join(decoded_words))  # Combine characters into words
return



def main():
    print(read_file_to_dict('morsecode.txt'))
morse_file = get_morse_file()

try:
        decoded_text = convert_file(morse_file, morse_dict)
        print("\nDecoded Message:")
        print(decoded_text)
    except FileNotFoundError:
        print("Error: The file specified could not be found. Please check the file name.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()