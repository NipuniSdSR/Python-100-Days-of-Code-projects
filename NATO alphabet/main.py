import pandas

nato_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
nato_alphaet_dict = {row.letter: row.code for (index, row) in nato_data_frame.iterrows()}
print(nato_alphaet_dict)

# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_word = input("Enter the word: ").upper()

nato_list = [nato_alphaet_dict[letter] for letter in user_word]
print(nato_list)