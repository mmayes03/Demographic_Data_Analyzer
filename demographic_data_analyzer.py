import pandas as pd




main_df = pd.read_csv('csv_files/adult.data.csv', na_values= ["None", '?'])

main_df = main_df.fillna({'workclass': 'Unemployed',
                            'occupation': 'Unemployed', 
                                'native-country': 'Unknown'})
# white = df.loc[:, 'race'] == 'White'
# print(df.value_counts(white))
# race_counter = main_df['race'].value_counts()
# print(race_counter)
# print(main_df.isnull().sum())


def race_count(df):
    races = df['race'].drop_duplicates() #find each race
    # print(races)
    people_of_each_race = {}
    white = (df['race'] == 'White').sum()
    black = (df['race'] == 'Black').sum()
    Asian_Pac_Islander = (df['race'] == 'Asian-Pac-Islander').sum()
    Amer_Indian_Eskimo = (df['race'] == 'Amer-Indian-Eskimo').sum()
    Other = (df['race'] == 'Other').sum()
    people_of_each_race['White'] = white
    people_of_each_race['Black'] = black
    people_of_each_race['Asian-Pac-Islander'] = Asian_Pac_Islander
    people_of_each_race['Amer-Indian-Eskimo'] = Amer_Indian_Eskimo
    people_of_each_race['Other'] = Other
    
    print(people_of_each_race)

def average_age_men(df):
    men_age = df.loc[df['sex'] == 'Male', 'age'].mean()
    av_age = round(men_age)
    print(f"The average age of men is {av_age}")

def percentage_bachelors(df):
    education = df['education'].count()
    bachelors = df.loc[df['education'] == 'Bachelors', 'education'].count()
    percent = round(((bachelors/education)*100), 2)
    print(f"There is {percent}% of people with a Bachelors degree")

def higher_education_rich(df):
    Bachelors = df['education'] == 'Bachelors'
    Masters = df['education'] == 'Masters'
    Doctorate = df['education'] == 'Doctorate'
    salery = df['salary'] == '>50K'
    total_advance = df[(Bachelors)|(Masters)|(Doctorate)]['education'].count()
    advanced_ed = df[((Bachelors)|(Masters)|(Doctorate)) & (salery)]['salary'].count()
    advance_percent = round(((advanced_ed/total_advance)*100), 2)
    print(f"There is {advance_percent}% of people with an advance education making more than 50k.")

def lower_education_rich(df):
    
    Bachelors = df['education'] == 'Bachelors'
    Masters = df['education'] == 'Masters'
    Doctorate = df['education'] == 'Doctorate'
    salery = df['salary'] == '>50K'
    total_non_advance = df[~((Bachelors)|(Masters)|(Doctorate))]['education'].count()
    advanced_ed = df[~((Bachelors)|(Masters)|(Doctorate)) & (salery)]['salary'].count() #Use ~ for opposite 
    advance_percent = round(((advanced_ed/total_non_advance)*100), 2)
    print(f"There is {advance_percent}% of people without an advanve degree making more than 50k.")

def min_work_hours(df):
    min_hrs = df['hours-per-week'].min()
    print(f"The minimum number of hours worked is {min_hrs}")

def rich_percentage(df):
    min_hrs = df[df['hours-per-week'] == 1]['hours-per-week'].count()
    ppl_min_hrs_over_50k = df[(df['hours-per-week'] == 1) &(df['salary'] == '>50K')]['hours-per-week'].count()
    percent_min_over_50k = round((ppl_min_hrs_over_50k/min_hrs)*100, 1)
    print(f"The percent of people that work the minimum number of hours and make over 50k is {percent_min_over_50k}%")
def country_with_highest_50k_amongst_50k(df):
    country_50k = df[df['salary']== '>50K']['native-country'].value_counts()
    max_value = df[df['salary']== '>50K']['native-country'].value_counts().max()
    total_country_over_50k = df[df['salary']== '>50K']['native-country'].value_counts().sum()
    country_count = df['native-country'].value_counts()
    country_found = ''
    country_found_pop = 0
    for key, values in country_50k.items():
        if values == max_value:
            # print(f"The {key} has the highest percentage of people that earn >50K\n")
            country_found += key
    for key, pop in country_count.items():
        if key == country_found:
            country_found_pop += pop
    percentage_50k= round((max_value/total_country_over_50k)*100, 2)
    percentage_country_base = round((max_value/country_found_pop)*100, 2)
    print(f"The percentage of people in {country_found} compared to other \n countries with people who make over 50k is: {percentage_50k}%\n")
    print(f"The percent of people in {country_found} that make >50k is {percentage_country_base}%")

def highest_earning_country_percentage(df):
    country_50k = df[df['salary']== '>50K']['native-country'].value_counts()
    country_count = df['native-country'].value_counts()
    country_50k_percent_df = round((country_50k/country_count)*100, 2)
    country_50k_percent_highest = round((country_50k/country_count)*100, 2).idxmax() #returns index
    percent_of_50k_highest = country_50k_percent_df[country_50k_percent_highest]
    print(f"{country_50k_percent_highest} is the country with the highest percent of >50k earners amounting to {percent_of_50k_highest}%")
def top_IN_occupation(df):
    indian_total_over_50k = df[(df['native-country']== 'India')&(df['salary']== '>50K')]['native-country'].count()
    indian_pop_ocupations = df[(df['native-country']== 'India')&(df['salary']== '>50K')]['occupation'].value_counts()
    indian_max_pop_ocupations = df[(df['native-country']== 'India')&(df['salary']== '>50K')]['occupation'].value_counts().max()
    for key, value in indian_pop_ocupations.items():
        if value == indian_max_pop_ocupations:
            print(f"The the most popular occupation for those who earn >50K in India is '{key}'jobs.")


# return {
#         'race_count': race_count,
#         'average_age_men': average_age_men,
#         'percentage_bachelors': percentage_bachelors,
#         'higher_education_rich': higher_education_rich,
#         'lower_education_rich': lower_education_rich,
#         'min_work_hours': min_work_hours,
#         'rich_percentage': rich_percentage,
#         'highest_earning_country': highest_earning_country,
#         'highest_earning_country_percentage':highest_earning_country_percentage,
#         'top_IN_occupation': top_IN_occupation
#     }


# race_count(main_df)
# average_age_men(main_df)
# percentage_bachelors(main_df)
# higher_education_rich(main_df)
# lower_education_rich(main_df)
# min_work_hours(main_df)
# rich_percentage(main_df)
# country_with_highest_50k_amongst_50k(main_df)
# highest_earning_country_percentage(main_df)
# top_IN_occupation(main_df)