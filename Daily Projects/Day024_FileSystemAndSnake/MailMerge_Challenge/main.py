# TODO: Create a letter using starting_letter.txt
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name
#Save the lterrsin the folder "ReadyToSend"

guests = []

INVITEDGUESTS_FP = './Input/Names/invited_names.txt'
LETTER_FP = './Input/Letters/starting_letter.txt'

with open(INVITEDGUESTS_FP) as names:
    for line in names.readlines():
        guests.append(line.strip())

# print(guests)  # for testing to make sure list comes through

for name in guests:
    with open(LETTER_FP) as letter:
        
        # Clear out file if it already exists
        with open(f'./Output/ReadyToSend/{name}.txt', mode = 'w') as file:
                    file.write('') 
                    
        # For each line, append it on to the file.
        for line in letter.readlines():
            try: 
                #If [name] is in the file, replace it with the name
                if '[name]' in line:
                    line = line.replace('[name]',name)
            finally:
                with open(f'./Output/ReadyToSend/{name}.txt', mode = 'a') as file:
                    file.write(line)