import pandas as pd
import numpy as np
from functools import reduce

file = "DAB Project - Excel File.xlsx"

gdp = pd.read_excel(file, sheet_name="GDP per capita")
electricity = pd.read_excel(file, sheet_name="Electricity Consumption")
trade = pd.read_excel(file, sheet_name="Trade%GDP")
fdi = pd.read_excel(file, sheet_name="FDI%GDP")
mobile = pd.read_excel(file, sheet_name="Mobile Subscriptions")

gdp = gdp[["Country", "GDP per capita"]]
electricity = electricity[["Country", "Electricity Consumption"]]
trade = trade[["Country", "Trade%GDP"]]
fdi = fdi[["Country", "FDI%GDP"]]
mobile = mobile[["Country", "Mobile Subscriptions"]]

dfs = [gdp, electricity, trade, fdi, mobile]

final = reduce(
    lambda left, right: pd.merge(left, right, on="Country", how="inner"),
    dfs
)

final = final.dropna()

final = final[~final["Country"].str.contains("income|Asia|Africa|Europe|America|Arab|Pacific|Caribbean|OECD|IBRD|IDA|Euro|dividend", case=False, na=False)]

print(final)

with pd.ExcelWriter(file, mode="a", engine="openpyxl") as writer:
    final.to_excel(writer, sheet_name="Final Sheet", index=False)