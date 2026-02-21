# Getting Started

This guide will help you set up and run the Rent vs Buy Analysis Tool.

## Quick Start (Web Application)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Run the Application
```bash
python app.py
```

### Step 3: Open in Browser
Navigate to: `http://localhost:5000`

That's it! Enter your parameters and click "Analyze Buy vs Rent"

---

## Running Examples

To see various analysis scenarios with sample data:

```bash
python examples.py
```

This will run 6 different scenarios including:
- Modest home in the Midwest
- Median home (national average)
- Expensive home in high-value areas
- Long-term 30-year analysis
- High appreciation market
- Low down payment scenario

---

## Using the Python Library Directly

For scripting or integration into other applications:

```python
from rent_vs_buy import RentVsBuyAnalysis, print_analysis_report

# Create an analysis object
analysis = RentVsBuyAnalysis(
    purchase_price=500000,
    down_payment=100000,
    loan_term_years=30,
    annual_interest_rate=6.5
)

# Run the comparison
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

# Print formatted report
print_analysis_report(results)

# Or access individual values
print(f"Recommendation: {results['recommendation']}")
print(f"Financial Advantage: ${results['financial_advantage']:,.2f}")
```

---

## Project Structure

```
Rent vs Buy/
├── rent_vs_buy.py          # Core analysis engine
├── app.py                  # Flask web application
├── config.py               # Configuration settings
├── examples.py             # Example scenarios
├── requirements.txt        # Python dependencies
├── README.md               # Full documentation
├── QUICKSTART.md          # This file
├── templates/
│   └── index.html          # Web interface
└── static/                 # CSS/JavaScript files (future)
```

---

## Key Features

✅ **Comprehensive Analysis**
- Complete financial comparison of buying vs renting
- Detailed cost breakdowns
- Home equity calculations

✅ **Flexible Parameters**
- Customize all assumptions
- Market-specific rates
- Personal circumstances

✅ **Multiple Interfaces**
- Web application (browser-based)
- Command-line (Python script)
- Library (for integration)

✅ **Easy to Use**
- Intuitive UI
- Pre-loaded defaults
- Clear recommendations

---

## Troubleshooting

### Port 5000 Already in Use
If port 5000 is already in use, modify `app.py`:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to 5001
```

### Dependencies Issues
Reinstall dependencies:
```bash
pip install --upgrade -r requirements.txt
```

### Python Version
Ensure you have Python 3.7 or higher:
```bash
python --version
```

---

## Next Steps

1. **Try the web application** - Best for interactive analysis
2. **Run examples.py** - See how different scenarios play out
3. **Customize parameters** - Adjust for your market and situation
4. **Share results** - Print or export your analysis

---

## Support

For questions or issues:
1. Check the README.md for detailed parameter explanations
2. Review the example scenarios in examples.py
3. Examine the source code in rent_vs_buy.py

---

Enjoy using the Rent vs Buy Analysis Tool! 🏠
