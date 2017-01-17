import pandas as pd


def replace_column_values(df, dict, col_name, new_col_name=None):
    df_return = df
    if new_col_name is None:
        df_return[col_name].replace(dict, inplace=True)
    else:
        df_return[new_col_name] = df_return[col_name].replace(dict, inplace=False)

    return df_return

if __name__ == "__main__":

    df = pd.DataFrame({'letters':['a','a','c'],
                       'numbers':[1,2,3]})
    dict = {'a':1}
    print("Example of replacing values:")
    df_return = replace_column_values(df, dict, 'letters:')
    print(df_return)                                                                                                                                                                                                                                                                                                          

    print("Example of replacing values in a new column")
    df_return = replace_column_values(df, dict, 'letters', 'new_column')
    print(df_return)




