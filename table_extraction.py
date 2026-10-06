import pandas as pd
import requests
from io import StringIO

url = "https://www.w3schools.com/html/html_tables.asp"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

print("Status Code:", response.status_code)

html_data = StringIO(response.text)

tables = pd.read_html(html_data)

print("Number of tables found:", len(tables))

df = tables[0]

print("\nExtracted Table:")
print(df.to_string(index=False))

print("\nFirst Five Rows:")
print(df.head().to_string(index=False))

print("\nShape of the table:")
print(df.shape)

df.to_csv("extracted_table.csv", index=False)
df.to_excel("extracted_table.xlsx", index=False)

print("\nTable saved successfully as CSV and Excel files.")










