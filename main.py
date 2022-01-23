# @author: Daniel Murillo Portuguez
import pandas as pd

from models.vehicle import Vehicle

# Add new transportation vehicle________________________________
toyota = Vehicle(345679, "Toyota", "Hilux", 1, "Pick Up",
                 3, 15000000, 400, "2/1/2019")

print(toyota.add_new_vehicle())
print()
print("Vehicle detail")
print(toyota.to_string())
print()
# ___________________________________________________________________________________________________________________


# __________________________________________________First_Query______________________________________________________
# The path of the Excel file
carSalesDataForReportsFile = "CarSalesDataForReports.xlsx"
# Read the Stock, Invoices and InvoiceLines sheets to save in 3 dataframes
dfStock = pd.read_excel(carSalesDataForReportsFile, sheet_name="Stock")
dfInvoices = pd.read_excel(carSalesDataForReportsFile, sheet_name="Invoices")
dfInvoiceLines = pd.read_excel(carSalesDataForReportsFile, sheet_name="InvoiceLines")

firstMerge = pd.merge(dfStock, dfInvoiceLines, on="StockID")
secondMerge = pd.merge(firstMerge, dfInvoices, on="InvoiceID")

q1_2015 = secondMerge.loc[(secondMerge['InvoiceDate'] >= '2015-01-01')
                          & (secondMerge['InvoiceDate'] < '2015-04-01')]

q3_2015 = secondMerge.loc[(secondMerge['InvoiceDate'] >= '2015-07-01')
                          & (secondMerge['InvoiceDate'] < '2015-10-01')]

print("Top 3 Car brands most sold During the first Quarter\n")
print(q1_2015['Make'].value_counts().head(3))
print()
print("Top 3 Car brands most sold During the third Quarter\n")
print(q3_2015['Make'].value_counts().head(3))

# _________________________________________________Second_Query______________________________________________________

dfColors = pd.read_excel(carSalesDataForReportsFile, sheet_name="Colors")

thirdMerge = pd.merge(secondMerge, dfColors, on='ColorID')
# ___________________________________________________________________________________________________________________
q1_2012 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2012-01-01') & (thirdMerge['InvoiceDate'] < '2012-04-01')]
q2_2012 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2012-04-01') & (thirdMerge['InvoiceDate'] < '2012-07-01')]
q3_2012 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2012-07-01') & (thirdMerge['InvoiceDate'] < '2012-10-01')]
q4_2012 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2012-10-01') & (thirdMerge['InvoiceDate'] < '2013-01-01')]

print()
print('Top 3 car color most sold during Q1 2012\n')
print(q1_2012['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q2 2012\n')
print(q2_2012['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q3 2012\n')
print(q3_2012['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q4 2012\n')
print(q4_2012['Color'].value_counts().head(3))

q1_2013 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2013-01-01') & (thirdMerge['InvoiceDate'] < '2013-04-01')]
q2_2013 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2013-04-01') & (thirdMerge['InvoiceDate'] < '2013-07-01')]
q3_2013 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2013-07-01') & (thirdMerge['InvoiceDate'] < '2013-10-01')]
q4_2013 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2013-10-01') & (thirdMerge['InvoiceDate'] < '2014-01-01')]

print()
print('Top 3 car color most sold during Q1 2013\n')
print(q1_2013['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q2 2013\n')
print(q2_2013['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q3 2013\n')
print(q3_2013['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q4 2013\n')
print(q4_2013['Color'].value_counts().head(3))

q1_2014 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2014-01-01') & (thirdMerge['InvoiceDate'] < '2014-04-01')]
q2_2014 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2014-04-01') & (thirdMerge['InvoiceDate'] < '2014-07-01')]
q3_2014 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2014-07-01') & (thirdMerge['InvoiceDate'] < '2014-10-01')]
q4_2014 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2014-10-01') & (thirdMerge['InvoiceDate'] < '2015-01-01')]

print()
print('Top 3 car color most sold during Q1 2014\n')
print(q1_2014['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q2 2014\n')
print(q2_2014['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q3 2014\n')
print(q3_2014['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q4 2014\n')
print(q4_2014['Color'].value_counts().head(3))

q1__2015 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2015-01-01') & (thirdMerge['InvoiceDate'] < '2015-04-01')]
q2_2015 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2015-04-01') & (thirdMerge['InvoiceDate'] < '2015-07-01')]
q3__2015 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2015-07-01') & (thirdMerge['InvoiceDate'] < '2015-10-01')]
q4_2015 = thirdMerge.loc[(thirdMerge['InvoiceDate'] >= '2015-10-01') & (thirdMerge['InvoiceDate'] < '2016-01-01')]

print()
print('Top 3 car color most sold during Q1 2015\n')
print(q1__2015['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q2 2015\n')
print(q2_2015['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q3 2015\n')
print(q3__2015['Color'].value_counts().head(3))
print()
print('Top 3 car color most sold during Q4 2015\n')
print(q4_2015['Color'].value_counts().head(3))

