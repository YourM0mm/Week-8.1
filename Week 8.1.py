import os.path

def main():
    directory = input("Enter the directory where you want to save your file : ")
    fileName = input("Enter the files name : ")
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

# I initially went with https://www.chegg.com/homework-help/questions-and-answers/python-create-program-performs-file-processing-activities-program-week-use-os-library-orde-q41710269
# I had another code I was working on my own but just wasn't getting anywhere.
