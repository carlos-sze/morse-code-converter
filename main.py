# TODO1: prepare morse table for letters and morse code values
# TODO2: accept input text
# TODO3: loop through each letter, return morse code for each letter
# TODO4: error handling

import pandas as pd

df = pd.read_csv('morse_mapping_table.csv', engine='python')

def morse_convert(text):
    end_morse_code = ""
    try:
      for char in text:
          end_morse_code += df[df['letter'] == char].morse_code.values
          end_morse_code += ' '
    except KeyError as error_message:
      print(f"Invalid character. The key {error_message} does not exist.")
      morse_convert(text)  # call function again after error
    else:
      print(f"Here's the translated Morse code: {end_morse_code}")


input_text = input("Type the text you want to translate as Morse code:\n").upper()
morse_convert(input_text)
