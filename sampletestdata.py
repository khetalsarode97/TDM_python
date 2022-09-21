from itertools import product
from faker import Faker
import random

fake = Faker()

def id_generate(no_rows, prefix, suffix, fixedlength, format,dataType):
    id_data = []
    randomlength = 0
    randomlength = int(fixedlength) - len(prefix) - len(suffix)
    randomlength = int(randomlength)
    print(randomlength)
    print(dataType)
    try:
        if dataType == "RandomInteger" or format == 'SequentialInteger':
            number_range = []
            num_zero = []
            number_range.append(list(range(1, 1111111, 1)))
            for i in range(int(no_rows)):
                id_num = 0
                id_num = len(str(number_range[0][i]))
                num_zero = []
                print(randomlength - id_num)
                for j in range(randomlength - id_num):
                    num_zero.append('1')
                id_data.append(prefix + str("".join(num_zero)) + str(number_range[0][i]) + suffix)
        elif dataType == "RandomString" or format == 'SequentialString':
            if randomlength >= 5:
                data = ''
                char_first = []
                data = list(product("ABCDEFGHJKLMNOPQRSTUVWXYZ", repeat=5))
                for i in range(int(no_rows)):
                    sequential_data_len = 0
                    char_first = []
                    sequential_data_len = len("".join(data[i]))
                    for j in range(randomlength - sequential_data_len):
                        char_first.append('A')
                    id_data.append(prefix + str("".join(char_first)) + str("".join(data[i])) + suffix)    
            else: 
                data = list(product("ABCDEFGHJKLMNOPQRSTUVWXYZ", repeat=randomlength))
                for i in range(int(no_rows)):
                     id_data.append(prefix + "".join(data[i]) + suffix)
        print(id_data)
        return id_data
    except:
        return "Exception Occured"

# def name(no_rows, prefix, suffix, fixedlength, format,datatype):
#     name_data = []
#     data_count = 0
#     randomlength = int(fixedlength) - len(prefix) - len(suffix)
#     print(datatype)
#     if datatype == "RandomString":
#         while True:
#             if format == "LastName":
#                 name = fake.last_name()
#             elif format == "FullName":
#                 name = fake.name()
#             elif format == "" or format == "FirstName":
#                 name = fake.first_name()
#
#             if len(name) == int(randomlength):
#                 name_data.append(prefix + name + suffix)
#                 data_count += 1
#             if data_count == int(no_rows):
#                 break
#     elif datatype == "RandomInteger":
#         name = list(product("0123456789", repeat=int(randomlength)))
#         for i in range(int(no_rows)):
#             name_data.append(prefix + "".join(name[i]) + suffix)
#         print(name_data)
#
#     #print(name_data)
#     return name_data

def name(no_rows, prefix, suffix, fixedlength, format,datatype):
    name_data = []
    char_data = []
    int_data = []
    data_count = 0
    randomlength = int(fixedlength) - len(prefix) - len(suffix)
    randomlength = int(randomlength)
    if datatype == "RandomString":
        if int(randomlength) > 2:
            while True:
                if format == "LastName":
                    name = fake.last_name()
                elif format == "FullName":
                    name = fake.name()
                elif format == "" or format == "FirstName":
                    name = fake.first_name()
                if len(name) == int(randomlength):
                    name_data.append(prefix + name + suffix)
                    data_count += 1
                if data_count == int(no_rows):
                    break
        else:
            name = list(product("ABCDEFGHJKLMNOPQRSTUVWXYZ", repeat=randomlength))
            for i in range(len(name)):
                char_data.append("".join(name[i]))
            for i in range(int(no_rows)):
                name_data.append(prefix + random.choice(char_data) + suffix)
    elif datatype == "RandomInteger":
        name = list(product("0123456789", repeat=int(randomlength)))
        for i in range(len(name)):
            int_data.append("".join(name[i]))
        for i in range(int(no_rows)):
            name_data.append(prefix + random.choice(int_data) + suffix)
    return name_data



def email_data(no_rows, prefix, suffix, domainName, domainType, fixedlength, userdefineddatatype, format):
    email_data = []
    #randomLength = fixedlength - int(len(prefix)) - len(suffix)
    for _ in range(int(no_rows)):
        email = fake.email()
        username = email.split('@')[0]
        domain = email.split('@')[1]
        domain_name = domain.split('.')[0]
        domain_type = domain.split('.')[1]
        if format == 'Prefix+randomname':
            email_data.append(prefix + username + '@' + domain)
        elif format == "randomname+Suffix":
            email_data.append(username +suffix + '@' + domain)
        elif format == "Prefix+randomname+Suffix":
            email_data.append(prefix + username + suffix + '@' + domain)
        elif format == "Prefix+randomname+DomainName":
            email_data.append(prefix + username + '@' + domainName + '.' + domain_type)
        elif format == "Suffix+randomname+DomainName":
            email_data.append(username + suffix + '@' + domainName + '.' + domain_type)
        elif format == "Prefix+randomname+DomainType":
            email_data.append(prefix + username + '@' + domain_name + '.' + domainType)
        elif format == "Suffix+randomname+DomainType":
            email_data.append(username + suffix + '@' + domain_name + '.' + domainType)
        elif format == "Prefix+randomname+DomainName+DomainType":
            email_data.append(prefix + username + '@' + domainName + '.' + domainType)
        elif format == "Suffix+randomname+DomainName+DomainType":
            email_data.append(username + suffix + '@' + domainName + '.' + domainType)
        elif format == "Prefix+randomname+Suffix+DomainName":
            email_data.append(prefix + username + suffix + '@' + domainName + '.' + domain_type)
        elif format == "Prefix+randomname+Suffix+DomainType":
            email_data.append(prefix + username + suffix + '@' + domain_name + '.' + domainType)
        elif format == "Prefix+randomname+Suffix+DomainName+DomainType":
            email_data.append(prefix + username + suffix + '@' + domainName + '.' + domainType)
        elif format == "RandomE-Mail":
            email_data.append(email)
    return email_data