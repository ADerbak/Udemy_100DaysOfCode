import pandas

#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}


#TODO: turn this into a try/catch and loop until valid
ask = True
while(ask):
    
        name = input("What is your name?: ").upper()
        # if any(chr.isdigit() for chr in name):
        #     raise KeyError
        try:
            letters = [nato_dict[letter] for letter in name]
        except KeyError:
            print("Sorry, only letters allowed")
        else:
            ask = False
        

print(letters)
