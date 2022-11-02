import tabula

# Second arg is the page # where the table is located
# Need Java for this to work
tab = tabula.read_pdf("weather.pdf", pages=2)
#tab = tabula.read_pdf("table_and_text.pdf", pages=1)

# tab is a list of length 1, with the only element being a pd DataFrame. tabula invokes pandas
print(tab)

#tab[0].to_csv("weather_table.csv", index=None)
#tab[0].to_csv("table_and_text.xlsx", index=None)