with open("./Input/Names/invited_names.txt", "r") as invited_names:
    name_list = invited_names.readlines()

with open("./Input/Letters/starting_letter.txt", "r") as letter:
    read_letter = letter.read()
    for name in name_list:
        name_integrated_mail = read_letter.replace("....", name.strip())
        mail = open(f"./Output/ReadyToSend/{name}_integrated.txt", "w")
        mail.write(name_integrated_mail)