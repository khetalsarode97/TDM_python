import random
from faker import Faker

fake = Faker()


def Address(no_rows):
    Address_data = []
    for i in range(int(no_rows)):
        address = fake.address()
        address = address.replace('\n', ',')
        Address_data.append(address)
    #print(Address_data)
    return Address_data

# def Phone_number(no_rows):
#     phone_number = []
#     for i in range(int(no_rows)):
#         phone = fake.phone_number()
#         phone_number.append(phone)
#     return phone_number

def Phone_number(no_rows):
    phone_number = []
    ph_no = []
    data = []
    for i in range(int(no_rows)):
        ph_no = []
        ph_no.append(random.randint(6, 9))
        for i in range(1, 10):
            ph_no.append(random.randint(0, 9))
        phone_number_data = "".join(map(str, ph_no))
        phone_number.append(phone_number_data)
    return phone_number

def Aadhar(no_rows):
    aadhar_data = []
    fake = Faker('en_IN')
    for i in range(int(no_rows)):
        aadhar_data.append(fake.aadhaar_id())
    #print(aadhar_data)
    return aadhar_data


# def Name(no_rows, type, prefix, suffix, min, max, fixed):
#     Name = []
#     for i in range(no_rows):
#         if type == 'prefixName':
#             name = fake.first_name()
#             Name.append(prefix + name)
#         elif type == 'suffixName':
#             name = fake.first_name()
#             Name.append(name + suffix)
#         elif type == 'presuffName':
#             name = fake.first_name()
#             Name.append(prefix + name + suffix)
#         elif type == 'fullName':
#             name = fake.name()
#             Name.append(name)
#         elif type == 'fName':
#             name = fake.first_name()
#             Name.append(name)
#         elif type == 'lName':
#             name = fake.last_name()
#             Name.append(name)
#     return Name

# def state(no_rows):
#     state = []
#     for i in range(no_rows):
#         state.append(fake.state())
#     return state

def country(no_rows,type):
    country = []
    for i in range(int(no_rows)):
        country.append(fake.country())
        # if type == "type1":
        #     country.append(fake.country())
        # else:
        #     country.append(fake.current_country())
    return country

