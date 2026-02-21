# Rent vs Buy Analysis Tool

A comprehensive financial analysis tool to help you make an informed decision between buying and renting a house.

## Features

- **Complete Financial Analysis**: Compares the net cost of buying vs the position from renting and investing
- **Detailed Breakdown**: Shows mortgage payments, property taxes, maintenance, insurance, and more
- **Market Assumptions**: Considers home appreciation and investment market returns
- **Interactive Web Interface**: User-friendly dashboard for easy analysis
- **Command-line Interface**: Run analysis directly from Python for scripting

## What the Tool Calculates

### Buying Scenario
- Monthly mortgage payments with amortization
- Property taxes, maintenance, and insurance costs
- HOA fees and closing costs
- Home appreciation over time
- Home equity and selling costs
- Total net cost of ownership

### Renting Scenario
- Total rent paid over analysis period with annual increases
- Investment growth of down payment in the market
- Net financial position compared to buying

## Installation

1. **Clone or download the repository**
   ```bash
   cd "Rent vs Buy"
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Web Interface (Recommended)

1. Start the Flask application:
   ```bash
   python app.py
   ```

2. Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter your parameters and click "Analyze Buy vs Rent"

### Command-line Interface

Run the Python script directly with your own parameters:

```python
from rent_vs_buy import RentVsBuyAnalysis, print_analysis_report

# Create analysis
analysis = RentVsBuyAnalysis(
    purchase_price=500000,
    down_payment=100000,
    loan_term_years=30,
    annual_interest_rate=6.5
)

# Run comparison
results = analysis.compare_scenarios(
    years=10,
    monthly_rent=2000,
    annual_market_return=7.0,
    annual_property_tax_rate=1.2,
    annual_maintenance_rate=1.0,
    annual_insurance_rate=0.5,
    annual_hoa=200,
    closing_costs_percent=3,
    annual_appreciation_rate=3.0,
    annual_rent_increase_rate=3.0
)

# Print report
print_analysis_report(results)
```

## Default Assumptions

- **Loan Term**: 30 years
- **Interest Rate**: 6.5%
- **Property Tax Rate**: 1.2% of home value annually
- **Maintenance**: 1.0% of home value annually
- **Insurance**: 0.5% of home value annually
- **HOA Fees**: $200/month
- **Closing Costs**: 3% of purchase price
- **Home Appreciation**: 3% annually
- **Market Return**: 7% annually
- **Rent Increase**: 3% annually
- **Realtor Commission**: 6% (selling costs)

## Input Parameters

### Basic Information
- **Purchase Price**: Total price of the house you're considering
- **Down Payment**: Available cash for down payment
- **Monthly Rent**: Comparable rental price in the area
- **Analysis Period**: Years to analyze (typically 10-30)

### Mortgage Terms
- **Loan Term**: Length of mortgage (typically 15 or 30 years)
- **Interest Rate**: Annual mortgage interest rate

### Ownership Costs
- **Property Tax Rate**: Annual property tax as % of home value
- **Maintenance Rate**: Annual maintenance costs as % of home value
- **Insurance Rate**: Annual insurance as % of home value
- **HOA Fees**: Annual HOA charges if applicable
- **Closing Costs**: One-time costs as % of purchase price

### Market Assumptions
- **Home Appreciation Rate**: Expected annual increase in home value
- **Market Return Rate**: Expected annual investment returns
- **Rent Increase Rate**: Expected annual increase in rent

## Output

The analysis provides:

1. **Recommendation**: Clear advice on whether to BUY or RENT
2. **Financial Advantage**: Dollar amount showing which option is better
3. **Detailed Costs**: Breakdown of all expenses for buying
4. **Home Equity**: Net position after home appreciation and sale
5. **Investment Returns**: Growth of down payment if invested instead
6. **Comparison**: Side-by-side financial comparison

## Example Analysis

```
Purchase Price: $500,000
Down Payment: $100,000
Monthly Rent: $2,000
Analysis Period: 10 years

Results:
- Buying Net Cost: $187,465
- Renting + Investing Position: $156,890
- Recommendation: RENT (saves $30,575)
```

## Key Insights

The tool helps you understand:
- **Break-even Analysis**: When does buying become better than renting?
- **Cost of Capital**: How much of your down payment gets locked in equity?
- **Market Impact**: How sensitive is the decision to appreciation rates?
- **True Cost of Ownership**: All hidden costs of homeownership

## Important Notes

- This tool provides financial analysis only, not investment advice
- Actual costs vary based on location, market conditions, and personal circumstances
- Consider non-financial factors: stability, flexibility, lifestyle preferences
- Consult with a financial advisor for personalized guidance
- Tax implications are not included in this analysis

## Technical Details

- **Language**: Python 3
- **Framework**: Flask (web interface)
- **Calculation Method**: Standard mortgage amortization formulas
- **Browser**: Chrome, Firefox, Safari, Edge (modern versions)

## License

This project is open source and available for personal and educational use.
