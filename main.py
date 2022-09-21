import ast
import base64
import json
import os.path

import mysql.connector
import pandas as pd
from flask import *
from flask_cors import CORS
import India_data
import bank
import country
import data
import sampletestdata

app._static_folder = os.path.abspath("static/")
app = Flask(__name__)
CORS(app)

# debugger
app.debug = True
app.secret_key = 'development key'

app.config['JSON_SORT_KEYS'] = False
connection = mysql.connector.connect(host='14.99.175.107',port ='17633', database='flexib_db', user='root', password='root')
print(connection)

@app.route('/')
def homepage():
    return "home"

@app.route('/sample_data', methods=['Post'])
def sample_data():
    email = []
    name = []
    id = []
    aadharData = []
    Pancard = []
    SSN = []
    Sin = []
    Words = []
    Paragraph = []
    URL = []
    Booleanvalues = []
    Currency = []
    Color = []
    Specialcharacter = []
    Zipcode = []
    LatLong = []
    Shortcountrycode = []
    Numbers = []
    Gender = []
    IPAddress = []
    Creditcardno = []
    Date = []
    Password = []
    IFSC = []
    Bankaccountno = []
    City = []
    State = []
    Address = []
    Country = []
    PhoneNo = []
    response = request.json
    print(response)
    records = response['noofrows']
    # if response['type'] == "preview":
    if 'type' in response:
        exportFormat = ""
    else:
        exportFormat = response['exportformat']
    for i in range(len(response['columndata'])):
        dataOptions = response['columndata'][i]["DataOptions"]
        dataop = dataOptions.split(",")
        for j in range(len(dataop)):
            response['columndata'][i][dataop[j].split(" - ")[0]] = dataop[j].split(" - ")[1]
        del response['columndata'][i]['DataOptions']
    print(response)
    datagenerate = {}
    for i in range(len(response["columndata"])):
        if response["columndata"][i]["DataType"] == 'ID':
            # id_generate(no_rows,prefix,suffix,fixlength,Formats,datatype)
            if response["columndata"][i]['Formats'] == "Prefix+Random":
                id.append(
                    sampletestdata.id_generate(records, response["columndata"][i]["prefix"], "",
                                               response["columndata"][i]["fixlength"], "",
                                               response["columndata"][i]["dataType"]))
            elif response["columndata"][i]['Formats'] == "Random+Suffix":
                id.append(
                    sampletestdata.id_generate(records, "", response["columndata"][i]["suffix"],
                                               response["columndata"][i]["fixlength"], "",
                                               response["columndata"][i]["dataType"]))
            elif response["columndata"][i]['Formats'] == "Prefix+Random+Suffix":
                id.append(
                    sampletestdata.id_generate(records, response["columndata"][i]["prefix"],
                                               response["columndata"][i]["suffix"],
                                               response["columndata"][i]["fixlength"], "",
                                               response["columndata"][i]["dataType"]))

            elif response["columndata"][i]['Formats'] == "Random+Suffix":
                id.append(
                    sampletestdata.id_generate(records, "", response["columndata"][i]["suffix"],
                                               response["columndata"][i]["fixlength"], "",
                                               response["columndata"][i]["dataType"]))
            elif response["columndata"][i]['Formats'] == "SequentialString":
                id.append(sampletestdata.id_generate(records, "", "", response["columndata"][i]["fixlength"], "",
                                                     response["columndata"][i]["dataType"]))

            elif response["columndata"][i]['Formats'] == "SequentialInteger":
                id.append(sampletestdata.id_generate(records, "", "", response["columndata"][i]["fixlength"],
                                                     "SequentialInteger", response["columndata"][i]["dataType"]))
            for j in range(len(id)):
                datagenerate[response['columndata'][i]["ColumnName"]] = id[j]
        elif response["columndata"][i]["DataType"] == 'Name':
            # name(no_rows,prefix,suffix,fixlength,Formats)
            if response["columndata"][i]['Formats'] == "Prefix+RandomName":
                name.append(sampletestdata.name(records, response["columndata"][i]["prefix"], "",
                                                response["columndata"][i]["fixlength"], "",
                                                response["columndata"][i]["dataType"]))
            elif response["columndata"][i]['Formats'] == "RandomName+Suffix":
                name.append(sampletestdata.name(records, "", response["columndata"][i]["suffix"],
                                                response["columndata"][i]["fixlength"], "",
                                                response["columndata"][i]["dataType"]))
            elif response["columndata"][i]['Formats'] == "Prefix+RandomName+Suffix":
                name.append(
                    sampletestdata.name(records, response["columndata"][i]["prefix"],
                                        response["columndata"][i]["suffix"], response["columndata"][i]["fixlength"], "",
                                        response["columndata"][i]["dataType"]))
            elif response["columndata"][i]['Formats'] == "FullName":
                name.append(sampletestdata.name(records, "", "", response["columndata"][i]["fixlength"], "FullName",
                                                response["columndata"][i]["dataType"]))
            elif response["columndata"][i]['Formats'] == "FirstName":
                name.append(sampletestdata.name(records, "", "", response["columndata"][i]["fixlength"], "FirstName",
                                                response["columndata"][i]["dataType"]))
            elif response["columndata"][i]['Formats'] == "LastName":
                name.append(sampletestdata.name(records, "", "", response["columndata"][i]["fixlength"], "LastName",
                                                response["columndata"][i]["dataType"]))
            # print(name)
            for j in range(len(name)):
                datagenerate[response['columndata'][i]["ColumnName"]] = name[j]
        elif response["columndata"][i]["DataType"] == 'Email':
            # email_data(no_rows, prefix, suffix, domainName, domainType, fixlength, userdefineddatatype, Formats)
            if response["columndata"][i]['Formats'] == "Prefix+randomname":
                email.append(sampletestdata.email_data(records, response["columndata"][i]["prefix"],
                                                       "", "", "", "", ",", response["columndata"][i]["Formats"]))

            elif response["columndata"][i]['Formats'] == 'randomname+Suffix':
                email.append(sampletestdata.email_data(records, "", response["columndata"][i]["suffix"], "", "", "",
                                                       ",", response["columndata"][i]["Formats"]))

            elif response["columndata"][i]['Formats'] == 'Prefix+randomname+Suffix':
                email.append(sampletestdata.email_data(records, response["columndata"][i]["prefix"],
                                                       response["columndata"][i]["suffix"], "", "", "", ",",
                                                       response["columndata"][i]["Formats"]))

            elif response["columndata"][i]['Formats'] == "Prefix+randomname+DomainName":
                email.append(sampletestdata.email_data(records, response["columndata"][i]["prefix"], "",
                                                       response["columndata"][i]["domainName"],
                                                       "", "", "", response["columndata"][i]["Formats"]))

            elif response["columndata"][i]['Formats'] == "Suffix+randomname+DomainName":
                email.append(sampletestdata.email_data(records, "", response["columndata"][i]["suffix"],
                                                       response["columndata"][i]["domainName"],
                                                       "", "", "", response["columndata"][i]["Formats"]))

            elif response["columndata"][i]['Formats'] == "Prefix+randomname+DomainType":
                email.append(sampletestdata.email_data(records, response["columndata"][i]["prefix"], "", "",
                                                       response["columndata"][i]["domainType"], "", "",
                                                       response["columndata"][i]["Formats"]))
            elif response["columndata"][i]['Formats'] == "Suffix+randomname+DomainType":
                email.append(sampletestdata.email_data(records, "", response["columndata"][i]["suffix"], "",
                                                       response["columndata"][i]["domainType"], "", "",
                                                       response["columndata"][i]["Formats"]))
            elif response["columndata"][i]['Formats'] == "Prefix+randomname+DomainName+DomainType":
                email.append(sampletestdata.email_data(records, response["columndata"][i]["prefix"], "",
                                                       response["columndata"][i]["domainName"],
                                                       response["columndata"][i]["domainType"], "", "",
                                                       response["columndata"][i]["Formats"]))
            elif response["columndata"][i]['Formats'] == "Suffix+randomname+DomainName+DomainType":
                email.append(sampletestdata.email_data(records, "", response["columndata"][i]["suffix"],
                                                       response["columndata"][i]["domainName"],
                                                       response["columndata"][i]["domainType"], "", "",
                                                       response["columndata"][i]["Formats"]))
            elif response["columndata"][i]['Formats'] == "Prefix+randomname+Suffix+DomainName":
                email.append(sampletestdata.email_data(records, response["columndata"][i]["prefix"],
                                                       response["columndata"][i]["suffix"],
                                                       response["columndata"][i]["domainName"],
                                                       "", "", "", response["columndata"][i]["Formats"]))
            elif response["columndata"][i]['Formats'] == "Prefix+randomname+Suffix+DomainType":
                email.append(sampletestdata.email_data(records, response["columndata"][i]["prefix"],
                                                       response["columndata"][i]["suffix"], "",
                                                       response["columndata"][i]["domainType"], "", "",
                                                       response["columndata"][i]["Formats"]))
            elif response["columndata"][i]['Formats'] == "Prefix+randomname+Suffix+DomainName+DomainType":
                email.append(sampletestdata.email_data(records, response["columndata"][i]["prefix"],
                                                       response["columndata"][i]["suffix"],
                                                       response["columndata"][i]["domainName"],
                                                       response["columndata"][i]["domainType"], "", "",
                                                       response["columndata"][i]["Formats"]))
            elif response["columndata"][i]['Formats'] == "RandomE-Mail":
                email.append(
                    sampletestdata.email_data(records, "", "", "", "", "", "", response["columndata"][i]["Formats"]))
            # print("email data")
            # print(email)
            # print(email[0])

            for j in range(len(email)):
                datagenerate[response['columndata'][i]["ColumnName"]] = email[j]
                # Datatype == Email
        elif response["columndata"][i]["DataType"] == 'AadharCard':
            aadharData.append(India_data.Aadhar(records))
            for j in range(len(aadharData)):
                datagenerate[response['columndata'][i]["ColumnName"]] = aadharData[j]
        elif response["columndata"][i]["DataType"] == 'Pancard':
            Pancard.append(data.Pancard(records))
            for j in range(len(Pancard)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Pancard[j]
        elif response["columndata"][i]["DataType"] == 'Sin':
            Sin.append(data.Sin(records))
            for j in range(len(Sin)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Sin[j]
        elif response["columndata"][i]["DataType"] == 'SSN':
            SSN.append(data.Ssn(records))
            for j in range(len(SSN)):
                datagenerate[response['columndata'][i]["ColumnName"]] = SSN[j]
        elif response["columndata"][i]["DataType"] == 'Words':
            Words.append(data.Word(records, response["columndata"][i]["fixlength"]))
            for j in range(len(Words)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Words[j]
        elif response["columndata"][i]["DataType"] == 'Paragraph':
            Paragraph.append(data.Paragraph(records, "1"))
            for j in range(len(Paragraph)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Paragraph[j]
        elif response["columndata"][i]["DataType"] == 'URL':
            URL.append(data.Url(records, ""))
            for j in range(len(URL)):
                datagenerate[response['columndata'][i]["ColumnName"]] = URL[j]
        elif response["columndata"][i]["DataType"] == 'Booleanvalues':
            Booleanvalues.append(data.Boolean_values(records, response["columndata"][i]["Formats"]))
            for j in range(len(Booleanvalues)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Booleanvalues[j]
        
        elif response["columndata"][i]["DataType"] == 'Currency':
            if response["columndata"][i]["Formats"] != 'Short+FullName':
                Currency = []
                CurrencyshortName = []
                Currency.append(data.Currency(records, response["columndata"][i]["Formats"]))
                for j in range(len(Currency[0])):
                    CurrencyshortName.append(Currency[0][j])
                datagenerate[response['columndata'][i]["ColumnName"].split(",")[0]] = CurrencyshortName
            else:
                Currency = []
                CurrencyshortName = []
                CurrencyfullName = []
                Currency.append(data.Currency(records, response["columndata"][i]["Formats"]))
                for j in range(len(Currency[0])):
                    CurrencyshortName.append(Currency[0][j][0])
                    CurrencyfullName.append(Currency[0][j][1])
                datagenerate[response['columndata'][i]["ColumnName"].split(",")[0]] = CurrencyshortName
                datagenerate[response['columndata'][i]["ColumnName"].split(",")[1]] = CurrencyfullName
        elif response["columndata"][i]["DataType"] == 'Color':
            if response["columndata"][i]["Formats"] != "ColorNamewithHexCode":
                Color = []
                colorNameData = []
                Color.append(data.Color(records, response["columndata"][i]["Formats"]))
                print(Color)
                for j in range(len(Color[0])):
                    colorNameData.append(Color[0][j])
                datagenerate[response['columndata'][i]["ColumnName"].split(",")[0]] = colorNameData
            else:
                Color = []
                Color.append(data.Color(records, response["columndata"][i]["Formats"]))
                colorNameData = []
                colorHexData = []
                for j in range(len(Color[0])):
                    colorNameData.append(Color[0][j][0])
                    colorHexData.append(Color[0][j][1])
                datagenerate[response['columndata'][i]["ColumnName"].split(",")[0]] = colorNameData
                datagenerate[response['columndata'][i]["ColumnName"].split(",")[1]] = colorHexData
        
        elif response["columndata"][i]["DataType"] == 'Specialcharacter':
            Specialcharacter.append(data.Special_characters(records, response["columndata"][i]["fixlength"]))
            for j in range(len(Specialcharacter)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Specialcharacter[j]
        elif response["columndata"][i]["DataType"] == 'Zipcode':
            Zipcode.append(country.zipcode(records, response["columndata"][i]["Formats"], ""))
            for j in range(len(Zipcode)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Zipcode[j]
        elif response["columndata"][i]["DataType"] == 'Lat&Long':
            
            if response["columndata"][i]["Formats"] != "LatitudeandLongitude":
                LatLong = []
                latitudeData = []
                LatLong.append(data.latlong(records, "", response["columndata"][i]["Formats"]))
                for j in range(len(LatLong[0])):
                    latitudeData.append(LatLong[0][j])
                datagenerate[response['columndata'][i]["ColumnName"].split(",")[0]] = latitudeData
            else:
                LatLong = []
                latitudeData = []
                longitudeData = []
                LatLong.append(data.latlong(records, "", response["columndata"][i]["Formats"]))
                for j in range(len(LatLong[0])):
                    latitudeData.append(LatLong[0][j][0])
                    longitudeData.append(LatLong[0][j][1])
                datagenerate[response['columndata'][i]["ColumnName"].split(",")[0]] = latitudeData
                datagenerate[response['columndata'][i]["ColumnName"].split(",")[1]] = longitudeData
        elif response["columndata"][i]["DataType"] == 'Shortcountrycode':
            Shortcountrycode.append(data.Country_code(records))
            for j in range(len(Shortcountrycode)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Shortcountrycode[j]
        elif response["columndata"][i]["DataType"] == 'Numbers':
            Numbers.append(data.Number(records, response["columndata"][i]["Formats"],
                                       response["columndata"][i]["fixlength"]))
            for j in range(len(Numbers)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Numbers[j]
        elif response["columndata"][i]["DataType"] == 'Gender':
            Gender.append(data.gender(records))
            for j in range(len(Gender)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Gender[j]
        elif response["columndata"][i]["DataType"] == 'IPAddress':
            IPAddress.append(data.ip_address(records))
            for j in range(len(IPAddress)):
                datagenerate[response['columndata'][i]["ColumnName"]] = IPAddress[j]
        elif response["columndata"][i]["DataType"] == 'Creditcardno':
            Creditcardno.append(data.Credit_card_number(records, response["columndata"][i]["Formats"]))
            for j in range(len(Creditcardno)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Creditcardno[j]
        elif response["columndata"][i]["DataType"] == 'Date':
            Date.append(data.date(records, response["columndata"][i]["Formats"]))
            for j in range(len(Date)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Date[j]
        elif response["columndata"][i]["DataType"] == 'Password':
            if response["columndata"][i]["Formats"] == "StringPassword":
                Password.append(data.Password(records, "", "", response["columndata"][i]["fixlength"],
                                              response["columndata"][i]["Formats"], ""))
            elif response["columndata"][i]["Formats"] == "IntegerPassword":
                Password.append(data.Password(records, "", "", response["columndata"][i]["fixlength"],
                                              response["columndata"][i]["Formats"], ""))
            elif response["columndata"][i]["Formats"] == "Prefix+Random":
                Password.append(data.Password(records, response["columndata"][i]["prefix"], "",
                                              response["columndata"][i]["fixlength"],
                                              response["columndata"][i]["Formats"],
                                              response["columndata"][i]["dataType"]))
            elif response["columndata"][i]["Formats"] == "Suffix+Random":
                Password.append(data.Password(records, "", response["columndata"][i]["suffix"],
                                              response["columndata"][i]["fixlength"],
                                              response["columndata"][i]["Formats"],
                                              response["columndata"][i]["dataType"]))
            elif response["columndata"][i]["Formats"] == "Prefix+Random+Suffix":
                Password.append(data.Password(records, response["columndata"][i]["prefix"],
                                              response["columndata"][i]["suffix"],
                                              response["columndata"][i]["fixlength"],
                                              response["columndata"][i]["Formats"],
                                              response["columndata"][i]["dataType"]))
            elif response["columndata"][i]["Formats"] == "SpecialCharactersPassword":
                Password.append(data.Password(records, "", "", response["columndata"][i]["fixlength"],
                                              response["columndata"][i]["Formats"], ""))
            elif response["columndata"][i]["Formats"] == "RandomPassword":
                Password.append(data.Password(records, "", "", response["columndata"][i]["fixlength"],
                                              response["columndata"][i]["Formats"], ""))
            for j in range(len(Password)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Password[j]
        elif response["columndata"][i]["DataType"] == 'IFSC':
            IFSC.append(bank.IFSC_code(records, response["columndata"][i]["Formats"]))
            for j in range(len(IFSC)):
                datagenerate[response['columndata'][i]["ColumnName"]] = IFSC[j]
        elif response["columndata"][i]["DataType"] == 'Bankaccountno':
            Bankaccountno.append(data.Bank_account_number(records, response["columndata"][i]["Formats"]))
            for j in range(len(Bankaccountno)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Bankaccountno[j]
        elif response["columndata"][i]["DataType"] == 'City':
            City.append(country.city(records, response["columndata"][i]["Formats"]))
            for j in range(len(City)):
                datagenerate[response['columndata'][i]["ColumnName"]] = City[j]
        elif response["columndata"][i]["DataType"] == 'State':
            State.append(country.state(records, response["columndata"][i]["Formats"]))
            for j in range(len(State)):
                datagenerate[response['columndata'][i]["ColumnName"]] = State[j]
        elif response["columndata"][i]["DataType"] == 'Address':
            Address.append(India_data.Address(records))
            for j in range(len(Address)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Address[j]
        elif response["columndata"][i]["DataType"] == 'Country':
            Country.append(India_data.country(records, ""))
            for j in range(len(Country)):
                datagenerate[response['columndata'][i]["ColumnName"]] = Country[j]
        elif response["columndata"][i]["DataType"] == 'PhoneNo':
            PhoneNo.append(India_data.Phone_number(records))
            for j in range(len(PhoneNo)):
                datagenerate[response['columndata'][i]["ColumnName"]] = PhoneNo[j]
    df = pd.DataFrame(datagenerate)
    # print(df)
    if 'type' in response:
        if response['type'] == "preview":
            preview_data = df.to_json('static/assets/data_files/data_json.json', orient="table")
            # preview_data = pd.read_json("static/assets/data_files/data_json.json")
            preview_data_file = json.load(open('static/assets/data_files/data_json.json'))
            # df = pd.DataFrame(data["result"])
            print(preview_data)
            return jsonify({
                "message": "Success",
                "status": "200",
                "data": [preview_data_file]
            })

    if exportFormat == 'Excel':
        df.to_excel("data_excel.xlsx", index=False, engine='xlsxwriter')
        with open('data_excel.xlsx', 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_data = base64_encoded_data.decode('utf-8')
        # return base64_data
        return jsonify({
            "message": "Success",
            "status": "200",
            "ExportFormat": exportFormat,
            "data": base64_data
        })
        # base64_bytes = base64_message.encode('utf-8')
        # with open('exportdata.xlsx', 'wb') as file_to_save:
        #     decoded_data = base64.decodebytes(base64_bytes)
        #     file_to_save.write(decoded_data)

    elif exportFormat == 'Csv':
        df.to_csv('data_csv.csv', index=False)
        with open('data_csv.csv', 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_data = base64_encoded_data.decode('utf-8')
        # return base64_data
        return jsonify({
            "message": "Success",
            "status": "200",
            "ExportFormat": exportFormat,
            "data": base64_data
        })
    elif exportFormat == 'JSON':
        df.to_json('data_json.json', orient="table")
        with open('data_json.json', 'rb') as binary_file:
            binary_file_data = binary_file.read()
            base64_encoded_data = base64.b64encode(binary_file_data)
            base64_data = base64_encoded_data.decode('utf-8')
        # return base64_data
        return jsonify({
            "message": "Success",
            "status": "200",
            "ExportFormat": exportFormat,
            "data": base64_data
        })
    return "Done"


@app.route('/fetch_project_names', methods=['GET'])
def fetch_project_names():
    try:
        projectName = []
        project_data = {}
        project_data['Project_list'] = []
        cursor = connection.cursor()
        query = "select Project_name from project"
        cursor.execute(query)
        fields = cursor.fetchall()
        for i in range(len(fields)):
            projectName.append(fields[i][0])
        project_data['Project_list'] += projectName
        # return project_data
        return jsonify({
            "message": "Success",
            "status": "200",
            "data": project_data
        })
    except:
        return "Exception Occured"


@app.route('/fetch_profile_names', methods=['POST'])
def fetch_profile_names():
    try:
        profile_names = []
        profile_data = dict()
        connection = mysql.connector.connect(host='14.99.175.107',port ='17633', database='flexib_db', user='root', password='root')
        print(connection)
        response = request.json
        project_name = response['Project_Name']
        print(connection)
        cursor = connection.cursor()
        args = (project_name)
        query = "select Project_ID from project where Project_name = %s"
        cursor.execute(query, (args,))
        ver = cursor.fetchall()
        print(ver)
        args = (ver[0][0])
        query = "select Profile_name from user_profiles where Project_ID = %s"
        cursor.execute(query, (args,))
        profile = cursor.fetchall()
        print(profile)
        if len(profile) != 0:
            for i in range(len(profile)):
                profile_data['profilename'] = profile[i][0]
                print(profile_data)
                profile_names.append(profile_data.copy())
            # return jsonify(profile_names
            return jsonify({
                "message": "Success",
                "status": "200",
                "data": profile_names
            })
        else:
            return "Profile is not created for this project"
    except:
        return "Exception Occured"


@app.route('/check_format', methods=['POST'])
def check_format():
    try:
        response = request.json
        project_name = response['Project_Name']
        connection = mysql.connector.connect(host='14.99.175.107',port ='17633', database='flexib_db', user='root', password='root')
        cursor = connection.cursor()
        print(connection)
        args = (project_name)
        query = "select Project_ID from project where Project_name = %s"
        cursor.execute(query, (args,))
        project_ID = cursor.fetchall()
        print(project_ID)
        profile_name = response['Profile_Name']
        args = (project_ID[0][0], profile_name)
        query = "select Fields from user_profiles where Project_ID = %s and Profile_name = %s"
        cursor.execute(query, args)
        fields = cursor.fetchall()
        print(fields)
        format_data = str(fields[0][0])
        profile_format = format_data.replace('"', "'")
        profile_data = ast.literal_eval(profile_format)
        # return jsonify(profile_data)
        return jsonify({
            "message": "Success",
            "status": "200",
            "data": profile_data
        })
    except:
        return jsonify({"Message": "Exception Occured"})


@app.route('/delete_profile', methods=['POST'])
def delete_profile():
    try:
        response = request.json
        project_name = response['Project_Name']
        profile_name = response['Profile_Name']
        connection = mysql.connector.connect(host='14.99.175.107',port ='17633', database='flexib_db', user='root', password='root')
        cursor = connection.cursor()
        print(connection)
        args = (project_name)
        query = "select Project_ID from project where Project_name = %s"
        cursor.execute(query, (args,))
        project_ID = cursor.fetchall()
        print(project_ID)
        args = (profile_name, project_ID[0][0])
        query = "select * from user_profiles where Profile_name = %s and Project_ID = %s ;"
        cursor.execute(query, args)
        profiles_data = cursor.fetchall()
        print(profiles_data)
        if len(profiles_data) != 0:
            args = (profile_name, project_ID[0][0])
            query = "SET SQL_SAFE_UPDATES = 0;"
            cursor.execute(query)
            query = "delete from user_profiles where Profile_name = %s and Project_ID = %s ;"
            cursor.execute(query, args)
            query = "SET SQL_SAFE_UPDATES = 1;"
            cursor.execute(query)
            connection.commit()
            # return jsonify({"Message" : "Profile is deleted"})
            return jsonify({
                "message": "Success",
                "status": "200"
            })
        else:
            return jsonify({"Message": "Profile is Not Exist"})
    except:
        return "Exception Occured"


@app.route('/create_profile', methods=['POST'])
def create_profile():
    try:
        response = request.json
        project_name = response['Project_Name']
        profile_name = response['Profile_Name']
        connection = mysql.connector.connect(host='14.99.175.107',port ='17633', database='flexib_db', user='root', password='root')
        fields = response['fields']
        fields = str(fields).replace("'", '"')
        cursor = connection.cursor()
        print(connection)
        args = (project_name)
        query = "select Project_ID from project where Project_name = %s"
        cursor.execute(query, (args,))
        project_ID = cursor.fetchall()
        print(project_ID)
        cursor = connection.cursor()
        args = (profile_name)
        query = "select * from user_profiles where Profile_name =%s"
        cursor.execute(query, (args,))
        ver = cursor.fetchall()
        print(ver)
        if (len(ver) == 0):
            cursor = connection.cursor()
            args = (profile_name, fields, project_ID[0][0])
            query = "insert into user_profiles(Profile_name,Fields,Project_ID)values(%s,%s,%s)"
            cursor.execute(query, args)
            connection.commit()
            # return jsonify({"Message" :"Profile created successfully"})
            return jsonify({
                "message": "Success",
                "status": "200"
            })
        else:
            if (ver[0][1] == profile_name):
                return jsonify({"Message": "Profile already registered"})
    except:
        return jsonify({"Message": "Exception Occured"})


if __name__ == '__main__':
    # from waitress import serve
    # serve(app, host="0.0.0.0", port=5001)
    app.run(host="0.0.0.0", port=5001, debug=True, threaded=True)
