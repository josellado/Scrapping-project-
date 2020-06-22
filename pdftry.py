from fpdf import FPDF

def creaPDF():
    pdf = FPDF('P','mm','A4')
    pdf.add_page()
    pdf.set_xy(0, 0)
    pdf.set_font('arial', 'B', 12)
    pdf.cell(60)
    pdf.cell(75, 10, "ALBUS DUMBLEDORE  ARMY", 0, 2, 'C')
    pdf.cell(90, 10, " ", 0, 2, 'C')
    pdf.cell(-40)
    
    pdf.output("archivo.pdf")
    pdf.output("src/reporteparaenviar.pdf", "F")
    
