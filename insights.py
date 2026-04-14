def generate_insights(data):

    return f"""
EXECUTIVE SUMMARY:
The company generated total sales of {data['total_sales']:.2f} with a profit margin of {data['profit_margin']:.2f}%.
The top performing country is {data['top_country']} and the most profitable product is {data['top_product']}.

KEY RISKS:
- Dependency on a single region
- Fluctuating profit margins

GROWTH OPPORTUNITIES:
- Expand high-performing products
- Improve underperforming months

RECOMMENDATIONS:
- Optimize pricing
- Reduce discounts
- Focus on high-margin products
"""