import pandas

df = pandas.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter:row.code for (index, row) in df.iterrows()}

def generate_phonetic():
        name = input("What is your name?: ").upper()

        try:
            letters = [nato_dict[letter] for letter in name]
        except KeyError:
            print("Sorry, only letters allowed")
            generate_phonetic()
        else:
            print(letters)
        

generate_phonetic()
