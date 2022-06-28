import pandas as pd

def open_file(file):
    with open(file) as f:
        terms = f.read().splitlines()
    return terms

file = 'https://raw.githubusercontent.com/Swashbuckler1/be_the_dell-ta/master/Dell_Interns_Directory.csv'
dell_interns_directory = pd.read_csv(file)

universities = dell_interns_directory['University'].unique()
degrees = dell_interns_directory['Degree'].unique()
years = dell_interns_directory['Year'].unique()
business_units = dell_interns_directory['BusinessUnit'].unique()
campus_locations = dell_interns_directory['CampusLocation'].unique()
majors = dell_interns_directory['Major'].unique()