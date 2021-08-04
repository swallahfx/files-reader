from abstractions import ModuleInterfaceB



class ReadBytesFromFile(ModuleInterfaceB):
    def __init__(self, input_file_type = ""):
        self.input_file_type = input_file_type


    def type_validation(self): 
        if self.input_file_type[-4:]  in [".txt", ".csv", ".tsv" ]:
            return self.input_file_type

        
    def file_manipulation(self):
        try:
            with open(self.type_validation(), 'r') as read_obj:
                newrow = read_obj.read()
            return newrow
        except FileNotFoundError:
            print("wrong file input")
            exit()


    def file_iteration(self):
        newfile = ""
        for line in self.file_manipulation():
            newfile +=line
        return newfile.split("\n")


    def read_first_two_lines(self):
        row_one = self.file_iteration()[0]
        row_two = self.file_iteration()[1]
        return (f"\n{row_one}\n{row_two}\n" )


    def read_last_two_lines(self):
        row_one = self.file_iteration()[-2]
        row_two = self.file_iteration()[-1]
        return (f"\n{row_one}\n{row_two}\n")

        






if __name__ == "__main__":   
      
        
    file_input = input("\nPlease input a file to read: ")
    while file_input[-4:] not in [".txt", ".csv", ".tsv" ]:
        print(f"pls select the right file, this file-type: {file_input} does not allow readByte ")
        file_input = input("\nPlease input a file type to read: ")
    ReadBytesFromFile = ReadBytesFromFile(file_input)

    operations = input("Would you like to 'readall' or 'firsttwo' or 'lasttwo' : ").lower().strip()
    while operations not in ['readall','firsttwo','lasttwo' ]:
        print("\npls select the right option \n")    
        operations = input("Would you like to 'readall' or 'iterate' or 'firsttwo' or 'lasttwo' : ").lower().strip()

    if operations == 'readall':
        print(f"\n{ReadBytesFromFile.file_manipulation()}")
        print("\n-----------Thank-you-----------\n")

    if operations == 'firsttwo':
        print(ReadBytesFromFile.read_first_two_lines())
        print("\n-----------Thank-you-----------\n")

    if operations == 'lasttwo':
            print(ReadBytesFromFile.read_last_two_lines())
            print("\n-----------Thank-you-----------\n")

