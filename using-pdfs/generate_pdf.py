from fpdf import FPDF

# pt is the unit used for the text
# This initialises a pdf but its empty, we need to add pages to it
pdf = FPDF(orientation="P", unit="pt", format="A4")

# intuitively, we add from top to bottom
pdf.add_page()
# height & weight in pt, try keep dimension ratio same as original image or it'll look distorted
# x is positional arg
pdf.image('reptar.jpg', w=80, h=50, x=500)


# Always need to set the font before you add a cell if it's gonna be text
pdf.set_font(family="Times", style="B", size=24)
# add text. The pdf as a whole is based on cells, and you add text etc within a given cell you've made
#similar to figure idea of matplotlib where you make a figure and then draw axes, pdf=figure, cell=axes
# h & w dictate the size of the cell and we choose where to put it by alignment. w=0 counter-intuitively
# means "use the whole cell width"
# border shows us what we've outlined and ln is for a linebreak after this cell
pdf.cell(w=0, h=50, txt="Reptar from Rugrats", align="C", border=1, ln=1)

# add more cells
pdf.set_font(family="Times", style="B", size=14)
pdf.cell(w=0, h=15, txt="Description", ln=1, border=1)


pdf.set_font(family="Times", size=12)
txt_1 = """Sample text giving Reptars background. He is a dinosaur.
The Reptar Wagon appeared in several episodes of Rugrats following the release of The Rugrats Movie 
once again voiced by Busta Rhymes through archive recordings from the film.
"""
# need to use multicell for text wrapping when you have a lot of text, it lets it wrap the lines in the
# cells
pdf.multi_cell(w=0, h=15, txt=txt_1, border=1)

# Remember cells start where others leave off, so need to adjust the height and width accordingly
# No ln and a width of 200 lets them be on the same line - mak sure width is long enough for text or it
# will overlap. If width was 0 here, it'd span from vertical margin on one side to the other, so
# The attitude bit would start just where that margin ends, ie at edge of file and get cut off
pdf.set_font(family="Times", size=14)
pdf.cell(w=200, h=15, txt="Colours: Green, Blue", border=1)

pdf.set_font(family="Times", size=14)
pdf.cell(w=100, h=15, txt="Attitude: Chaotic", ln=1, border=1)

# Some good spacing
pdf.set_font(family="Times", size=14)
pdf.cell(w=50, h=25, txt="Likes: ")
pdf.set_font(family="Times", size=14)
pdf.cell(w=50, h=25, txt="Destruction", ln=1)

pdf.set_font(family="Times", size=14)
pdf.cell(w=50, h=25, txt="Hates: ")
pdf.set_font(family="Times", size=14)
pdf.cell(w=50, h=25, txt="The French", ln=1)

if __name__ == "__main__":
    # Output the pdf we've constructed
    pdf.output("mypdf.pdf")