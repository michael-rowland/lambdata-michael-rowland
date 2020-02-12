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

def train_val_test(df, val=False, split_proportion=0.8):
    '''
    returns tuple of split train and test DataFrame's
    includes val split if val=True

    Parameters
    ----------
    df : DataFrame
        Dataframe of all data to be split

    val : bool, optional (default=False)
        If true, further split train data into train/validate sets
    
    split_proportion : float, optional (default=0.8)
        Proportion of train, val, test split
    '''
    train, test = train_test_split(df, train_size=split_proportion)
    
    if val:
        train, val = train_test_split(train, train_size=split_proportion)
        return train, val, test
    
    return train, test