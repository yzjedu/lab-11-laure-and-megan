# Programmers: Laure and Megan
# Course: CS151, Dr. Zee
# Due Date: 2/12/24
# Lab Assignment: Lab 11
# Problem Statement: Make a program to convert morse code ciphers into plain English
# Data In: User input, morse code data
# Data Out: translated message in english
# Credits: codes from the repository and class notes
# Input Files: .txt, morse1.txt, morse2.txt, morse3.txt, and/or morsecode.txt expected

# Purpose: asks the user which file to convert to a dictionary
# Parameters: none
# Return: morse_dict_file, string, name of file that will be converted to a dictionary
def get_morse_dict_file():
    # ask the user which file they would like to use as a dictionary
    morse_dict_file = input('Welcome! This program converts files from morse code and outputs a new file with the translation in English. \n Which file would you like to use as the key or dictionary?')
    # morse_dict_file error checking
    while morse_dict_file != 'morsecode.txt':
        morse_dict_file = input('That is not a correct file. Which file would you like to use as the key or dictionary?')
    return morse_dict_file

# Purpose: reads the file to a dictionary
# Parameters: morse_dict_file, string, the name of the file that will be read into a dictionary
# Return: morse_dict, dictionary, dictionary that converts morse code to English
def read_file_to_dict(morse_dict_file):
    # initialize dictionary
    morse_dict = {}
    # try opening the file for reading
    try:
        morse_data = open(morse_dict_file, 'r')
        # Read each line, and add to morse_dict
        for line in morse_data:
            items = line.split('  ')
            key = items[1]
            value = items[0]
            morse_dict[key] = value
        #close the file and return the dictionary
        morse_data.close()
        return morse_dict
    # alert user in case of error
    except FileNotFoundError:
        print('File not found.')

# Purpose: asks the user which file to convert
# Parameters: none
# Return: morse_file, string, name of the file that the user would like converted to English
def get_morse_file():
    # ask the user which file they would like to convert
    morse_file = input('What is the file in morse code you would like to convert?')
    #morse_file input error checking
    while morse_file != "morse1.txt" and morse_file != "morse2.txt" and morse_file != 'morse3.txt':
        morse_file = input('That is not a conversion file. What is the file in morse code you would like to convert?')
    return morse_file

# Purpose: runs characters from the morse code file through the dictionary and into a list, and then writes this translated message list to a new file
# Parameters: morse_file (string, the name of the file in morse code that will be converted), morse_dict (dictionary, the dictionary from morse code to english)
# Return: none
def convert_file(morse_file, morse_dict):
    # open file for reading
    morse_file_data = open(morse_file, 'r')
    # initialize list for the translation
    translation_list = []
    for line in morse_file_data:
        # split every line into single characters
        characters = line.split()
        for character in characters:
            # separates every character into a new line
            character = character + '\n'
            # translates character using dictionary
            translated_char = morse_dict[character]
            # adds translated character to translation_list
            translation_list.append(translated_char)
        # Inputs a space between each line/word
        translation_list.append(' ')
    # Join translation list into a string
    translation = ''.join(translation_list)
    # close the file
    morse_file_data.close()
    # asks user what file they would like to write the translation to
    converted_file = input('What would you like to name the new file with the converted morse code? Please exclude the suffix.').lower()
    # opens file for writing and writes translation
    converted_file_data = open(f'{converted_file}.txt', 'w')
    converted_file_data.write(translation)
    print('The file has been converted.')
    # closes file
    converted_file_data.close()

# Purpose: asks user if they would like to convert a file again
# Parameters: none
# Return: none
def get_convert_again():
    convert_again = input('Would you like to convert another file? For yes, type Y and for no, type N.').lower()
    # error checking to ensure user inputs yes or no
    while convert_again != 'y' and convert_again != 'n':
        convert_again = input('That was an invalid input. Would you like to convert another file? For yes, type Y and for no, type N.').lower()
    # repeats main function of user would like to convert again
    while convert_again == 'y':
        main()
    # allows user to exit the program
    if convert_again == 'n':
        print('Process completed. Thank you for using this program!')

# Purpose: main function
# Parameters: none
# Return: none
def main():
    # asks user which file they would like to use for the dictionary
    morse_dict_file = get_morse_dict_file()
    # reads file to a dictionary
    morse_dict = read_file_to_dict(morse_dict_file)
    # finds the file the user would like to translate
    morse_file = get_morse_file()
    # converts message in morse code to English and outputs to a new file
    convert_file(morse_file, morse_dict)
    # asks if user would like to convert again
    get_convert_again()

# call main function
main()
