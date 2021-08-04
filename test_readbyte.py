from readbyte import ReadBytesFromFile as file
import unittest

class TestReadBytes(unittest.TestCase):

    def test_type_validation(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.type_validation()
        self.assertIsInstance(result, str)      
        self.assertEqual(any(result), True)
        self.assertIsNotNone(result)

    def test_file_manipulation(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.file_manipulation()
        self.assertIsInstance(result, str)     #str to list
        self.assertIsNotNone(result)
        self.assertEqual(any(result), True) 

    def test_file_iteration(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.file_iteration()
        self.assertIsNotNone(result)
        self.assertIsInstance(result, list)
        self.assertEqual(bool(result), True) 

    def test_read_first_two_lines(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.read_first_two_lines()
        self.assertIsInstance(result, str)
        self.assertEqual(bool(result), True) 
        self.assertIsNotNone(result)
            

    def test_read_last_two_lines(self): 
        dummy = 'newlife.csv'  
        work = file(dummy)
        result = work.read_last_two_lines()
        self.assertIsInstance(result, str)
        self.assertIsNotNone(result)
        self.assertEqual(bool(result), True) 

if __name__ == '__main__':
    unittest.main()






































 # import sys
# from read_bytes_fromfile import *

# def re_run():
#     print('Would you like to work on Files or Spreadsheet')
#     option_selected = sys.stdin.readline()
#     if option_selected.lower() == "files":
#         print('please input correct filename and filetype: ')
#         filename_and_type = sys.stdin.readline()
#         new1 = GetFilenameAndType()
#         new1.input_filename_and_type(filename_and_type)


#     elif option_selected.lower() == "spreadsheet":
#         pass
#     else:
#         re_run()


    

    
    