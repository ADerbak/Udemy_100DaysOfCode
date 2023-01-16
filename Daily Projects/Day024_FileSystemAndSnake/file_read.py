## Old method
# file =  open("my_file.txt")
# contents = file.read()
# print(contents)
# file.close()
    
with open("new_file.txt", mode = 'w') as file:
    # w = write over
    # a = append
    file.write('\nNew Text')
