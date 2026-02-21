"""
Configuration file for Rent vs Buy Analysis Tool
"""

# Application Settings
DEBUG = True
PORT = 5000

# Default Values
DEFAULT_ANALYSIS_PERIOD = 10
DEFAULT_LOAN_TERM = 30
DEFAULT_INTEREST_RATE = 6.5

# Default Cost Rates (as percentages or fixed amounts)
DEFAULT_PROPERTY_TAX_RATE = 1.2  # % of home value
DEFAULT_MAINTENANCE_RATE = 1.0  # % of home value
DEFAULT_INSURANCE_RATE = 0.5  # % of home value
DEFAULT_HOA_FEES = 200  # Monthly
DEFAULT_CLOSING_COSTS = 3  # % of purchase price
DEFAULT_SELLING_COMMISSION = 6  # % of home value

# Market Assumptions
DEFAULT_HOME_APPRECIATION_RATE = 3.0  # % per year
DEFAULT_MARKET_RETURN_RATE = 7.0  # % per year
DEFAULT_RENT_INCREASE_RATE = 3.0  # % per year

# Example Scenarios
EXAMPLE_SCENARIOS = {
    'modest_home': {
        'purchase_price': 300000,
        'down_payment': 60000,
        'monthly_rent': 1200,
        'location': 'Midwest/South'
    },
    'median_home': {
        'purchase_price': 500000,
        'down_payment': 100000,
        'monthly_rent': 2000,
        'location': 'National Average'
    },
    'expensive_home': {
        'purchase_price': 1000000,
        'down_payment': 250000,
        'monthly_rent': 4000,
        'location': 'California/Northeast'
    }
}
