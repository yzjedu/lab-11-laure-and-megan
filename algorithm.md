# Algorithm Document

1. Input a file name
2. Make an empty dictionary and name it 'morse_dict'
3. Open the file for reading
4. loop through each line in the file
    1. Split the line by two spaces (' ') to extract the key and value
    2. Assign the first part as the value and the second part as the key in morse_dict
   3. close the file 
5. define get_morse_file function
6. return to morse_dict
7. prompt the user to input the name of a Morse code file they want to convert
8. return the provided file name as morse_file
9. Convert morse code to text:
10. Input: morse_file (name of the file with Morse code) and morse_dict (dictionary of Morse code mappings).
11. Open the file for reading.
12. Initialize an empty list decoded_message to hold the translated text.
    1. split the line into Morse code words by single spaces.
    2. Translate each Morse code word into its corresponding character using morse_dict:
    3. Replace unknown Morse code characters with '?'.
    4. Join the characters into a decoded word and add it to decoded_message.
    5. Join all the decoded words into a single string separated by spaces.
13. Return to decoded text
14. Load dictionary from morsecode text
15. Get the name of the file to be converted
16. Print the decoded message
17. Error check 
    1. If the file connot be found , display error message
    2. For any other error display general error message
