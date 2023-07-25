import pandas as pd

class Numerical:
    def converted(self, column, value):
        df_train = pd.read_csv('numerical_data.csv')
        cat_data = pd.read_csv(r'Dataset\loan_train.csv')
        
        # Check if the value exists in the column of the DataFrame
        if value in cat_data[column].values:
            num = df_train.loc[cat_data[cat_data[column] == value].index[0]][column]
            return num
        else:
            print(f"Value '{value}' not found in the '{column}' column.")
            return None



