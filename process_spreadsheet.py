import pandas as pd
from abstractions import ModuleInterface

class ProcessSpreadsheet(ModuleInterface):
    def __init__(self, input_spsheet_type = ""):
        self.input_spsheet_type = input_spsheet_type
        self.df = (pd.read_table(input_spsheet_type, sep = ','))
        self.df1 = (pd.read_table(input_spsheet_type, sep = '\t')) 
        

    def type_validation(self):
        if self.input_spsheet_type[-4:] in [ ".csv", ".tsv" , "xlsx"]:
            return self.input_spsheet_type
        
    def read_full_content(self):
        if self.input_spsheet_type[-4:] == ".csv":
            return self.df
        if self.input_spsheet_type[-4:] == ".tsv":
            return self.df1  

    def file_iteration(self):
        if self.input_spsheet_type[-4:] == ".csv":
            for ind,row in self.df.iteritems():
                ind,row
            return ind,row
        if self.input_spsheet_type[-4:] == ".tsv":
            for ind,row in self.df1.iteritems():
                ind,row
            return ind,row
        

    def read_first_two_lines(self):
        if self.input_spsheet_type[-4:] == ".csv": 
            return self.df.iloc[:2]
        if self.input_spsheet_type[-4:] == ".tsv": 
            return self.df1.iloc[:2]
        

    def read_last_two_lines(self):
        if self.input_spsheet_type[-4:] == ".csv":
            return self.df.iloc[-2:]
        if self.input_spsheet_type[-4:] == ".tsv":
            return self.df1.iloc[-2:]
        





if __name__ == '__main__':

    
    file_input = input("\nPlease input a file to read: ")
    while file_input[-4:] not in [ ".csv", ".tsv"]:
        print(f"This filetype: {file_input} is not a spreadsheet type, please input a valid one\n")
        file_input = input("\nPlease input a file to read: ")
    ProcessSpreadsheet = ProcessSpreadsheet(file_input)

    operations = input("Would you like to 'readall' or 'firsttwo' or 'lasttwo' : ").lower().strip()
    while operations not in ['readall','firsttwo','lasttwo' ]:
        print("\npls select the right option \n")    
        operations = input("Would you like to 'readall' or 'iterate' or 'firsttwo' or 'lasttwo' : ").lower().strip()

    if operations == 'readall':
        print(f"\n{ProcessSpreadsheet.read_full_content()}")
        print("\n-----------Thank-you-----------\n")

    if operations == 'firsttwo':
        print(ProcessSpreadsheet.read_first_two_lines())
        print("\n-----------Thank-you-----------\n")

    if operations == 'lasttwo':
        print(ProcessSpreadsheet.read_last_two_lines())
        print("\n-----------Thank-you-----------\n")

    # if operations == 'iterate':
    #     print(ProcessSpreadsheet.file_iteration())
    #     print("\n-----------Thank-you-----------\n")

