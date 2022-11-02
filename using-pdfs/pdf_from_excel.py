import pandas as pd
from fpdf import FPDF

# Don't want to use pandas and iterrows for this, but format of dataframe is neat for this
# because it follows the df = list of dictionaries format, which is good fpr what we're doing here
df = pd.read_excel("animal_data.xlsx")
#print(df)

#wb = openpyxl.load_workbook("animal_data.xlsx")
#ws = wb.active

#for row in ws.iter_rows(values_only=True):
if __name__=="__main__":
    for index, row in df.iterrows():
        # row is a pd.series, think of that like a dict - row is the data for one animal
        #print("type row - ",type(row))
        pdf = FPDF(orientation="P", unit="pt", format="A4")
        pdf.add_page()

        pdf.set_font(family="Times", style="B", size=24)
        pdf.cell(w=0, h=50, txt=row["name"], align="C", ln=1)

        # After grabbing the title, we want evenly spaced identical font etc key pair values
        # so can just loop over col names in the series per row(animal)
        for column in df.columns[1:]:
            pdf.set_font(family='Times', style='B', size=14)
            pdf.cell(w=100, h=25, txt=f"{column.title()}:")
            pdf.set_font(family='Times', size=14)
            pdf.cell(w=100, h=25, txt=row[column], ln=1)


        pdf.output(f"{row['name']}.pdf")