"""
Example usage scenarios for the Rent vs Buy Analysis Tool
Run this file to see various analysis examples
"""

from rent_vs_buy import RentVsBuyAnalysis, print_analysis_report


def scenario_1_modest_home():
    """Scenario 1: Modest home in the Midwest"""
    print("\n" + "=" * 80)
    print("SCENARIO 1: Modest Home in the Midwest")
    print("=" * 80)
    
    analysis = RentVsBuyAnalysis(
        purchase_price=300000,
        down_payment=60000,
        loan_term_years=30,
        annual_interest_rate=6.0
    )
    
    results = analysis.compare_scenarios(
        years=10,
        monthly_rent=1200,
        annual_market_return=7.0,
        annual_property_tax_rate=1.0,
        annual_maintenance_rate=1.0,
        annual_insurance_rate=0.4,
        annual_hoa=0,
        closing_costs_percent=3,
        annual_appreciation_rate=2.5,
        annual_rent_increase_rate=2.5
    )
    
    print_analysis_report(results)


def scenario_2_median_home():
    """Scenario 2: Median home with standard rates"""
    print("\n" + "=" * 80)
    print("SCENARIO 2: Median Home (National Average)")
    print("=" * 80)
    
    analysis = RentVsBuyAnalysis(
        purchase_price=500000,
        down_payment=100000,
        loan_term_years=30,
        annual_interest_rate=6.5
    )
    
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
    
    print_analysis_report(results)


def scenario_3_expensive_home():
    """Scenario 3: Expensive home in high-value area"""
    print("\n" + "=" * 80)
    print("SCENARIO 3: Expensive Home (California/Northeast)")
    print("=" * 80)
    
    analysis = RentVsBuyAnalysis(
        purchase_price=1000000,
        down_payment=250000,
        loan_term_years=30,
        annual_interest_rate=7.0
    )
    
    results = analysis.compare_scenarios(
        years=10,
        monthly_rent=4000,
        annual_market_return=7.0,
        annual_property_tax_rate=1.5,
        annual_maintenance_rate=1.2,
        annual_insurance_rate=0.6,
        annual_hoa=500,
        closing_costs_percent=3,
        annual_appreciation_rate=4.0,
        annual_rent_increase_rate=3.5
    )
    
    print_analysis_report(results)


def scenario_4_long_term_analysis():
    """Scenario 4: Long-term analysis (30 years)"""
    print("\n" + "=" * 80)
    print("SCENARIO 4: Long-term Analysis (30 Years)")
    print("=" * 80)
    
    analysis = RentVsBuyAnalysis(
        purchase_price=500000,
        down_payment=100000,
        loan_term_years=30,
        annual_interest_rate=6.5
    )
    
    results = analysis.compare_scenarios(
        years=30,
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
    
    print_analysis_report(results)


def scenario_5_high_appreciation():
    """Scenario 5: High home appreciation market"""
    print("\n" + "=" * 80)
    print("SCENARIO 5: High Home Appreciation Market")
    print("=" * 80)
    
    analysis = RentVsBuyAnalysis(
        purchase_price=500000,
        down_payment=100000,
        loan_term_years=30,
        annual_interest_rate=6.5
    )
    
    results = analysis.compare_scenarios(
        years=10,
        monthly_rent=2000,
        annual_market_return=7.0,
        annual_property_tax_rate=1.2,
        annual_maintenance_rate=1.0,
        annual_insurance_rate=0.5,
        annual_hoa=200,
        closing_costs_percent=3,
        annual_appreciation_rate=5.0,  # Higher appreciation
        annual_rent_increase_rate=3.0
    )
    
    print_analysis_report(results)


def scenario_6_low_down_payment():
    """Scenario 6: Low down payment scenario"""
    print("\n" + "=" * 80)
    print("SCENARIO 6: Low Down Payment (5%)")
    print("=" * 80)
    
    analysis = RentVsBuyAnalysis(
        purchase_price=400000,
        down_payment=20000,  # Only 5%
        loan_term_years=30,
        annual_interest_rate=7.0  # Higher rate for lower down payment
    )
    
    results = analysis.compare_scenarios(
        years=10,
        monthly_rent=1800,
        annual_market_return=7.0,
        annual_property_tax_rate=1.1,
        annual_maintenance_rate=0.9,
        annual_insurance_rate=0.5,
        annual_hoa=150,
        closing_costs_percent=3,
        annual_appreciation_rate=3.0,
        annual_rent_increase_rate=3.0
    )
    
    print_analysis_report(results)


if __name__ == "__main__":
    print("\n" + "=" * 80)
    print("RENT VS BUY ANALYSIS - EXAMPLE SCENARIOS")
    print("=" * 80)
    print("\nThis script demonstrates various housing decision scenarios")
    print("by showing different market conditions and personal situations.\n")
    
    # Run all scenarios
    scenario_1_modest_home()
    scenario_2_median_home()
    scenario_3_expensive_home()
    scenario_4_long_term_analysis()
    scenario_5_high_appreciation()
    scenario_6_low_down_payment()
    
    print("\n" + "=" * 80)
    print("END OF EXAMPLES")
    print("=" * 80)
    print("\nTo use the web interface, run: python app.py")
    print("Then open http://localhost:5000 in your browser\n")
