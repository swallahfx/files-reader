from typing import Any
from pandas.core.base import PandasObject
from process_spreadsheet import ProcessSpreadsheet as file
import unittest

class TestProcessSpreadSheet(unittest.TestCase):

    def test_type_validation(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.type_validation()
        self.assertIsInstance(result, str)      
        self.assertEqual(bool(result), True)
        self.assertIsNotNone(result)

    def test_read_full_content(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.read_full_content()
        self.assertIsInstance(result, PandasObject)
        self.assertIsNotNone(result)
        self.assertEqual(any(result), True) 

    def test_file_iteration(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.file_iteration()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, tuple)
        self.assertEqual(bool(result), True) 

    def test_read_first_two_lines(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.read_first_two_lines()
        self.assertIsInstance(result, PandasObject)
        self.assertEqual(any(result), True) 
        self.assertIsNotNone(result)
            
    def test_read_last_two_lines(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.read_last_two_lines()
        self.assertIsInstance(result, PandasObject)
        self.assertIsNotNone(result)
        self.assertEqual(any(result), True) 

if __name__ == '__main__':
    unittest.main()



































# import pandas as pd
# import sys

# from pandas.core.algorithms import unique


# class UniqueXter:
#     def __init__(self):
#         self.df = pd.read_csv(self.input_filename_and_type) 
        
#     def read_file_all(self):
#         return self.df.head()
        
#     def read_first2lines(self):
#         self.df.iloc[:2]

#     def read_last2lines(self):
#         self.df.iloc[-2:]

#     def iterate_through(self):
#         for ind,row in self.df.iterrows():
#             return ind,row

# class GetFilenameAndType(UniqueXter):
    
#     def input_filename_and_type(self,filename_and_type):
#         # print('please input correct filename and filetype: ')
#         # filename_and_type = sys.stdin.readline()
#         if (filename_and_type[-4:] == ".tsv"):
#             csv_table =pd.read_table(filename_and_type, sep='\t')
#             csv_table.to_csv('new_csv.csv', index=False)
#             return csv_table

#         elif filename_and_type[-4:] == ".txt":
#             result = ''
#             with open(filename_and_type) as f:
#                 result = '\n'.join(f.readlines())
#             with open('new_csv.csv') as f:
#                 for line in result.split('\n'):
#                     line = line.replace(' ', ',')
#                     f.write(line + '\n')
#                 return f

#         else:
#             return filename_and_type

# class ProcessSpreadSheet(UniqueXter):

#     def spreadsheet_to_csv(self):
#         df = pd.read_excel("./data.xlsx")
#         df.to_csv("./data.csv", sep=",")

#         return df

# # # try:
# # #     with open('new_file.csv', 'r') as reader:
# # #         fp = reader.readline()
# # #         print(fp)                  #read returns string while readline(s) returns list
# # #         fp = reader.readline()
# # #         print(fp)
# # #         fp = reader.readlines()
# # #         print(fp)
# # # except FileNotFoundError as err:
# # #     print("dude use a correct file")
# # #     raise err

# # # try:
# # #     with open('new_file.tsv', 'w+') as writer:
# # #         fp = writer.write('They said tsv is differentiated from csv by tab, kinwalode ti stress wa po\n ')   
# # #         print(writer.tell()) #returns only len of str
# # #         fp = writer.readline()   #reads the file now
# # #         writer.seek(0,2)
# # #         print(writer.tell())
# # #         print(fp)
# # #         fp= writer.read()
# # #         print(fp)
# # #         with open('new_file.tsv', 'a+') as writerr:
# # #             fp = writerr.write('jkkjekjkvejkjkjks,fdfdfdfgrertthrtrtyh, ertgrtthtrergrttmyjrfermyks')
# # #             print(writerr.read())
# # #             for i in writerr:
# # #                 print(i.strip())
# # # except FileNotFoundError as err:
# # #     print("dude use a correct file")
# # #     raise err
# # from os.path import getsize
# # with open("file_ine.mp3", "w+") as writer:
# #     for i in range (getsize('file_ine.mp3')):
# #         writer.seek(i)
# #         print("Byte",i,":" ,writer.read(1))


# # # import pandas

# # # with open('new_file.csv', mode='w+') as file_read:
# # #     df = file_read.write('You are welcome to my first csv file, I want to bursy your head off\n')


# # # df = pandas.read_csv('new_file.csv')
# # # with open('new_file.csv', mode='a+') as file_read:
# # #     file_read.write('They say i am just starting, they never knew the jungle i was coming from\n')
# # #     print(df)


