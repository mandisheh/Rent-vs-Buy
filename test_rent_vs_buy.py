"""
Unit tests for the Rent vs Buy Analysis Tool
"""

import unittest
from rent_vs_buy import RentVsBuyAnalysis


class TestRentVsBuyAnalysis(unittest.TestCase):
    """Test cases for RentVsBuyAnalysis class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.analysis = RentVsBuyAnalysis(
            purchase_price=500000,
            down_payment=100000,
            loan_term_years=30,
            annual_interest_rate=6.5
        )
    
    def test_initialization(self):
        """Test that analysis initializes with correct values"""
        self.assertEqual(self.analysis.purchase_price, 500000)
        self.assertEqual(self.analysis.down_payment, 100000)
        self.assertEqual(self.analysis.loan_amount, 400000)
        self.assertEqual(self.analysis.num_payments, 360)
    
    def test_monthly_mortgage_payment(self):
        """Test monthly mortgage calculation"""
        payment = self.analysis.calculate_monthly_mortgage_payment()
        # Expected payment for $400k at 6.5% for 30 years is approximately $2,529
        self.assertAlmostEqual(payment, 2529, delta=10)
    
    def test_zero_interest_rate(self):
        """Test mortgage calculation with 0% interest"""
        analysis = RentVsBuyAnalysis(
            purchase_price=300000,
            down_payment=60000,
            loan_term_years=30,
            annual_interest_rate=0
        )
        payment = analysis.calculate_monthly_mortgage_payment()
        # Payment should be loan_amount / num_payments = 240000 / 360
        expected = 240000 / 360
        self.assertAlmostEqual(payment, expected, delta=0.01)
    
    def test_remaining_mortgage_balance_at_start(self):
        """Test remaining balance at start is nearly the loan amount"""
        balance = self.analysis.calculate_remaining_mortgage_balance(0)
        self.assertAlmostEqual(balance, self.analysis.loan_amount, delta=1)
    
    def test_remaining_mortgage_balance_at_end(self):
        """Test remaining balance at end of loan is zero"""
        balance = self.analysis.calculate_remaining_mortgage_balance(30)
        self.assertAlmostEqual(balance, 0, delta=10)
    
    def test_buying_costs_structure(self):
        """Test that buying costs returns all required fields"""
        costs = self.analysis.calculate_buying_costs(10)
        required_fields = [
            'initial_down_payment', 'closing_costs', 'total_mortgage_payments',
            'total_property_tax', 'total_maintenance', 'total_insurance',
            'total_hoa', 'selling_costs', 'total_costs', 'final_home_value',
            'remaining_mortgage_balance', 'home_equity', 'net_cost',
            'monthly_mortgage_payment'
        ]
        for field in required_fields:
            self.assertIn(field, costs)
            self.assertIsInstance(costs[field], (int, float))
    
    def test_investment_returns(self):
        """Test investment return calculations"""
        returns = self.analysis.calculate_investment_returns(10, annual_return_rate=7.0)
        
        # Investment should grow: initial * (1 + rate)^years
        initial = 100000
        rate = 0.07
        years = 10
        expected = initial * ((1 + rate) ** years)
        
        self.assertAlmostEqual(returns['final_amount'], expected, delta=100)
        self.assertEqual(returns['initial_investment'], 100000)
    
    def test_renting_costs_structure(self):
        """Test that renting costs returns all required fields"""
        costs = self.analysis.calculate_renting_costs(10, monthly_rent=2000)
        required_fields = [
            'total_rent_paid', 'investment_from_down_payment',
            'total_outflow', 'net_position'
        ]
        for field in required_fields:
            self.assertIn(field, costs)
            self.assertIsInstance(costs[field], (int, float))
    
    def test_renting_rent_accumulation(self):
        """Test that renting costs accumulate rent with increases"""
        costs = self.analysis.calculate_renting_costs(
            years=1,
            monthly_rent=1000,
            annual_rent_increase_rate=0
        )
        # 1 year of $1000/month rent = $12000
        self.assertAlmostEqual(costs['total_rent_paid'], 12000, delta=1)
    
    def test_comparison_scenario_structure(self):
        """Test comparison returns all required fields"""
        results = self.analysis.compare_scenarios(
            years=10,
            monthly_rent=2000
        )
        required_fields = [
            'analysis_period_years', 'buying', 'renting',
            'financial_advantage', 'buy_net_cost', 'rent_net_position',
            'recommendation', 'advantage_amount', 'advantage_description'
        ]
        for field in required_fields:
            self.assertIn(field, results)
        
        # Recommendation should be BUY or RENT
        self.assertIn(results['recommendation'], ['BUY', 'RENT'])
    
    def test_home_value_appreciation(self):
        """Test that home value appreciates correctly"""
        costs_0pct = self.analysis.calculate_buying_costs(
            10, annual_appreciation_rate=0
        )
        costs_3pct = self.analysis.calculate_buying_costs(
            10, annual_appreciation_rate=3.0
        )
        
        # Home value should be higher with appreciation
        self.assertGreater(
            costs_3pct['final_home_value'],
            costs_0pct['final_home_value']
        )
    
    def test_negative_financial_advantage_rent(self):
        """Test scenario where renting is better (negative advantage)"""
        # Use low home appreciation and high investment returns
        results = self.analysis.compare_scenarios(
            years=5,
            monthly_rent=1000,
            annual_market_return=15.0,  # Very high returns
            annual_appreciation_rate=0,  # No appreciation
            annual_rent_increase_rate=0
        )
        
        # In this case, renting should be better
        if results['recommendation'] == 'RENT':
            self.assertLess(results['financial_advantage'], 0)
    
    def test_positive_financial_advantage_buy(self):
        """Test scenario where buying is better (positive advantage)"""
        results = self.analysis.compare_scenarios(
            years=20,
            monthly_rent=3000,  # High rent
            annual_market_return=5.0,  # Low investment returns
            annual_appreciation_rate=5.0,  # High appreciation
            annual_rent_increase_rate=5.0  # High rent increase
        )
        
        # In this case, buying should typically be better
        if results['recommendation'] == 'BUY':
            self.assertGreater(results['financial_advantage'], 0)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and boundary conditions"""
    
    def test_short_analysis_period(self):
        """Test with very short analysis period"""
        analysis = RentVsBuyAnalysis(500000, 100000)
        results = analysis.compare_scenarios(years=1, monthly_rent=2000)
        self.assertEqual(results['analysis_period_years'], 1)
    
    def test_long_analysis_period(self):
        """Test with very long analysis period (50 years)"""
        analysis = RentVsBuyAnalysis(500000, 100000)
        results = analysis.compare_scenarios(years=50, monthly_rent=2000)
        self.assertEqual(results['analysis_period_years'], 50)
    
    def test_high_down_payment(self):
        """Test with high down payment (80%)"""
        analysis = RentVsBuyAnalysis(500000, 400000)
        payment = analysis.calculate_monthly_mortgage_payment()
        # Should have very low monthly payment
        self.assertLess(payment, 500)
    
    def test_zero_hoa_fees(self):
        """Test with zero HOA fees"""
        analysis = RentVsBuyAnalysis(500000, 100000)
        costs = analysis.calculate_buying_costs(10, annual_hoa=0)
        self.assertEqual(costs['total_hoa'], 0)
    
    def test_zero_rent_increase(self):
        """Test with zero rent increase rate"""
        analysis = RentVsBuyAnalysis(500000, 100000)
        costs = analysis.calculate_renting_costs(
            years=3,
            monthly_rent=2000,
            annual_rent_increase_rate=0
        )
        # Total rent should be exactly 2000 * 12 * 3 = 72000
        self.assertAlmostEqual(costs['total_rent_paid'], 72000, delta=1)


class TestCalculationAccuracy(unittest.TestCase):
    """Test mathematical accuracy of calculations"""
    
    def test_mortgage_amortization(self):
        """Test that mortgage amortization is accurate"""
        analysis = RentVsBuyAnalysis(
            purchase_price=300000,
            down_payment=60000,
            loan_term_years=30,
            annual_interest_rate=6.0
        )
        
        # Calculate total paid over life of loan
        payment = analysis.calculate_monthly_mortgage_payment()
        total_paid = payment * 360
        
        # Total interest paid should be positive
        interest_paid = total_paid - 240000
        self.assertGreater(interest_paid, 0)
    
    def test_compound_interest_investment(self):
        """Test compound interest calculation"""
        analysis = RentVsBuyAnalysis(500000, 100000)
        
        # Invest $100k at 7% for 10 years
        # Formula: P * (1 + r)^n = 100000 * (1.07)^10
        returns = analysis.calculate_investment_returns(
            years=10,
            annual_return_rate=7.0
        )
        
        expected = 100000 * (1.07 ** 10)
        self.assertAlmostEqual(returns['final_amount'], expected, delta=100)


def run_all_tests():
    """Run all unit tests"""
    unittest.main(verbosity=2)


if __name__ == '__main__':
    run_all_tests()
