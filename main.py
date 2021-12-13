import pdfplumber
import pandas as pd
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--path', help='File path in pdf format')
args = parser.parse_args()

pdf = pdfplumber.open(args.path)
npages = pdf.pages[1:]

page0 = pdf.pages[0]

table = page0.extract_table()
df = pd.DataFrame(table[1:], columns=table[0])

for page in npages:
    t = page.extract_table()
    df = df.append(pd.DataFrame(t[0:], columns=table[0]), ignore_index=True)

df.to_csv(r'output.csv', index=False, header=True)