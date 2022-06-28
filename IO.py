import pandas as pd

def read_file(sheet_url):
    url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
    df = pd.read_csv(url)
    return df

def open_file(file):
    with open(file) as f:
        terms = f.read().splitlines()
    return terms

# url = 'https://docs.google.com/spreadsheets/d/1GxATEQYgmFyvCQbt3ZXQretIFU8an36aeGxx2PFwoZU/edit#gid=0'
# df = read_file(url)
# print(df.head())