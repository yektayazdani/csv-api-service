import unittest
import os
from app.csv_reader import read_csv_file

class TestCsvReader(unittest.TestCase):
    
    def setUp(self):
        # Create a dummy CSV file for testing
        self.test_csv_path = "data/input2.csv" 
        with open(self.test_csv_path, 'w') as f:
            f.write("col1,col2\n")
            f.write("val1,val2\n")
            f.write("val3,val4\n")


    def tearDown(self):
        # Remove the dummy file after tests
        os.remove(self.test_csv_path)
        
    def test_read_csv_file(self):
        items = read_csv_file(self.test_csv_path)
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].data['col1'], 'val1')
        self.assertEqual(items[1].data['col2'], 'val4')
        
    def test_read_csv_file_not_found(self):
        #Change the file path temporarily so it raises file not found exception
        items = read_csv_file("non_existent_file.csv")
        self.assertEqual(len(items), 0)

if __name__ == '__main__':
    unittest.main()