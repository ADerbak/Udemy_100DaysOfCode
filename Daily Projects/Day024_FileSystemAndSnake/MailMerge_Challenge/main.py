# TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name
#Save the lterrsin the folder "ReadyToSend"

guests = []
with open('./Input/Names/invited_names.txt') as names:
    for line in names.readlines():
        guests.append(line.strip())

# print(guests)  # for testing to make sure list comes through

for name in guests:
    with open('./Input/Letters/starting_letter.txt') as letter:
        with open(f'./Output/ReadyToSend/{name}.txt', mode = 'w') as file:
                    file.write('')
        for line in letter.readlines():
            try: 
                if '[name]' in line:
                    line = line.replace('[name]',name)
            finally:
                with open(f'./Output/ReadyToSend/{name}.txt', mode = 'a') as file:
                    file.write(line)