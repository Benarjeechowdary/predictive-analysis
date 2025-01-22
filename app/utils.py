import pandas as pd

def save_csv(file, path):
    file.save(path)

def preprocess_data(file_path):
    data = pd.read_csv(file_path)
    data=data.rename(columns={'Failure_Risk':'Downtime'})
    data = data.select_dtypes(include=[float, int])  
    data=data.dropna()
    
    return data
