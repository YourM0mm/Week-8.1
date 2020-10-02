import os.path

def main():
    directory = input("Enter the directory to which you want to save your file : ")
    fileName = input("Enter the filename : ")
    name = input("Enter your name : ")
    address = input("Enter your address : ")
    phoneNumber = input("Enter your phone number : ")
    # Check if directory exists
    if os.path.isdir(directory):
        writeFile = open(os.path.join(directory,fileName), 'w')
        #write data separated by commas
        writeFile.write(name+','+address+','+phoneNumber+'\n')
        writeFile.close()
        print("File contents: ")
        #reading file for proof of storage
        readFile = open(os.path.join(directory,fileName), 'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry, the directory does not exist.")
main()
