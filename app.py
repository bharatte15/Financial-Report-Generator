from src.analysis import analyze_data
from src.insights import generate_insights
from src.report import create_pdf

# Load file
file = "data/Financial Sample.xlsx"

# Analyze
data = analyze_data(file)

# Generate insights
insights = generate_insights(data)

print(insights)

# Generate PDF
create_pdf(insights)