# Algorithm Document

---------------
* Purpose: asks the user which file to convert to a dictionary
* Name: get_morse_dict_file
* Parameters: none
* Return: morse_dict_file, string, name of file that will be converted to a dictionary
* Algorithm:
1. set morse_dict_file equal to user input with the message, "Welcome! This program converts files from morse code and outputs a new file with the translation in English. \n Which file would you like to use as the key or dictionary"
2. while morse_dict_file is not morsecode.txt
   1. output a message asking the user to try again, and set input equal to morse_dict_file
3. return morse_dict_file

-------------

* Purpose: reads the file to a dictionary
* Name: read_file_to_dict
* Parameters: morse_dict_file, string, the name of the file that will be read into a dictionary 
* Return: morse_dict, dictionary, dictionary that converts morse code to English
* Algorithm:
1. initialize empty dictionary morse_dict
2. try
   1. open morse_dict_file for reading
      1. for each line
         1. split line into items separated by a tab of space
         2. set key equal to items index 1
         3. set value equal to items index 0
         4. set morse_dict index key equal to value
   2. Close morse_dict_file
   3. return morse_dict
3. Except if there is a filenotfounderror
   1. output "File not found"
-------------

* Purpose: asks the user which file to convert
* Name: get_morse_file
* Parameters: none
* Return: morse_file, string, name of the file that the user would like converted to English
* Algorithm:
1. set morse_file equal to user input with the message "What is the file in morse code you would like to convert?"
2. While morse_file is not morse1.txt, morse2.txt or morse3.txt
   1. set morse_file equal to user input with the message "That is not a conversion file. What is the file in morse code you would like to convert?"
3. return morse_file

-------------

* Purpose: runs characters from the morse code file through the dictionary and into a list, and then writes this translated message list to a new file
* Name: convert_file
* Parameters: morse_file (string, the name of the file in morse code that will be converted), morse_dict (dictionary, the dictionary from morse code to english)
* Return: none
* Algorithm:
1. open morse_file for reading
2. initialize empty list translation_list
3. for each line in morse_file
   1. split the line into individual characters
      1. for each character
         1. write each character on a new line
         2. set translated_char equal to the character put through morse_dict
         3. add translated_char to the end of translation_list
      2. add a space in between each line or word
   2. Join the translation_list into one string
   3. close morse_file
   4. set converted_file equal to user input with the message "What would you like to name the new file with the converted morse code? Please exclude the suffix." and make it lowercase 
   5. open converted_file for writing
   6. write the translation string to the file
   7. output to the user "the file has been converted"
   8. close converted_file

-------------

* Purpose: asks user if they would like to convert a file again
* Name: get_convert_again
* Parameters: none
* Return: none
* Algorithm:
1. set convert_again equal to user input with the message 'Would you like to convert another file? For yes, type Y and for no, type N.' and make it lowercase
2. while convert_again is not y or n
   1. set convert_again equal to user input with the message 'That was an invalid input. Would you like to convert another file? For yes, type Y and for no, type N.'
3. While convert_again equals y
   1. call the main function
4. While convert_again equals n
   1. output to the user, 'Process completed. Thank you for using this program!'

-------------

* Purpose: main function
* Name: main
* Parameters: none
* Return: none
* Algorithm:
1. call get_morse_dict_file and set it equal to morse_dict_file
2. call read_file_to_dict with the parameter morse_dict_file and set it equal to morse_dict
3. call get_morse_file and set it equal to morse_file
4. call convert_file with the parameters morse_file and morse_dict
5. call get_convert_again

-------------

1. call main function

