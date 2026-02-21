# API Documentation

## Rent vs Buy Analysis Tool - Complete API Reference

---

## Core Class: RentVsBuyAnalysis

The main class that handles all rent vs buy analysis calculations.

### Constructor

```python
RentVsBuyAnalysis(purchase_price, down_payment, loan_term_years=30, annual_interest_rate=6.5)
```

#### Parameters
- `purchase_price` (float): Total purchase price of the house
- `down_payment` (float): Available cash for down payment
- `loan_term_years` (int, optional): Mortgage term in years (default: 30)
- `annual_interest_rate` (float, optional): Annual mortgage interest rate as percentage (default: 6.5)

#### Example
```python
analysis = RentVsBuyAnalysis(
    purchase_price=500000,
    down_payment=100000,
    loan_term_years=30,
    annual_interest_rate=6.5
)
```

---

## Methods

### calculate_monthly_mortgage_payment()

Calculates the monthly mortgage payment using standard amortization formula.

```python
payment = analysis.calculate_monthly_mortgage_payment()
```

**Returns**: `float` - Monthly payment amount

**Formula Used**: 
```
P = L[c(1+c)^n]/[(1+c)^n-1]
where:
  P = Monthly payment
  L = Loan amount
  c = Monthly interest rate
  n = Number of payments
```

**Example**
```python
# For $400k loan at 6.5% for 30 years
monthly_payment = analysis.calculate_monthly_mortgage_payment()
# Returns approximately $2,529
```

---

### calculate_buying_costs()

Comprehensive calculation of all buying-related costs over specified years.

```python
costs = analysis.calculate_buying_costs(
    years,
    annual_property_tax_rate=1.2,
    annual_maintenance_rate=1.0,
    annual_insurance_rate=0.5,
    annual_hoa=0,
    closing_costs_percent=3,
    annual_appreciation_rate=3.0
)
```

#### Parameters
- `years` (int): Analysis period in years
- `annual_property_tax_rate` (float, optional): Property tax as % of home value (default: 1.2)
- `annual_maintenance_rate` (float, optional): Maintenance as % of home value (default: 1.0)
- `annual_insurance_rate` (float, optional): Insurance as % of home value (default: 0.5)
- `annual_hoa` (float, optional): Annual HOA fees in dollars (default: 0)
- `closing_costs_percent` (float, optional): Closing costs as % of purchase (default: 3)
- `annual_appreciation_rate` (float, optional): Annual home appreciation % (default: 3.0)

#### Returns: Dictionary with keys
- `initial_down_payment`: Down payment amount
- `closing_costs`: One-time closing costs
- `total_mortgage_payments`: Sum of all mortgage payments
- `total_property_tax`: Sum of all property taxes
- `total_maintenance`: Sum of all maintenance costs
- `total_insurance`: Sum of all insurance premiums
- `total_hoa`: Sum of all HOA fees
- `selling_costs`: Estimated selling/realtor costs
- `total_costs`: Total cash outflow
- `final_home_value`: Home value after appreciation
- `remaining_mortgage_balance`: Unpaid mortgage balance
- `home_equity`: Net equity after sale
- `net_cost`: Total cost minus equity (true cost of buying)
- `monthly_mortgage_payment`: Monthly mortgage payment

#### Example
```python
costs = analysis.calculate_buying_costs(
    years=10,
    annual_property_tax_rate=1.2,
    annual_maintenance_rate=1.0,
    annual_insurance_rate=0.5,
    annual_hoa=200,
    closing_costs_percent=3,
    annual_appreciation_rate=3.0
)

print(f"Net cost of buying: ${costs['net_cost']:,.2f}")
print(f"Monthly mortgage: ${costs['monthly_mortgage_payment']:,.2f}")
```

---

### calculate_investment_returns()

Calculates growth of down payment if invested instead of buying.

```python
returns = analysis.calculate_investment_returns(
    years,
    annual_return_rate=7.0
)
```

#### Parameters
- `years` (int): Investment period in years
- `annual_return_rate` (float, optional): Expected annual return % (default: 7.0)

#### Returns: Dictionary with keys
- `initial_investment`: Initial down payment
- `final_amount`: Final value after growth
- `total_return`: Profit from investment
- `annual_return_rate`: Return rate used

#### Example
```python
# $100k invested at 7% annually for 10 years
returns = analysis.calculate_investment_returns(years=10, annual_return_rate=7.0)
print(f"Investment grows to: ${returns['final_amount']:,.2f}")
print(f"Profit: ${returns['total_return']:,.2f}")
```

---

### calculate_renting_costs()

Calculates total renting costs and investment growth over years.

```python
costs = analysis.calculate_renting_costs(
    years,
    monthly_rent,
    annual_rent_increase_rate=3.0
)
```

#### Parameters
- `years` (int): Renting period in years
- `monthly_rent` (float): Initial monthly rent
- `annual_rent_increase_rate` (float, optional): Annual rent increase % (default: 3.0)

#### Returns: Dictionary with keys
- `total_rent_paid`: Sum of all rent payments
- `investment_from_down_payment`: Down payment invested and grown
- `total_outflow`: Total cash paid out
- `net_position`: Investment value minus rent paid

#### Example
```python
renting = analysis.calculate_renting_costs(
    years=10,
    monthly_rent=2000,
    annual_rent_increase_rate=3.0
)

print(f"Total rent paid: ${renting['total_rent_paid']:,.2f}")
print(f"Net position: ${renting['net_position']:,.2f}")
```

---

### calculate_remaining_mortgage_balance()

Calculates unpaid mortgage balance after specified years.

```python
balance = analysis.calculate_remaining_mortgage_balance(years)
```

#### Parameters
- `years` (int): Years into the mortgage

#### Returns: `float` - Remaining unpaid balance

#### Example
```python
# After 10 years of a 30-year mortgage
balance = analysis.calculate_remaining_mortgage_balance(10)
print(f"Remaining balance: ${balance:,.2f}")
```

---

### compare_scenarios()

Master method that compares all aspects of buying vs renting.

```python
results = analysis.compare_scenarios(
    years,
    monthly_rent,
    annual_market_return=7.0,
    annual_property_tax_rate=1.2,
    annual_maintenance_rate=1.0,
    annual_insurance_rate=0.5,
    annual_hoa=0,
    closing_costs_percent=3,
    annual_appreciation_rate=3.0,
    annual_rent_increase_rate=3.0
)
```

#### Parameters
All parameters from `calculate_buying_costs()` plus:
- `monthly_rent` (float): Initial monthly rent
- `annual_market_return` (float, optional): Expected market return % (default: 7.0)

#### Returns: Dictionary with keys
- `analysis_period_years`: Number of years analyzed
- `buying`: Dict with buying scenario details (see `calculate_buying_costs()`)
- `renting`: Dict with renting scenario details (see `calculate_renting_costs()`)
- `financial_advantage`: Positive means buying is better, negative means renting is better
- `buy_net_cost`: Net cost of buying
- `rent_net_position`: Net position from renting
- `recommendation`: 'BUY' or 'RENT'
- `advantage_amount`: Absolute value of financial advantage
- `advantage_description`: Human-readable comparison

#### Example
```python
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

print(f"Recommendation: {results['recommendation']}")
print(f"Advantage: {results['advantage_description']}")
```

---

## Utility Functions

### print_analysis_report()

Prints a formatted analysis report to console.

```python
from rent_vs_buy import print_analysis_report

print_analysis_report(results)
```

#### Parameters
- `analysis_results` (dict): Results dictionary from `compare_scenarios()`

#### Example
```python
results = analysis.compare_scenarios(years=10, monthly_rent=2000)
print_analysis_report(results)
```

---

## Web API Endpoints

### POST /api/analyze

Performs analysis via HTTP request.

#### Request Body
```json
{
    "purchase_price": 500000,
    "down_payment": 100000,
    "monthly_rent": 2000,
    "analysis_years": 10,
    "loan_term_years": 30,
    "annual_interest_rate": 6.5,
    "annual_property_tax_rate": 1.2,
    "annual_maintenance_rate": 1.0,
    "annual_insurance_rate": 0.5,
    "annual_hoa": 200,
    "closing_costs_percent": 3,
    "annual_appreciation_rate": 3.0,
    "annual_market_return": 7.0,
    "annual_rent_increase_rate": 3.0
}
```

#### Response (Success)
```json
{
    "success": true,
    "results": {
        "recommendation": "BUY",
        "advantage_description": "Buying is better by $30,575",
        "financial_advantage": 30575,
        "buy_net_cost": 156890,
        "rent_net_position": 187465,
        "buying": { ... },
        "renting": { ... }
    }
}
```

#### Response (Error)
```json
{
    "error": "Down payment cannot exceed purchase price"
}
```

### GET /api/defaults

Returns default parameter values.

#### Response
```json
{
    "purchase_price": 500000,
    "down_payment": 100000,
    "monthly_rent": 2000,
    "analysis_years": 10,
    ...
}
```

---

## Example Workflows

### Complete Analysis Workflow

```python
from rent_vs_buy import RentVsBuyAnalysis, print_analysis_report

# Initialize
analysis = RentVsBuyAnalysis(
    purchase_price=500000,
    down_payment=100000,
    loan_term_years=30,
    annual_interest_rate=6.5
)

# Run analysis
results = analysis.compare_scenarios(
    years=10,
    monthly_rent=2000
)

# Display results
print_analysis_report(results)

# Access specific values
if results['recommendation'] == 'BUY':
    print(f"Buying saves ${results['financial_advantage']:,.2f}")
else:
    print(f"Renting saves ${abs(results['financial_advantage']):,.2f}")
```

### Break-even Analysis

```python
# Find the break-even year
for year in range(1, 31):
    results = analysis.compare_scenarios(years=year, monthly_rent=2000)
    if results['recommendation'] == 'BUY':
        print(f"Buying becomes better after {year} years")
        break
```

### Sensitivity Analysis

```python
# Test different appreciation rates
for appreciation in [0, 2, 3, 4, 5]:
    results = analysis.compare_scenarios(
        years=10,
        monthly_rent=2000,
        annual_appreciation_rate=appreciation
    )
    print(f"At {appreciation}% appreciation: {results['recommendation']}")
```

---

## Error Handling

The library validates inputs and raises exceptions for invalid data:

```python
try:
    analysis = RentVsBuyAnalysis(
        purchase_price=500000,
        down_payment=600000  # Invalid: exceeds purchase price
    )
except ValueError as e:
    print(f"Error: {e}")
```

Web API returns HTTP error codes:
- `400`: Invalid input parameters
- `500`: Server error during calculation

---

## Performance Notes

- Calculations are fast (typically < 100ms)
- Suitable for interactive web applications
- No external dependencies for core calculations (Flask required for web API only)

---

## Unit Tests

Run the test suite:
```bash
python -m unittest test_rent_vs_buy.py -v
```

---

## Version Information

- **Python**: 3.7+
- **Dependencies**: Flask 3.0.0+ (web API only)
- **License**: Open Source
