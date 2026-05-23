#Import necessary libraries

import os
from google import genai
from dotenv import load_dotenv

import pandas as pd
import io

#This is where the work is done.

load_dotenv()


def run_assassin(uploaded_file, threshold):
    uploaded_file.seek(0)

    try:
        df = pd.read_excel(uploaded_file, engine='openpyxl')
    
    except Exception:

        uploaded_file.seek(0)
        df = pd.read_csv(uploaded_file)

    required_col = "Stock_Level"
    if required_col not in df.columns:
        alternatives = ["Quantity", "Qty On Hand", "Stock", "Current_Stock"]
        found = False
        for alt in alternatives:
            if alt in df.columns:
                df.rename(columns={alt: required_col}, inplace=True)
                found = True
                break

        if not found:
            raise ValueError(f"Missing required column: {required_col}")

    results = df[df[required_col] < threshold]

    vendor_col = None
    for col in ["Vendor", "Supplier", "Manufacturer"]:
        if col in results.columns:
            vendor_col = col
            break

    if vendor_col:
        results = results.sort_values(by=[vendor_col, required_col], ascending=[True, True])

    else:
        resuls = results.sort_values(by=required_col, ascending=True)

    output = io.BytesIO()

    with pd.ExcelWriter(output, engine='openpyxl') as writer:
        results.to_excel(writer, index=False)

    output.seek(0)
    return output, results

client = genai.Client(api_key = os.getenv("GEMINI_API_KEY"))


def generate_reorder_summary(flagged_items):


    if flagged_items.empty:
        return "All stock levels are healthy.  No action required."
    

    data_summary = flagged_items.to_string(index=False)

    prompt = f"""
    You are a Strategic Procurement Manager's Assisstant in a busy distribution warehouse.
    Analyze the following inventory data: 

    {data_summary}

    Your goal is to help the buyer consolidate Purchase Orders to save time on manuallyswitching between spreadsheets when it's time to restock.
    1.  Identify which Vendor/Supplier has the highest number of low_stock items.
    2.  Recommend consolidating orders for that specific vendor to hit user-given freigh minimums.
    3.  Keep the summary professional, actionable, digestible to the reader, and under 3 sentences. 
    """

    response = client.models.generate_content(model='gemini-2.5-flash', contents=prompt)

    return response.text
