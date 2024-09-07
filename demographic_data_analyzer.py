import pandas as pd
from sympy import series


def calculate_demographic_data(print_data=True):
    # Read data from file
    fileN = 'adult.data.csv'
    df = pd.read_csv(fileN)
    #print(df.columns)

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    r_c = []
    for item in df.race:
        if item not in r_c:
            r_c.append(item)
    race_count = pd.Series(index = r_c)
    for index in race_count.index:
        race_count[index] = len(df[df['race'] == index ])

    # What is the average age of men?
    men = []
    for index, row in df.iterrows():
       if row['sex'] == 'Male':
            men.append(row['age'])
    average_age_men = round(pd.Series(men).mean(), 1)

    # What is the percentage of people who have a Bachelor's degree?
    b_c = 0
    for index,row in df.iterrows():
        if row['education'] == 'Bachelors':
            b_c += 1
    percentage_bachelors = round(b_c / max(df.index) * 100, 1)

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    high_ed_50 = 0 #number of people with a bachelors, masters, or doctorate that make more than 50k a year.
    high_ed = 0 #number of people with a bachelors, masters, or doctorate
    low_ed_50 = 0 #number of people without a bach, masters, or doctorate that make more than 50k a year.
    low_ed = 0
    for index,row in df.iterrows():
        if (row['education'] == 'Bachelors' or row['education'] == 'Masters' or row['education'] == 'Doctorate') and (row['salary'] == '>50K'):
            high_ed_50 += 1
        if (row['education'] == 'Bachelors' or row['education'] == 'Masters' or row['education'] == 'Doctorate'):
            high_ed += 1
        if (row['education'] != 'Bachelors' and row['education'] != 'Masters' and row['education'] != 'Doctorate') and (row['salary'] == '>50K'):
            low_ed_50 += 1
        if (row['education'] != 'Bachelors' and row['education'] != 'Masters' and row['education'] != 'Doctorate'):
            low_ed += 1

    higher_education =  round(high_ed / max(df.index) * 100, 1)


    # What percentage of people without advanced education make more than 50K?
    lower_education = round( low_ed / max(df.index)* 100, 1)

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    # percentage with salary >50K
    higher_education_rich = round(high_ed_50 / high_ed * 100, 1)
    lower_education_rich = round(low_ed_50 / low_ed * 100, 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = min(df['hours-per-week'])

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = 0
    minH_salary = 0

    for index,row in df.iterrows():
        if row['salary'] == '>50K' and row['hours-per-week'] == min_work_hours:
            minH_salary += 1
        if row['hours-per-week'] == min_work_hours:
            num_min_workers += 1

    rich_percentage = round(num_min_workers/minH_salary, 1)

    # What country has the highest percentage of people that earn >50K?
    country_pop = {}
    country_pop50plus = {}
    num_of_50plus = 0

    for index, row in df.iterrows():
        country_pop[row['native-country']] = 0
        country_pop50plus[row['native-country']] = 0
    for index, row in df.iterrows():
        country_pop[row['native-country']] += 1
        if row['salary'] == '>50K':
            country_pop50plus[row['native-country']] += 1
    country_50plus_percentage = {}
    for key, value in country_pop.items():
        country_50plus_percentage[key] = round( country_pop50plus[key] / country_pop[key] * 100 ,1 )

    h_e_c = max(country_50plus_percentage.items(), key = lambda x:x[1])
    highest_earning_country_percentage = h_e_c[1]
    highest_earning_country = h_e_c[0]

    # Identify the most popular occupation for those who earn >50K in India.
    pop_job_india = {}
    for index, row in df.iterrows():
        if row['native-country'] == 'India':
            pop_job_india[row['occupation']] = 0
    for index, row in df.iterrows():
        if row['native-country'] == 'India' and row['salary'] == '>50K':
            pop_job_india[row['occupation']] += 1

    t_I_c = max(pop_job_india.items(), key = lambda x:x[1])
    top_IN_occupation = t_I_c[0]





    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count)
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }

calculate_demographic_data()
