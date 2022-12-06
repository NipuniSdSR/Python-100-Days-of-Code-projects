#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
'''
/Users/nipuni/Desktop/100 days of Pyhton /day 24/Mail Merge Project Start/Input
/Users/nipuni/Desktop/100 days of Pyhton /day 24/Mail Merge Project Start
/Users/nipuni/Desktop/100 days of Pyhton /day 24/Mail Merge Project Start/Input/Letters
'''
with open("./Input/Names/invited_names.txt") as name_file:
    # names = name_file.read().split("\n") : 1 method
    names = name_file.readlines()
    print(names)

with open("./Input/Letters/starting_letter.txt") as starting_letter:
    start_letter = starting_letter.read()
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
    for name in names:
        # Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
        name = name.strip()  # remove the new line
        final_letter = start_letter.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}_letter.txt", mode='w') as letter:
            letter.write(final_letter)

