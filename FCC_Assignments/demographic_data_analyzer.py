import pandas as pd

def calculate_demographic_data():
    # Define column names as per the dataset (no headers in the file)
    columns = ['age', 'workclass', 'fnlwgt', 'education', 'education-num', 'marital-status', 'occupation', 'relationship', 'race', 'sex', 'capital-gain', 'capital-loss', 'hours-per-week', 'native-country', 'salary']
    
    # Load the dataset
    df = pd.read_csv(r'C:\Users\Admin\PROJECTS\AI_Projects\Data_Handling\Data\adult\adult.data.csv', header=None, names=columns)
    
    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    race_count = df['race'].value_counts()
    
    # What is the average age of men?
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)
    
    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelors = round((df['education'] == 'Bachelors').sum() / len(df) * 100, 1)
    
    # What percentage of people with advanced education make more than 50K?
    # What percentage of people without advanced education make more than 50K?
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100, 1)
    lower_education_rich = round((df[~higher_education & (df['salary'] == '>50K')].shape[0] / df[~higher_education].shape[0]) * 100, 1)
    
    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()
    
    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((num_min_workers['salary'] == '>50K').sum() / len(num_min_workers) * 100, 1)
    
    # What country has the highest percentage of people that earn >50K?
    country_count = df['native-country'].value_counts()
    country_rich_count = df[df['salary'] == '>50K']['native-country'].value_counts()
    highest_earning_country = (country_rich_count / country_count * 100).idxmax()
    highest_earning_country_percentage = round((country_rich_count / country_count * 100).max(), 1)
    
    # Identify the most popular occupation for those who earn >50K in India.
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()
    
    # DO NOT MODIFY BELOW THIS LINE
    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }