from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(text):
    doc = SimpleDocTemplate("Financial_Report.pdf")
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("Financial Performance Report", styles['Title']))
    content.append(Spacer(1, 20))

    for line in text.split("\n"):
        content.append(Paragraph(line, styles["Normal"]))
        content.append(Spacer(1, 10))

    doc.build(content)