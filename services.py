# # from app import app
# # from models import db, File
# # from config import Config
# import pandas as pd
# import pdfplumber

# def pdf_to_structured_text(pdf_path):
#     structured_text = ""
    
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             # Extract text with layout to preserve structure
#             text = page.extract_text(x_tolerance=1, y_tolerance=1,layout = True)
#             print(text)
#             if text:
#                 structured_text += text + "\n"
                
    
#     return structured_text


# def convert_text_to_table(text):
#     lines = text.strip().split("\n")
#     headers = ["Compte", "Débit", "Crédit"]
#     table_data = []

#     for line in lines:
#         # Skip empty lines
#         if not line.strip():
#             continue
        
#         # Split the line into columns based on fixed widths
#         compte = line[:40].strip()
#         debit = line[40:60].strip().replace(',', '')
#         credit = line[60:].strip().replace(',', '')

#         # Add the row to the table data
#         table_data.append([compte, debit, credit])
    
#     # Create a DataFrame
#     df = pd.DataFrame(table_data, columns=headers)
    
#     # Handle empty cells and conversion to numeric where possible
#     df = df.replace("", "0")
#     df["Débit"] = pd.to_numeric(df["Débit"], errors='coerce').fillna(0)
#     df["Crédit"] = pd.to_numeric(df["Crédit"], errors='coerce').fillna(0)
#     df = df.drop([0, 1, 2, 3, 10, 11, 12])

#     # Reset the index if needed
#     df = df.reset_index(drop=True)
    
#     return df
#______________________________________________________________________________________________________________________________________________
# import pandas as pd
# import pdfplumber
# import requests
# import json
# from decimal import Decimal

# def pdf_to_structured_text(pdf_path):
#     structured_text = ""
#     with pdfplumber.open(pdf_path) as pdf:
#         for page in pdf.pages:
#             text = page.extract_text(x_tolerance=1, y_tolerance=1, layout=True)
#             print(text)
#             if text:
#                 structured_text += text + "\n"
#     return structured_text

# def convert_text_to_table(text):
#     lines = text.strip().split("\n")
#     headers = ["Compte", "Débit", "Crédit"]
#     table_data = []
    
#     for line in lines:
#         if not line.strip():
#             continue
        
#         compte = line[:40].strip()
#         debit = line[40:60].strip().replace(',', '')
#         credit = line[60:].strip().replace(',', '')

#         table_data.append([compte, debit, credit])
    
#     df = pd.DataFrame(table_data, columns=headers)
#     df = df.replace("", "0")
#     df["Débit"] = pd.to_numeric(df["Débit"], errors='coerce').fillna(0)
#     df["Crédit"] = pd.to_numeric(df["Crédit"], errors='coerce').fillna(0)
#     df = df.drop([0, 1, 2, 3, 10, 11, 12])
#     df = df.reset_index(drop=True)
    
#     return df

# def transform_df_to_json(df):
#     data = {
#         "collateralHouseAmountDebit": Decimal(df.loc[df['Compte'] == 'COMPTE COLLATERAL HOUSE', 'Débit'].sum()),
#         "collateralHouseAmountCredit": Decimal(df.loc[df['Compte'] == 'COMPTE COLLATERAL HOUSE', 'Crédit'].sum()),
#         "collateralAmountDebit": Decimal(df.loc[df['Compte'] == 'COMPTECOLLATERALCLIENT', 'Débit'].sum()),
#         "collateralAmountCredit": Decimal(df.loc[df['Compte'] == 'COMPTECOLLATERALCLIENT', 'Crédit'].sum()),
#         "marginHouseAmountDebit": Decimal(df.loc[df['Compte'] == 'COMPTEMARGINHOUSE', 'Débit'].sum()),
#         "marginHouseAmountCredit": Decimal(df.loc[df['Compte'] == 'COMPTEMARGINHOUSE', 'Crédit'].sum()),
#         "marginAmountDebit": Decimal(df.loc[df['Compte'] == 'COMPTEMARGINCLIENT', 'Débit'].sum()),
#         "marginAmountCredit": Decimal(df.loc[df['Compte'] == 'COMPTEMARGINCLIENT', 'Crédit'].sum()),
#         "settlementHouseAmountDebit": Decimal(df.loc[df['Compte'] == 'COMPTE SETTLEMENT HOUSE', 'Débit'].sum()),
#         "settlementHouseAmountCredit": Decimal(df.loc[df['Compte'] == 'COMPTE SETTLEMENT HOUSE', 'Crédit'].sum()),
#         "settlementAmountDebit": Decimal(df.loc[df['Compte'] == 'COMPTE SETTLEMENT CLIENT', 'Débit'].sum()),
#         "settlementAmountCredit": Decimal(df.loc[df['Compte'] == 'COMPTE SETTLEMENT CLIENT', 'Crédit'].sum()),
#         "Comission": Decimal(df.loc[df['Compte'] == 'COMMISSION', 'Débit'].sum())
#     }
#     return
import pandas as pd
import pdfplumber
import requests
import json
from decimal import Decimal

def pdf_to_structured_text(pdf_path):
    structured_text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text = page.extract_text(x_tolerance=1, y_tolerance=1, layout=True)
            if text:
                structured_text += text + "\n"
    return structured_text

def convert_text_to_table(text):
    lines = text.strip().split("\n")
    headers = ["Compte", "Débit", "Crédit"]
    table_data = []
    
    for line in lines:
        if not line.strip():
            continue
        
        compte = line[:40].strip()
        debit = line[40:60].strip().replace(',', '')
        credit = line[60:].strip().replace(',', '')

        table_data.append([compte, debit, credit])
    
    df = pd.DataFrame(table_data, columns=headers)
    df = df.replace("", "0")
    df["Débit"] = pd.to_numeric(df["Débit"], errors='coerce').fillna(0)
    df["Crédit"] = pd.to_numeric(df["Crédit"], errors='coerce').fillna(0)
    df = df.drop([0, 1, 2, 3, 10, 11, 12])
    df = df.reset_index(drop=True)
    
    return df

def transform_df_to_json(df):
    data = {
        "collateralHouseAmountDebit": str(Decimal(df.loc[df['Compte'] == 'COMPTE COLLATERAL HOUSE', 'Débit'].sum())),
        "collateralHouseAmountCredit": str(Decimal(df.loc[df['Compte'] == 'COMPTE COLLATERAL HOUSE', 'Crédit'].sum())),
        "collateralAmountDebit": str(Decimal(df.loc[df['Compte'] == 'COMPTECOLLATERALCLIENT', 'Débit'].sum())),
        "collateralAmountCredit": str(Decimal(df.loc[df['Compte'] == 'COMPTECOLLATERALCLIENT', 'Crédit'].sum())),
        "marginHouseAmountDebit": str(Decimal(df.loc[df['Compte'] == 'COMPTEMARGINHOUSE', 'Débit'].sum())),
        "marginHouseAmountCredit": str(Decimal(df.loc[df['Compte'] == 'COMPTEMARGINHOUSE', 'Crédit'].sum())),
        "marginAmountDebit": str(Decimal(df.loc[df['Compte'] == 'COMPTEMARGINCLIENT', 'Débit'].sum())),
        "marginAmountCredit": str(Decimal(df.loc[df['Compte'] == 'COMPTEMARGINCLIENT', 'Crédit'].sum())),
        "settlementHouseAmountDebit": str(Decimal(df.loc[df['Compte'] == 'COMPTE SETTLEMENT HOUSE', 'Débit'].sum())),
        "settlementHouseAmountCredit": str(Decimal(df.loc[df['Compte'] == 'COMPTE SETTLEMENT HOUSE', 'Crédit'].sum())),
        "settlementAmountDebit": str(Decimal(df.loc[df['Compte'] == 'COMPTE SETTLEMENT CLIENT', 'Débit'].sum())),
        "settlementAmountCredit": str(Decimal(df.loc[df['Compte'] == 'COMPTE SETTLEMENT CLIENT', 'Crédit'].sum())),
        "comissionCDebit": str(Decimal(df.loc[df['Compte'] == 'COMMISSION', 'Débit'].sum())),
        "comissionCredit": str(Decimal(df.loc[df['Compte'] == 'COMMISSION', 'Crédit'].sum()))
    }
    return json.dumps(data)

def send_data_to_microservice(data_json):
    url = "http://your-spring-boot-service/endpoint"
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, headers=headers, data=data_json)
    return response
