# dependencies import


from src.ETL import cast_columns 
from src.ETL import clean_format_arff
from src.ETL import add_columns_if_not_exist
from src.ETL import format_dataframe
from src import ETL_tool


import unittest
import os
from data.test import test_vars



class test_ETL(unittest.TestCase):
    def test_ETL_clean_format_arff(self):
        """
        Test clean_format_arff function. We check if the cleaned up file is the same as expected
        """

        input_file ="data/test/test_format_file_input.arff"
        expected_output_file = "data/test/test_format_file_output.arff"

        with open(expected_output_file, 'r') as f:
            expected_output = f.readlines()

 
        output_file = clean_format_arff(input_file)


        with open("data/clean_test_format_file_input.arff","r") as f:
            output = f.readlines()
        os.remove(output_file)

        self.assertEqual(output_file, "data/clean_test_format_file_input.arff")
        self.assertEqual(output, expected_output)

    def test_ETL_add_columns_if_not_exist(self):
        """
        Test add_columns_if_not_exist function. We check if the function adds the missing columns to the dataframe.
        
        """

        # we create a dataframe with missing columns
        input = test_vars.DF_WITH_MISSING_COLUMNS 
    
        # we create a dataframe with all the columns
        expected_output = test_vars.DF_WITH_ALL_COLUMNS
        output = add_columns_if_not_exist(input)

        # we check that the output has the same columns as the expected output
        self.assertEqual(output.columns.tolist(), expected_output.columns.tolist())
        # we check that the output has the same number of NaN values as the expected output
        self.assertEqual(output.isna().sum().sum(), expected_output.isna().sum().sum())


    def test_ETL_cast_columns(self):
        """
        Test cast_columns function. We check if the columns type are casted correctly
        """

        input = test_vars.EMPTY_DF_WITH_WRONG_TYPES
        
        expected_output = test_vars.EMPTY_DF_WITH_CORRECT_TYPES
        
        output = cast_columns(input)

        self.assertEqual(output.dtypes.tolist(), expected_output.dtypes.tolist())


    def test_ETL_format_dataframe(self):
        """
        Test format_dataframe function. We check if the output dataframe is of the same kind as the expected dataframe
        """
        input = test_vars.DF_WITH_MISSING_COLUMNS_AND_BAD_FORMAT

        expected_output = test_vars.DF_WITH_ALL_COLUMNS_AND_GOOD_FORMAT
        
        output = format_dataframe(input)

        # we check that the output has the same columns as the expected output
        self.assertEqual(output.columns.tolist(), expected_output.columns.tolist())
        # we check that the output has the same number of NaN values as the expected output
        self.assertEqual(output.isna().sum().sum(), expected_output.isna().sum().sum())


    def test_ETL_load_data_bad_input(self):
        """
        test load_data function. We check if the function raises an error if the input path is not a file.
        """
        input_path = "data/test/test_vars.py"
        
        with self.assertRaises(ValueError):
            ETL_tool.load_data(input_path)


    def test_ETL_load_data_good_input(self):
        """
        test load_data function. We check if the output dataframe is of the same kind as the expected dataframe
        """

        input_path = "data/test/test_format_file_input.arff"
        expected_output = test_vars.DF_OUTPUT_FROM_ARFF_TEST_FILE
        output = ETL_tool.load_data(input_path)

        # we check that the output has the same columns as the expected output
        self.assertEqual(output.columns.tolist(), expected_output.columns.tolist())
        # we check that the output has the same number of NaN values as the expected output
        self.assertEqual(output.isna().sum().sum(), expected_output.isna().sum().sum())


if __name__ == '__main__':
    unittest.main()

