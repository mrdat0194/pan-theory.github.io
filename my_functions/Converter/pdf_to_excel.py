# Import Module
import tabula

# Read PDF File
# this contain a list
df = tabula.read_pdf("Test_system.pdf", pages=1)[0]

print(df)
# Convert into Excel File
df.to_excel('Test_system.xlsx')