from pandas import DataFrame
from pandas import Series
from pandas import NA


DF_WITH_MISSING_COLUMNS = DataFrame({
            'age': [25, 12, 15, 14, 19, 23, 25, 29],
            'al': [0, 1, 2, 2, 4, 5, 5, 4],
            'ba': ["notpresent", NA, "present", "notpresent", "present", NA, "present", "present"]
            }) 
        
nan_list = [NA for i in range(8)]
DF_WITH_ALL_COLUMNS = DataFrame({
            'age': [25, 12, 15, 14, 19, 23, 25, 29],
            'al': [0, 1, 2, 2, 4, 5, 5, 4],
            'ba': ["notpresent", NA, "present", "notpresent", "present", NA, "present", "present"],
            'bp': nan_list,
            'sg': nan_list,
            'su': nan_list,
            'rbc': nan_list,
            'pc': nan_list,
            'pcc': nan_list,
            'bgr': nan_list,
            'bu': nan_list,
            'sc': nan_list,
            'sod': nan_list,
            'pot': nan_list,
            'hemo': nan_list,
            'pcv': nan_list,
            'wbcc': nan_list,
            'rbcc': nan_list,
            'htn': nan_list,
            'dm': nan_list,
            'cad': nan_list,
            'appet': nan_list,
            'pe': nan_list,
            'ane': nan_list,
            'class': nan_list
            })

EMPTY_DF_WITH_WRONG_TYPES = DataFrame(columns=[
            'age', 'bp', 'sg', 'al', 'su', 'rbc', 'pc', 'pcc', 'ba', 'bgr',
            'bu', 'sc', 'sod', 'pot', 'hemo', 'pcv', 'wbcc', 'rbcc', 'htn', 'dm',
            'cad', 'appet', 'pe', 'ane', 'class'], 
            dtype=object) 

EMPTY_DF_WITH_CORRECT_TYPES = DataFrame({
            'age': Series(dtype='int'),
            'bp': Series(dtype='int'),
            'sg': Series(dtype='category'),
            'al': Series(dtype='category'),
            'su': Series(dtype='category'),
            'rbc':Series(dtype='category'),
            'pc': Series(dtype='category'),
            'pcc': Series(dtype='category'),
            'ba': Series(dtype='category'),
            'bgr': Series(dtype='int'),
            'bu': Series(dtype='float'),
            'sc': Series(dtype='float'),
            'sod': Series(dtype='float'),
            'pot': Series(dtype='float'),
            'hemo': Series(dtype='float'),
            'pcv': Series(dtype='int'),
            'wbcc': Series(dtype='int'),
            'rbcc': Series(dtype='float'),
            'htn': Series(dtype='category'),
            'dm': Series(dtype='category'),
            'cad': Series(dtype='category'),
            'appet': Series(dtype='category'),
            'pe': Series(dtype='category'),
            'ane': Series(dtype='category'),
            'class': Series(dtype='category')
            })

DF_WITH_MISSING_COLUMNS_AND_BAD_FORMAT = DataFrame({
            'age': [25, 12, 15],
            'al': [0, 1, 2],
            'ba': [b'notpresent', b'?', b'present']
            }) 
nan_list = [NA for i in range(3)]
DF_WITH_ALL_COLUMNS_AND_GOOD_FORMAT = DataFrame({
            'age': [25, 12, 15],
            'al': [0, 1, 2],
            'ba': ["notpresent", NA, "present"],
            'bp': nan_list,
            'sg': nan_list,
            'su': nan_list,
            'rbc': nan_list,
            'pc': nan_list,
            'pcc': nan_list,
            'bgr': nan_list,
            'bu': nan_list,
            'sc': nan_list,
            'sod': nan_list,
            'pot': nan_list,
            'hemo': nan_list,
            'pcv': nan_list,
            'wbcc': nan_list,
            'rbcc': nan_list,
            'htn': nan_list,
            'dm': nan_list,
            'cad': nan_list,
            'appet': nan_list,
            'pe': nan_list,
            'ane': nan_list,
            'class': nan_list
            })


DF_OUTPUT_FROM_ARFF_TEST_FILE = DataFrame({
            'age': [48, 7, 62],
            'bp': [80, 50, 80],
            'sg': [1.020, 1.020, 1.010],
            'al': [1, 4, 2],
            'su': [0, 0, 3],
            'rbc':  [NA, NA, "normal"],           
            'pc': ["normal", "normal", "normal"],
            'pcc': nan_list,
            'ba': nan_list,
            'bgr': nan_list,
            'bu': nan_list,
            'sc': nan_list,
            'sod': nan_list,
            'pot': nan_list,
            'hemo': nan_list,
            'pcv': nan_list,
            'wbcc': nan_list,
            'rbcc': nan_list,
            'htn': nan_list,
            'dm': nan_list,
            'cad': nan_list,
            'appet': nan_list,
            'pe': nan_list,
            'ane': nan_list,
            'class': nan_list
            })