PLACEHOLDER = "[Name]"

with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()    # returns all the lines in the file as a list item

with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()  # remove spaces at the beginning and the end
        new_letter = letter_contents.replace(PLACEHOLDER, stripped_name)  # replaces a specified phrase with another specified phrase
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)



