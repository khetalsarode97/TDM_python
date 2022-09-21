import datetime
import random
import string
from itertools import product
from random import randint

import pandas as pd
from faker import Faker

fake = Faker()



def id_generate(no_rows, prefix, suffix, fixedlength, format):
    id_data = []
    randomlength = int(fixedlength) - len(prefix) - len(suffix)
    try:
        if format == 'SequentialInteger':
            data = list(product("0123456789", repeat=randomlength))
            for i in range(int(no_rows)):
                id_data.append("".join(data[i]))
        else:
            data = list(product("ABCDEFGHJKLMNOPQRSTUVWXYZ", repeat=randomlength))
            for i in range(int(no_rows)):
                id_data.append(prefix + "".join(data[i]) + suffix)
        return id_data
    except:
        return "Exception Occured"




def name(no_rows, prefix, suffix, fixedlength, format):
    name_data = []
    data_count = 0
    randomlength = int(fixedlength) - len(prefix) - len(suffix)
    print(randomlength)
    while True:
        if format == "LastName":
            name = fake.last_name()
        elif format == "FullName":
            name = fake.name()
        else:
            name = fake.first_name()
        if len(name) == randomlength:
            name_data.append(prefix + name + suffix)
            data_count += 1
        if data_count == no_rows:
            break
    return name_data


def First_name(no_rows, num):
    data_count = 0
    first_name = []
    while True:
        name = fake.first_name()
        if len(name) <= num:
            first_name.append(name)
            data_count += 1
        if data_count == no_rows:
            break
    return first_name


def Last_name(no_rows, num):
    data_count = 0
    last_name = []
    while True:
        name = fake.last_name()
        if len(name) <= num:
            last_name.append(name)
            data_count += 1
        if data_count == no_rows:
            break
    return last_name



def email_data(no_rows, prefix, suffix, domainName, domainType, fixedlength, userdefineddatatype, format):
    email_data = []
    #randomLength = fixedlength - int(len(prefix)) - len(suffix)
    for _ in range(no_rows):
        email = fake.email()
        username = email.split('@')[0]
        domain = email.split('@')[1]
        domain_name = domain.split('.')[0]
        domain_type = domain.split('.')[1]
        if format == 'Prefix+randomname' or format == 'randomname+Suffix' or format == 'Prefix+randomname+Suffix':
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
        else:
            email_data.append(email)
    return email_data




def Password(num, prefix, suffix, fixedlength, format, type):
    password = []
    randomlength = int(fixedlength) - len(prefix) - len(suffix)
    for _ in range(int(num)):
        if format == "StringPassword":
            characters = string.ascii_letters
        elif format == "IntegerPassword":
            characters = string.digits + string.punctuation
        elif format == "Prefix+Random" or format == "Suffix+Random" or format == "Prefix+Random+Suffix":
            if type == "RandomString":
                characters = string.ascii_letters + string.punctuation
            elif type == "RandomInteger":
                characters = string.digits + string.punctuation
        elif format == "SpecialCharactersPassword":
            characters = string.punctuation
        elif format == "RandomPassword":
            characters = string.ascii_letters + string.digits + string.punctuation

        pass1 = prefix + ''.join(random.choice(characters) for i in range(randomlength)) + suffix
        password.append(pass1)
    return password




def Special_characters(no_rows, length):
    special_character = []
    for i in range(int(no_rows)):
        special_char = string.punctuation
        string1 = ''.join(random.choice(special_char) for i in range(int(length)))
        special_character.append(string1)
    return special_character


def Paragraph(no_rows, length):
    paragraph = []
    for _ in range(int(no_rows)):
        sentences = fake.paragraph(nb_sentences=int(length), variable_nb_sentences=False)
        paragraph.append(sentences)
    return paragraph


def Number(num, type,fixedLength):
    numeric_data = []
    fixedLength = int(fixedLength)
    for _ in range(int(num)):
        if type == "SequentialIntegerNumbers":
            # numeric.append(_ + 1)
            data = list(product("0123456789", repeat=fixedLength))
            # for i in range(int(num)):
            numeric_data.append("".join(data[_]))
        elif type == "RandomNumbers":
            min = pow(10, fixedLength - 1)
            max = pow(10, fixedLength) - 1
            numeric_data.append(random.randint(min, max))
    print(numeric_data)
    return numeric_data



def Color(no_rows, format):
    colordata = []
    for _ in range(int(no_rows)):
        if format == "ColorName":
            colordata.append(fake.safe_color_name())
        elif format == "ColorHexCode":
            colordata.append(fake.color())
        elif format == "ColorNamewithHexCode":
            colorHexdata = [fake.safe_color_name(),fake.color()]
            colordata.append(colorHexdata)
    return colordata


def Credit_card_number(num, type):
    credit_card_number = []
    for _ in range(int(num)):
        if type == 'AmericanExpressCard(AMEX)':
            credit_card_number.append(fake.credit_card_number(card_type='amex'))
        elif type == 'DinersClubCards':
            credit_card_number.append(fake.credit_card_number(card_type='diners'))
        elif type == 'DiscoverCards':
            credit_card_number.append(fake.credit_card_number(card_type='discover'))
        elif type == 'JapanCreditBureauCard(JCB)':
            credit_card_number.append(fake.credit_card_number(card_type='jcb'))
        # elif type == 'jcb15':
        #     credit_card_number.append(fake.credit_card_number(card_type='jcb15'))
        # elif type == 'jcb16':
        #     credit_card_number.append(fake.credit_card_number(card_type='jcb16'))
        elif type == 'MaestroCard':
            credit_card_number.append(fake.credit_card_number(card_type='maestro'))
        elif type == 'MasterCard':
            credit_card_number.append(fake.credit_card_number(card_type='mastercard'))
        elif type == 'VisaCard13Digit ':
            credit_card_number.append(fake.credit_card_number(card_type='visa13'))
        elif type == 'VisaCard16Digit ':
            credit_card_number.append(fake.credit_card_number(card_type='visa16'))
        elif type == 'visa19':
            credit_card_number.append(fake.credit_card_number(card_type='visa19'))
        else:
            credit_card_number.append(fake.credit_card_number(card_type='visa'))
    return credit_card_number


def Bank_account_number(num, type):
    bank_account_number = []
    first_digit_sbi = ["10", "20", "30", "50", "60", "56", "66", "53", "63", "57", "67"]
    second_third_digit_axis = ['17', '18', '19', '20', '21', '22']
    fourth_fifth_digit_axis = ['01', '02', '03', '06']
    ac_no1 = []
    for _ in range(int(num)):
        if type == 'HDFCBank':
            bank_account_number.append('0' + f'{random.randrange(1, 99999999999999):13}')
        elif type == 'ICICIBank':
            df = pd.read_excel("static/assets/data_files/icici_ifsc.xlsx")
            for _ in range(len(df)):
                ac = df['IFSC CODE'][_]
                num = ac.replace("ICIC", "")
                ac_no1.append(num)
            ic = random.choice(ac_no1)
            bank_account_number.append(ic[3:] + ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)]))
        elif type == 'SBIBank':
            first_digit = random.choice(first_digit_sbi)
            bank_account_number.append(first_digit + f'{random.randrange(1, 999999999):9}')
        elif type == 'AxisBank':
            bank_account_number.append('9' + str(random.choice(second_third_digit_axis)) + str(
                random.choice(fourth_fifth_digit_axis)) + ''.join(["{}".format(randint(0, 9)) for num in range(0, 10)]))
    return bank_account_number


def Boolean_values(no_rows,format):
    boolean_values = []
    for _ in range(int(no_rows)):
        data = fake.boolean(chance_of_getting_true=50)
        if format == "1or0":
            data = str(data)
            data = data.replace("True","1")
            data = data.replace("False", "0")
            boolean_values.append(data)
        elif format == "TrueorFalse":
            boolean_values.append(data)
    return boolean_values


def Currency(no_rows, format):
    currencyData = []
    for _ in range(int(no_rows)):
        currency = fake.currency()
        if format == 'ShortName':
            currencyData.append(currency[0])
        elif format == 'FullName':
            currencyData.append(currency[1])
        elif format == 'Short+FullName':
            currencyData.append(currency)
    return currencyData

def Url(num, suffix):
    url = []
    for _ in range(int(num)):
        if (not suffix):
            url.append(fake.url())
        else:
            weblink = fake.url()
            weblink_split = weblink.split('.')
            weblink_split[-1] = str(suffix) + '/'
            url.append('.'.join(weblink_split))
    return url


def Country_code(num):
    country_code = []
    for _ in range(int(num)):
        country_code.append(fake.country_code())
    return country_code


def Ssn(num):
    ssn_data = []
    for i in range(int(num)):
        ssn_data.append(fake.ssn())
    return ssn_data


def Pancard(no_rows):
    pancard_data = []
    for i in range(int(no_rows)):
        pan = ''.join(random.choices(string.ascii_uppercase, k=5)) + f'{random.randrange(1, 9999):04}' + ''.join(
            random.choices(string.ascii_uppercase, k=1))
        pancard_data.append(pan)
    return pancard_data


def Word(no_rows,fixlength):
    word_data = []
    data_count = 0
    while True:
        word = fake.word()
        if len(word) == int(fixlength):
            word_data.append(word)
            data_count += 1
        if data_count == int(no_rows):
             break
    return word_data


def Sin(no_rows):
    sin_data = []
    for i in range(int(no_rows)):
        digit1 = f'{random.randrange(1, 999):03}'
        digit2 = f'{random.randrange(1, 999):03}'
        digit3 = f'{random.randrange(1, 999):03}'
        sin = digit1 + '-' + digit2 + '-' + digit3
        sin_data.append(sin)
    return sin_data


def ip_address(num):
    ip_address = []
    for i in range(int(num)):
        ip_address.append(fake.ipv4())
    return ip_address


def gender(no_rows):
    gender = []
    for i in range(int(no_rows)):
        gender_data = lambda: 'Male' if random.randint(0, 1) == 0 else 'Female'
        gender.append(gender_data())
    return gender

def latlong(no_rows, country_code, format):
    latlongData = []
    for i in range(int(no_rows)):
        latlong = fake.local_latlng(coords_only=True)
        #print(latlong)
        if format == "Latitude":
            latlongData.append(latlong[0])
        elif format == "Longitude":
            latlongData.append(latlong[1])
        elif format == "LatitudeandLongitude":
            latlongData.append(latlong)
    return latlongData


def date(no_rows, format):
    date = []
    for i in range(int(no_rows)):
        datetime = fake.date_time()
        if format == "Date":
            date.append(datetime.strftime("%d"))
        elif format == "Month":
            date.append(datetime.strftime("%m"))
        elif format == "Year":
            date.append(datetime.strftime("%Y"))
        elif format == "DD/MM/YYYY":
            date.append(datetime.strftime("%d/%m/%Y"))
        elif format == "YYYY/DD/MM":
            date.append(datetime.strftime("%Y/%d/%m"))
        elif format == "YYYY/MM/DD":
            date.append(datetime.strftime("%Y/%m/%d"))
        elif format == "DD.MM.YYYY":
            date.append(datetime.strftime("%d.%m.%Y"))
        elif format == "YYYY.DD.MM":
            date.append(datetime.strftime("%Y.%d.%m"))
        elif format == "YYYY.MM.DD":
            date.append(datetime.strftime("%Y.%m.%d"))
        elif format == "DD-MM-YYYY":
            date.append(datetime.strftime("%d-%m-%Y"))
        elif format == "YYYY-DD-MM":
            date.append(datetime.strftime("%Y-%d-%m"))
        elif format == "YYYY-MM-DD":
            date.append(datetime.strftime("%Y-%m-%d"))
        elif format == "DDMMYYYY":
            date.append(datetime.strftime("%d %m %Y"))
        elif format == "YYYYDDMM":
            date.append(datetime.strftime("%Y %d %m"))
        elif format == "YYYYMMDD":
            date.append(datetime.strftime("%Y %m %d"))
    return date