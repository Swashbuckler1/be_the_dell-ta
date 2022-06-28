import pandas as pd

def open_file(file):
    with open(file) as f:
        terms = f.read().splitlines()
    return terms

file = 'https://raw.githubusercontent.com/Swashbuckler1/be_the_dell-ta/master/Dell_Interns_Directory.csv'
df = pd.read_csv(file)
print(df['TechnologiesOfInterest'].values[1])