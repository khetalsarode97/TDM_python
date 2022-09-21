import pandas as pd
import random

def IFSC_code(no_rows, type):
    no_rows = int(no_rows)
    Ifsc_data = []
    ifsc_bank = []
    if type == 'ICICIBank':
        ifsc = pd.read_excel("static/assets/data_files/icici_ifsc.xlsx")
        for i in range(len(ifsc['IFSC CODE'])):
            ifsc_bank.append(ifsc['IFSC CODE'][i])
        for i in range(no_rows):
            Ifsc_data.append(random.choice(ifsc_bank))

    elif type == 'SBIBank':
        ifsc = pd.read_excel("static/assets/data_files/sbi_ifsc.xlsx")
        for i in range(len(ifsc['IFSC'])):
            ifsc_bank.append(ifsc['IFSC'][i])
        for i in range(no_rows):
            Ifsc_data.append(random.choice(ifsc_bank))
    elif type == 'HDFCBank':
        ifsc = pd.read_excel("static/assets/data_files/hdfc_ifsc.xlsx")
        for i in range(len(ifsc['IFSC'])):
            ifsc_bank.append(ifsc['IFSC'][i])
        for i in range(no_rows):
            Ifsc_data.append(random.choice(ifsc_bank))
    elif type == 'AxisBank':
        ifsc = pd.read_excel("static/assets/data_files/axis_ifsc.xlsx")
        for i in range(len(ifsc['IFSC'])):
            ifsc_bank.append(ifsc['IFSC'][i])
        for i in range(no_rows):
            Ifsc_data.append(random.choice(ifsc_bank))
    return Ifsc_data

