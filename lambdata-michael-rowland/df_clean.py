import pandas as pd
from sklearn.model_selection import train_test_split

def check_null(df):
    '''
    function prints columns that contain null/NaN values
    '''
    for col in df.columns:
        null_count = df[col].isnull().values.sum()
        if null_count > 0:
            print(f"'{col}' contains {null_count} NaN's")

def train_val_test(df, val=True, split_proportion=0.8):
    '''
    returns tuple of split train, val, and test, DataFrame's
    '''
    train, test = train_test_split(df, train_size=split_proportion)
    train, val = train_test_split(train, train_size=split_proportion)
    
    return train, val, test