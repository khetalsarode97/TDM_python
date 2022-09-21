import random
import pandas as pd
from faker import Faker


fake = Faker()

def state(no_rows,country):
    state = []
    data = pd.read_excel("static/assets/data_files/all_country_zip/country_data_new/" + str(country.upper()) + ".xlsx")
    state_data = data['STATE'].unique().tolist()
    for i in range(int(no_rows)):
        if len(state_data) > 1:
                state.append(random.choice(state_data))
        else:
            state.append(fake.state())
    return state

def city(no_rows,country):
    city = []
    data = pd.read_excel("static/assets/data_files/all_country_zip/country_data_new/" + str(country.upper()) + ".xlsx")
    print(data['CITY'])
    city_data = data['CITY'].unique().tolist()
    for i in range(int(no_rows)):
        city.append(random.choice(city_data))
        #city.append(city_data[i])
    return city



def zipcode(no_rows,country,state):
    zipcode = []
    data = pd.read_excel("static/assets/data_files/all_country_zip/country_data_new/" + country + ".xlsx",index_col = 0)
    zipcode_data = data['POSTAL_CODE'].unique().tolist()
    if len(zipcode_data) <= 0:
        zipcode.append(fake.zipcode())
    else:
        for i in range(int(no_rows)):
            zipcode.append(random.choice(zipcode_data))
    return zipcode