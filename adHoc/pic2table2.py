import pandas as pd
import easyocr

imgp = "photo_2024.jpg"
reader = easyocr.Reader(['en'])
results = reader.readtext(imgp)
tabledata = []
for (bbox, text, prob) in results:
    tabledata.append([text])
df = pd.DataFrame(tabledata)
output_file = "easyocr.xlsx"
df.to_excel(output_file, index=False, header=False)