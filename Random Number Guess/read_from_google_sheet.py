import pandas as pd

sheet_id = '1nq1YQhUMDLvlMx4Oo4NGbod0l-XBzULronWhau9CUl0'
df = pd.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv")
print("printing")
print(df)
