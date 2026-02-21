"""
Web interface for Rent vs Buy Analysis
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from rent_vs_buy import RentVsBuyAnalysis
import json
import os

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Render the main analysis page."""
    # Read HTML file directly (works with or without templates folder)
    html_path = os.path.join(os.path.dirname(__file__), 'index.html')
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        # Fallback if index.html is in templates folder
        html_path = os.path.join(os.path.dirname(__file__), 'templates', 'index.html')
        with open(html_path, 'r', encoding='utf-8') as f:
            return f.read()

@app.route('/api/analyze', methods=['POST'])
def analyze():
    """API endpoint for rent vs buy analysis."""
    try:
        data = request.json
        
        # Extract parameters
        purchase_price = float(data.get('purchase_price', 0))
        down_payment = float(data.get('down_payment', 0))
        monthly_rent = float(data.get('monthly_rent', 0))
        analysis_years = int(data.get('analysis_years', 10))
        
        # Mortgage parameters
        loan_term = int(data.get('loan_term_years', 30))
        interest_rate = float(data.get('annual_interest_rate', 6.5))
        
        # Ownership costs
        property_tax_rate = float(data.get('annual_property_tax_rate', 1.2))
        maintenance_rate = float(data.get('annual_maintenance_rate', 1.0))
        insurance_rate = float(data.get('annual_insurance_rate', 0.5))
        hoa = float(data.get('annual_hoa', 0.2))
        closing_costs = float(data.get('closing_costs_percent', 3))
        
        # Market parameters
        home_appreciation = float(data.get('annual_appreciation_rate', 3.0))
        market_return = float(data.get('annual_market_return', 7.0))
        rent_increase = float(data.get('annual_rent_increase_rate', 3.0))
        
        # Income and investment parameters
        monthly_income = float(data.get('monthly_income', 5000))
        annual_inflation = float(data.get('annual_inflation_rate', 2.5))
        monthly_investment_percentage = float(data.get('monthly_investment_percentage', 10.0))
        
        # Validate inputs
        if purchase_price <= 0 or down_payment <= 0 or monthly_rent <= 0:
            return jsonify({'error': 'All main parameters must be positive'}), 400
        
        if down_payment > purchase_price:
            return jsonify({'error': 'Down payment cannot exceed purchase price'}), 400
        
        # Create analysis
        analysis = RentVsBuyAnalysis(
            purchase_price=purchase_price,
            down_payment=down_payment,
            loan_term_years=loan_term,
            annual_interest_rate=interest_rate
        )
        
        # Run comparison
        results = analysis.compare_scenarios(
            years=analysis_years,
            monthly_rent=monthly_rent,
            annual_market_return=market_return,
            annual_property_tax_rate=property_tax_rate,
            annual_maintenance_rate=maintenance_rate,
            annual_insurance_rate=insurance_rate,
            annual_hoa=hoa,
            closing_costs_percent=closing_costs,
            annual_appreciation_rate=home_appreciation,
            annual_rent_increase_rate=rent_increase,
            monthly_income=monthly_income,
            annual_inflation_rate=annual_inflation,
            monthly_investment_percentage=monthly_investment_percentage
        )
        
        # Debug: Print results
        print(f"DEBUG - buy_net_cost: {results['buy_net_cost']}")
        print(f"DEBUG - rent_net_position: {results['rent_net_position']}")
        print(f"DEBUG - rent_net_cost: {results['rent_net_cost']}")
        print(f"DEBUG - monthly_costs exists? {'monthly_costs' in results}")
        if 'monthly_costs' in results:
            print(f"DEBUG - monthly_costs keys: {results['monthly_costs'].keys()}")
            print(f"DEBUG - buy_monthly_investments: {results['monthly_costs'].get('buy_monthly_investments', 'MISSING')}")
            print(f"DEBUG - rent_monthly_investments: {results['monthly_costs'].get('rent_monthly_investments', 'MISSING')}")
        print(f"DEBUG - yearly_growth exists? {'yearly_growth' in results}")
        if 'yearly_growth' in results:
            print(f"DEBUG - yearly_growth keys: {results['yearly_growth'].keys()}")
            print(f"DEBUG - yearly_growth years: {results['yearly_growth']['years']}")
            print(f"DEBUG - yearly_growth home_equity type: {type(results['yearly_growth']['home_equity_after_sales'])}")
            print(f"DEBUG - yearly_growth home_equity: {results['yearly_growth']['home_equity_after_sales']}")
            print(f"DEBUG - yearly_growth investment_growth: {results['yearly_growth']['investment_growth']}")
        else:
            print(f"DEBUG - Available keys: {results.keys()}")
        
        # Format results for JSON response
        return jsonify({
            'success': True,
            'results': {
                'recommendation': results['recommendation'],
                'advantage_description': results['advantage_description'],
                'financial_advantage': round(results['financial_advantage'], 2),
                'buy_net_cost': round(results['buy_net_cost'], 2),
                'buy_net_position': round(results['buying']['net_position'], 2),
                'rent_net_cost': round(results['rent_net_cost'], 2),
                'rent_net_position': round(results['rent_net_position'], 2),
                'buying': {
                    'down_payment': round(results['buying']['initial_down_payment'], 2),
                    'closing_costs': round(results['buying']['closing_costs'], 2),
                    'monthly_mortgage': round(results['buying']['monthly_mortgage_payment'], 2),
                    'total_mortgage_payments': round(results['buying']['total_mortgage_payments'], 2),
                    'total_interest_paid': round(results['buying']['total_interest_paid'], 2),
                    'total_property_tax': round(results['buying']['total_property_tax'], 2),
                    'total_maintenance': round(results['buying']['total_maintenance'], 2),
                    'total_insurance': round(results['buying']['total_insurance'], 2),
                    'total_hoa': round(results['buying']['total_hoa'], 2),
                    'selling_costs': round(results['buying']['selling_costs'], 2),
                    'total_costs': round(results['buying']['total_costs'], 2),
                    'final_home_value': round(results['buying']['final_home_value'], 2),
                    'home_equity': round(results['buying']['home_equity'], 2),
                },
                'renting': {
                    'total_rent_paid': round(results['renting']['total_rent_paid'], 2),
                    'investment_amount': round(results['renting']['investment_amount'], 2),
                    'down_payment': round(down_payment, 2),
                },
                'monthly_costs': {
                    'years': results['monthly_costs']['years'],
                    'buy_costs': results['monthly_costs']['buy_costs'],
                    'rent_costs': results['monthly_costs']['rent_costs'],
                    'monthly_income': results['monthly_costs']['monthly_income'],
                    'buy_monthly_investments': results['monthly_costs']['buy_monthly_investments'],
                    'rent_monthly_investments': results['monthly_costs']['rent_monthly_investments']
                },
                'yearly_growth': {
                    'years': results['yearly_growth']['years'],
                    'home_equity_after_sales': results['yearly_growth']['home_equity_after_sales'],
                    'investment_growth': results['yearly_growth']['investment_growth']
                }
            }
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/defaults', methods=['GET'])
def get_defaults():
    """Return default values for the form."""
    return jsonify({
        'purchase_price': 500000,
        'down_payment': 100000,
        'monthly_rent': 2000,
        'analysis_years': 10,
        'loan_term_years': 30,
        'annual_interest_rate': 6.5,
        'annual_property_tax_rate': 1.2,
        'annual_maintenance_rate': 1.0,
        'annual_insurance_rate': 0.5,
        'annual_hoa': 0.2,
        'closing_costs_percent': 3,
        'annual_appreciation_rate': 3.0,
        'annual_market_return': 7.0,
        'annual_rent_increase_rate': 3.0,
        'monthly_income': 5000,
        'annual_inflation_rate': 2.5,
        'monthly_investment_percentage': 10.0
    })

if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
