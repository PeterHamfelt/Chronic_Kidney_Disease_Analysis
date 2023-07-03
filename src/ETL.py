
# dependencies import
from scipy.io import arff
from numpy import nan
from pandas import DataFrame
from os import remove
from os.path import split
from logging import warning

COLUMN_LIST = ['age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr',
                'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc', 'htn', 'dm',
                'cad', 'appet', 'pe', 'ane', 'class']

TYPE_DICT = {
    'category': ['sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'htn', 'dm', 'cad', 'appet', 'pe', 'ane', 'class'],
    'int': ['age', 'bp', 'bgr', 'pcv', 'wbcc'],
    'float':['bu', 'sc', 'sod', 'pot', 'hemo', 'rbcc']
}

def clean_format_arff(path: str) -> str:
    """
    This method cleans the .arff file and formats it to be loaded as a dataframe.
    :param path: the path to the original .arff file
    :return: the path to the new .arff file
    """

    # the original .arff file is loaded as a list of lines
    with open(path, "r") as original_file:
        lines = original_file.readlines()

    # the new .arff file is created and the cleaned lines are written
    new_file_path = "data/clean_" + split(path)[-1]
    with open(new_file_path, "w") as new_file:
        for line in lines:
            # the comments and the header are ignored in the cleaning process
            if line.startswith("@") or line.startswith("%"):
                new_file.write(line)

            # the cleaning process replaces tabs and spaces with commas and removes unnecessary commas
            else:
                new_line = line.replace("\t", "")
                new_line = new_line.replace(" ", "")
                new_line = new_line.replace(",,", ",")
                new_file.write(new_line)

    return new_file_path

def add_columns_if_not_exist(df : DataFrame) -> DataFrame:
    """
    This method adds a column to the dataframe from the determined chronic kidney disease dataset if it does not exist.
    :param df: the original dataframe
    :return: the dataframe with the added columns
    """
    for column in COLUMN_LIST:
        if column not in df.columns:
            df[column] = nan
            warning(f"The column {column} wasn't found in the dataset. It has been added with NaN values")

    return df

def cast_columns(df: DataFrame) -> DataFrame:
    """
    This method casts the dataframe columns to the correct data types.
    :param df: the original dataframe
    :return: the dataframe with the correct data types
    """

    for columns_type in TYPE_DICT.keys():

        if columns_type == 'category':
            df[TYPE_DICT['category']] = df[TYPE_DICT['category']].fillna(value=b'?', inplace=False)
            for column in TYPE_DICT['category']:
                df[column] = df[column].apply(lambda x:str(x)[2:-1])
            df[TYPE_DICT['category']] = df[TYPE_DICT['category']].astype('category')

        else:
            df[TYPE_DICT[columns_type]] = df[TYPE_DICT[columns_type]].astype(columns_type, errors='ignore')
    df.replace('<NA>', nan, inplace=True)
    return df

def format_dataframe(df: DataFrame) -> DataFrame:
    """
    This method formats the dataframe that was previously loaded from the chronic kidney disease dataset file/
    The columns are changed to the correct data types  whith the help of a type dictionnary and missing values are replaced with pandas.NA.
    
    :param df: the original dataframe
    :return: the formatted dataframe
    """
    df = add_columns_if_not_exist(df)
    df = cast_columns(df)
    df = df.replace('?', nan)
    return df

class ETL:
    def  load_data(self, file_path:str) -> DataFrame:
        """
        This method loads the chronic kidney disease dataset file and formats it to be loaded as a dataframe.
        :param file_path: the path to the original chronic kidney disease dataset file
        :return: the formatted dataframe
        """
        if not file_path.endswith(".arff"):
            raise ValueError("The file must be a .arff file")
            
        new_file_path = clean_format_arff(file_path)    # the original dataset file is cleaned and formatted in a readable arff file
        data = arff.loadarff(new_file_path)                 # the chronic kidney disease dataset file is loaded
        remove(new_file_path)                            # the temporary created dataset file is delete
        df = DataFrame(data[0])                          # the data is converted to a dataframe
        df = format_dataframe(df)                       # the dataframe is formatted in the correct data types
        return df