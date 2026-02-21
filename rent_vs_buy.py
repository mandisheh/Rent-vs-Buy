"""
Rent vs Buy Analysis Tool
Compares the financial implications of buying vs renting and investing the down payment.
"""

class RentVsBuyAnalysis:
    def __init__(self, purchase_price, down_payment, loan_term_years=30, annual_interest_rate=6.5):
        """
        Initialize the analysis with property and financing details.
        
        Args:
            purchase_price: Total price of the house
            down_payment: Available cash for down payment
            loan_term_years: Mortgage loan term (default 30 years)
            annual_interest_rate: Mortgage interest rate as percentage (default 6.5%)
        """
        self.purchase_price = purchase_price
        self.down_payment = down_payment
        self.loan_amount = purchase_price - down_payment
        self.loan_term_years = loan_term_years
        self.annual_interest_rate = annual_interest_rate / 100
        self.monthly_interest_rate = self.annual_interest_rate / 12
        self.num_payments = loan_term_years * 12
    
    def calculate_monthly_mortgage_payment(self):
        """Calculate monthly mortgage payment using the standard mortgage formula."""
        if self.monthly_interest_rate == 0:
            return self.loan_amount / self.num_payments
        
        payment = self.loan_amount * (
            (self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** self.num_payments) /
            ((1 + self.monthly_interest_rate) ** self.num_payments - 1)
        )
        return payment
    
    def calculate_buying_costs(self, years, annual_property_tax_rate=1.2, annual_maintenance_rate=1.0,
                              annual_insurance_rate=0.5, annual_hoa=0.2, closing_costs_percent=3,
                              annual_appreciation_rate=3.0, monthly_income=5000, annual_inflation_rate=2.5,
                              monthly_investment_percentage=10.0, annual_market_return=7.0):
        """
        Calculate total costs of buying over specified years.
        Includes home equity plus investments from available budget.
        
        Args:
            years: Analysis period in years
            annual_property_tax_rate: Annual property tax as % of home value
            annual_maintenance_rate: Annual maintenance as % of home value
            annual_insurance_rate: Annual insurance as % of home value
            annual_hoa: Annual HOA fees as % of home value
            closing_costs_percent: One-time closing costs as % of purchase price
            annual_appreciation_rate: Expected annual home appreciation rate
            monthly_income: Initial monthly income
            annual_inflation_rate: Annual income inflation rate
            monthly_investment_percentage: Percentage of available budget to invest
            annual_market_return: Expected annual market return for investments
        
        Returns:
            Dictionary with detailed cost breakdown
        """
        monthly_mortgage = self.calculate_monthly_mortgage_payment()
        total_mortgage_payments = monthly_mortgage * 12 * years
        
        # Calculate remaining balance after specified years
        remaining_balance = self.calculate_remaining_mortgage_balance(years)
        
        # Principal paid = initial loan - remaining balance
        principal_paid = self.loan_amount - remaining_balance
        
        # Total interest paid = total payments - principal paid
        total_interest_paid = total_mortgage_payments - principal_paid
        
        # Closing costs (upfront)
        closing_costs = self.purchase_price * (closing_costs_percent / 100)
        
        # Ongoing costs
        total_property_tax = 0
        total_maintenance = 0
        total_insurance = 0
        total_hoa = 0
        
        current_home_value = self.purchase_price
        for year in range(years):
            # Costs based on current appreciated value
            annual_property_tax = current_home_value * (annual_property_tax_rate / 100)
            total_property_tax += annual_property_tax
            
            annual_maintenance = current_home_value * (annual_maintenance_rate / 100)
            total_maintenance += annual_maintenance
            
            annual_insurance = current_home_value * (annual_insurance_rate / 100)
            total_insurance += annual_insurance
            
            annual_hoa_cost = current_home_value * (annual_hoa / 100)
            total_hoa += annual_hoa_cost
            
            # Appreciate home value
            current_home_value *= (1 + annual_appreciation_rate / 100)
        
        # Final home value
        final_home_value = self.purchase_price * ((1 + annual_appreciation_rate / 100) ** years)
        
        # Home equity (home value - remaining mortgage - selling costs)
        selling_costs = final_home_value * 0.06  # Typical 6% realtor commission
        home_equity = final_home_value - remaining_balance - selling_costs
        
        total_costs = (closing_costs + total_mortgage_payments + total_property_tax + 
                      total_maintenance + total_insurance + total_hoa + selling_costs)
        
        # Calculate investments from available budget (income - monthly buy costs)
        monthly_return = annual_market_return / 100 / 12
        available_budget_investments = 0
        
        current_home_value = self.purchase_price
        for year in range(years):
            # Income increases annually with inflation
            current_monthly_income = monthly_income * ((1 + annual_inflation_rate / 100) ** year)
            
            # Monthly investment = percentage of gross income (not dependent on costs)
            monthly_investment_amount = current_monthly_income * (monthly_investment_percentage / 100)
            
            for month in range(12):
                # Grow existing investment
                available_budget_investments *= (1 + monthly_return)
                # Add monthly investment
                available_budget_investments += monthly_investment_amount
            
            # Appreciate home value for next year
            current_home_value *= (1 + annual_appreciation_rate / 100)
        
        # Total wealth after buying = home equity + available budget investments
        total_wealth = home_equity + available_budget_investments
        
        return {
            'initial_down_payment': self.down_payment,
            'closing_costs': closing_costs,
            'total_mortgage_payments': total_mortgage_payments,
            'total_interest_paid': total_interest_paid,
            'total_property_tax': total_property_tax,
            'total_maintenance': total_maintenance,
            'total_insurance': total_insurance,
            'total_hoa': total_hoa,
            'selling_costs': selling_costs,
            'total_costs': total_costs,
            'final_home_value': final_home_value,
            'remaining_mortgage_balance': remaining_balance,
            'home_equity': home_equity,
            'available_budget_investments': available_budget_investments,
            'net_cost': total_costs - home_equity,
            'net_position': total_wealth - (total_costs - selling_costs),
            'monthly_mortgage_payment': monthly_mortgage
        }
    
    def calculate_remaining_mortgage_balance(self, years):
        """Calculate remaining mortgage balance after specified years."""
        months_paid = years * 12
        if months_paid >= self.num_payments:
            return 0
        
        monthly_payment = self.calculate_monthly_mortgage_payment()
        remaining_payments = self.num_payments - months_paid
        
        balance = monthly_payment * (
            ((1 + self.monthly_interest_rate) ** remaining_payments - 1) /
            (self.monthly_interest_rate * (1 + self.monthly_interest_rate) ** remaining_payments)
        )
        return balance
    
    def calculate_investment_returns(self, years, annual_return_rate=7.0):
        """
        Calculate investment returns if down payment is invested instead of buying.
        
        Args:
            years: Investment period in years
            annual_return_rate: Expected annual market return rate (default 7%)
        
        Returns:
            Dictionary with investment details
        """
        annual_return = annual_return_rate / 100
        final_amount = self.down_payment * ((1 + annual_return) ** years)
        total_return = final_amount - self.down_payment
        
        return {
            'initial_investment': self.down_payment,
            'final_amount': final_amount,
            'total_return': total_return,
            'annual_return_rate': annual_return_rate
        }
    
    def calculate_renting_costs(self, years, monthly_rent, annual_market_return=7.0, annual_rent_increase_rate=3.0,
                               monthly_income=5000, annual_inflation_rate=2.5, monthly_investment_percentage=10.0):
        """
        Calculate total renting costs over specified years.
        Uses available monthly budget (income - rent) * investment percentage for investments.
        
        Args:
            years: Renting period in years
            monthly_rent: Initial monthly rent
            annual_rent_increase_rate: Expected annual rent increase rate
            monthly_income: Initial monthly income
            annual_inflation_rate: Annual income inflation rate
            monthly_investment_percentage: Percentage of available budget to invest
        
        Returns:
            Dictionary with renting details
        """
        total_rent = 0
        for year in range(years):
            annual_rent = monthly_rent * 12 * ((1 + annual_rent_increase_rate / 100) ** year)
            total_rent += annual_rent
        
        # Calculate investment growth: down payment + monthly investments from available budget
        monthly_return = annual_market_return / 100 / 12
        investment_value = self.down_payment
        
        for year in range(years):
            # Income increases annually with inflation
            current_monthly_income = monthly_income * ((1 + annual_inflation_rate / 100) ** year)
            
            # Calculate current monthly rent
            current_monthly_rent = monthly_rent * ((1 + annual_rent_increase_rate / 100) ** year)
            
            # Available budget for investment = income - rent
            available_budget = max(0, current_monthly_income - current_monthly_rent)
            monthly_investment_amount = available_budget * (monthly_investment_percentage / 100)
            
            for month in range(12):
                # Grow existing investment
                investment_value *= (1 + monthly_return)
                # Add monthly investment
                investment_value += monthly_investment_amount
        
        return {
            'total_rent_paid': total_rent,
            'investment_amount': investment_value,
            'total_outflow': total_rent,
            'net_position': investment_value - total_rent
        }
    
    def calculate_monthly_costs(self, years, monthly_rent, annual_property_tax_rate=1.2, 
                               annual_maintenance_rate=1.0, annual_insurance_rate=0.5, 
                               annual_hoa=0, closing_costs_percent=3, annual_appreciation_rate=3.0, 
                               annual_rent_increase_rate=3.0, monthly_income=5000, annual_inflation_rate=2.5,
                               monthly_investment_percentage=10.0):
        """
        Calculate yearly average costs and monthly investment amounts for both buying and renting scenarios.
        
        Returns:
            Dictionary with lists of years and average yearly costs/investments
        """
        # Initialize lists
        years_list = list(range(1, years + 1))
        buy_yearly_costs = []
        rent_yearly_costs = []
        monthly_income_values = []
        buy_monthly_investments = []
        rent_monthly_investments = []
        
        # Buying costs
        monthly_mortgage = self.calculate_monthly_mortgage_payment()
        current_home_value = self.purchase_price
        
        for year in years_list:
            yearly_buy_costs = 0
            
            for month_in_year in range(12):
                # Monthly costs based on current home value
                monthly_property_tax = current_home_value * (annual_property_tax_rate / 100) / 12
                monthly_maintenance = current_home_value * (annual_maintenance_rate / 100) / 12
                monthly_insurance = current_home_value * (annual_insurance_rate / 100) / 12
                monthly_hoa = current_home_value * (annual_hoa / 100) / 12
                
                # Sum monthly costs
                yearly_buy_costs += monthly_mortgage + monthly_property_tax + monthly_maintenance + monthly_insurance + monthly_hoa
            
            # Calculate average monthly cost for this year
            avg_monthly_cost = yearly_buy_costs / 12
            buy_yearly_costs.append(round(avg_monthly_cost, 2))
            
            # Update home value annually
            current_home_value *= (1 + annual_appreciation_rate / 100)
        
        # Renting costs and investments
        for year in years_list:
            # Calculate average monthly rent for this year (accounting for annual increases)
            current_monthly_rent = monthly_rent * ((1 + annual_rent_increase_rate / 100) ** (year - 1))
            rent_yearly_costs.append(round(current_monthly_rent, 2))
        
        # Monthly income and investment values (accounting for inflation)
        current_home_value = self.purchase_price
        for year in years_list:
            current_monthly_income = monthly_income * ((1 + annual_inflation_rate / 100) ** (year - 1))
            monthly_income_values.append(round(current_monthly_income, 2))
            
            # For buy scenario: available budget is income minus monthly buy costs
            monthly_mortgage = self.calculate_monthly_mortgage_payment()
            current_home_value_for_taxes = self.purchase_price * ((1 + annual_appreciation_rate / 100) ** (year - 1))
            monthly_property_tax = current_home_value_for_taxes * (annual_property_tax_rate / 100) / 12
            monthly_maintenance = current_home_value_for_taxes * (annual_maintenance_rate / 100) / 12
            monthly_insurance = current_home_value_for_taxes * (annual_insurance_rate / 100) / 12
            monthly_hoa_cost = current_home_value_for_taxes * (annual_hoa / 100) / 12
            
            total_monthly_buy_cost = monthly_mortgage + monthly_property_tax + monthly_maintenance + monthly_insurance + monthly_hoa_cost
            available_budget_buy = max(0, current_monthly_income - total_monthly_buy_cost)
            monthly_investment_buy = available_budget_buy * (monthly_investment_percentage / 100)
            buy_monthly_investments.append(round(monthly_investment_buy, 2))
            
            # For rent scenario: available budget is income minus monthly rent
            current_monthly_rent = monthly_rent * ((1 + annual_rent_increase_rate / 100) ** (year - 1))
            available_budget_rent = max(0, current_monthly_income - current_monthly_rent)
            monthly_investment_rent = available_budget_rent * (monthly_investment_percentage / 100)
            rent_monthly_investments.append(round(monthly_investment_rent, 2))
            
            # Update home value for next year
            current_home_value *= (1 + annual_appreciation_rate / 100)
        
        return {
            'years': years_list,
            'buy_costs': buy_yearly_costs,
            'rent_costs': rent_yearly_costs,
            'monthly_income': monthly_income_values,
            'buy_monthly_investments': buy_monthly_investments,
            'rent_monthly_investments': rent_monthly_investments
        }
    
    def calculate_yearly_growth(self, years, monthly_rent, annual_market_return=7.0, 
                               closing_costs_percent=3, annual_appreciation_rate=3.0, 
                               annual_rent_increase_rate=3.0, monthly_income=5000, 
                               annual_inflation_rate=2.5, monthly_investment_percentage=10.0,
                               annual_property_tax_rate=1.2, annual_maintenance_rate=1.0,
                               annual_insurance_rate=0.5, annual_hoa=0):
        """
        Calculate yearly home equity (after sales) and investment growth.
        Uses available monthly budget (income - monthly cost) * investment percentage for additional investments.
        
        Returns arrays with values for each year for charting.
        """
        yearly_home_equity = []
        yearly_investment_value_buy = []
        yearly_investment_value_rent = []
        yearly_investment_gains_buy = []
        yearly_investment_gains_rent = []
        monthly_return = annual_market_return / 100 / 12
        
        # Calculate monthly costs for both scenarios
        monthly_mortgage = self.calculate_monthly_mortgage_payment()
        current_home_value = self.purchase_price
        
        for year in range(1, years + 1):
            # Calculate home equity after sales at this year
            final_home_value = self.purchase_price * ((1 + annual_appreciation_rate / 100) ** year)
            remaining_balance = self.calculate_remaining_mortgage_balance(year)
            selling_costs = final_home_value * 0.06
            equity_after_sales = final_home_value - remaining_balance - selling_costs
            yearly_home_equity.append(round(max(0, equity_after_sales), 2))
            
            # Calculate investment with available budget for BUY SCENARIO
            investment_value_buy = self.down_payment
            total_contributions_buy = self.down_payment
            
            for y in range(year):
                # Income increases annually with inflation
                current_monthly_income = monthly_income * ((1 + annual_inflation_rate / 100) ** y)
                
                # Calculate average monthly buy cost
                home_value_at_year = self.purchase_price * ((1 + annual_appreciation_rate / 100) ** y)
                monthly_property_tax = home_value_at_year * (annual_property_tax_rate / 100) / 12
                monthly_maintenance = home_value_at_year * (annual_maintenance_rate / 100) / 12
                monthly_insurance = home_value_at_year * (annual_insurance_rate / 100) / 12
                monthly_hoa = home_value_at_year * (annual_hoa / 100) / 12
                avg_monthly_buy_cost = monthly_mortgage + monthly_property_tax + monthly_maintenance + monthly_insurance + monthly_hoa
                
                # Calculate available budget for investment (income - cost of buying)
                available_budget_buy = max(0, current_monthly_income - avg_monthly_buy_cost)
                monthly_investment_amount_buy = available_budget_buy * (monthly_investment_percentage / 100)
                
                for month in range(12):
                    # Grow existing investment
                    investment_value_buy *= (1 + monthly_return)
                    # Add monthly investment
                    investment_value_buy += monthly_investment_amount_buy
                    total_contributions_buy += monthly_investment_amount_buy
            
            yearly_investment_value_buy.append(round(investment_value_buy, 2))
            # Calculate gains: total value minus contributions
            gains_buy = max(0, investment_value_buy - total_contributions_buy)
            yearly_investment_gains_buy.append(round(gains_buy, 2))
            
            # Calculate investment with available budget for RENT SCENARIO
            investment_value_rent = self.down_payment
            total_contributions_rent = self.down_payment
            
            for y in range(year):
                # Income increases annually with inflation
                current_monthly_income = monthly_income * ((1 + annual_inflation_rate / 100) ** y)
                
                # Calculate current rent cost
                current_monthly_rent = monthly_rent * ((1 + annual_rent_increase_rate / 100) ** y)
                
                # Calculate available budget for investment (income - rent)
                available_budget_rent = max(0, current_monthly_income - current_monthly_rent)
                monthly_investment_amount_rent = available_budget_rent * (monthly_investment_percentage / 100)
                
                for month in range(12):
                    # Grow existing investment
                    investment_value_rent *= (1 + monthly_return)
                    # Add monthly investment
                    investment_value_rent += monthly_investment_amount_rent
                    total_contributions_rent += monthly_investment_amount_rent
            
            yearly_investment_value_rent.append(round(investment_value_rent, 2))
            # Calculate gains: total value minus contributions
            gains_rent = max(0, investment_value_rent - total_contributions_rent)
            yearly_investment_gains_rent.append(round(gains_rent, 2))
        
        return {
            'years': list(range(1, years + 1)),
            'home_equity_after_sales': yearly_home_equity,
            'investment_growth': yearly_investment_value_rent,  # For backwards compatibility
            'investment_growth_buy': yearly_investment_value_buy,
            'investment_growth_rent': yearly_investment_value_rent,
            'investment_gains_buy': yearly_investment_gains_buy,
            'investment_gains_rent': yearly_investment_gains_rent
        }
    
    def compare_scenarios(self, years, monthly_rent, annual_market_return=7.0, 
                         annual_property_tax_rate=1.2, annual_maintenance_rate=1.0,
                         annual_insurance_rate=0.5, annual_hoa=0, closing_costs_percent=3,
                         annual_appreciation_rate=3.0, annual_rent_increase_rate=3.0,
                         monthly_income=5000, annual_inflation_rate=2.5, monthly_investment_percentage=10.0):
        """
        Compare buying vs renting scenarios and provide analysis.
        
        Returns:
            Dictionary with comparison results
        """
        buying_costs = self.calculate_buying_costs(
            years, annual_property_tax_rate, annual_maintenance_rate,
            annual_insurance_rate, annual_hoa, closing_costs_percent, annual_appreciation_rate,
            monthly_income, annual_inflation_rate, monthly_investment_percentage, annual_market_return
        )
        
        renting_costs = self.calculate_renting_costs(years, monthly_rent, annual_market_return, annual_rent_increase_rate,
                                                     monthly_income, annual_inflation_rate, monthly_investment_percentage)
        
        # Get monthly cost data for charting
        monthly_costs = self.calculate_monthly_costs(
            years, monthly_rent, annual_property_tax_rate, annual_maintenance_rate,
            annual_insurance_rate, annual_hoa, closing_costs_percent, annual_appreciation_rate,
            annual_rent_increase_rate, monthly_income, annual_inflation_rate, monthly_investment_percentage
        )
        
        # Get yearly equity and investment growth data for charting
        yearly_growth = self.calculate_yearly_growth(
            years, monthly_rent, annual_market_return, closing_costs_percent,
            annual_appreciation_rate, annual_rent_increase_rate, monthly_income,
            annual_inflation_rate, monthly_investment_percentage,
            annual_property_tax_rate, annual_maintenance_rate,
            annual_insurance_rate, annual_hoa
        )
        
        # Net position comparison
        buy_net_cost = buying_costs['net_cost']
        rent_net_cost = renting_costs['total_outflow']  # Total rent paid (actual cost)
        
        # Compare net positions: which scenario leaves you with more wealth?
        buy_net_position = buying_costs['net_position']
        rent_net_position = renting_costs['net_position']
        position_advantage = buy_net_position - rent_net_position
        
        return {
            'analysis_period_years': years,
            'buying': buying_costs,
            'renting': renting_costs,
            'financial_advantage': position_advantage,
            'buy_net_cost': buy_net_cost,
            'rent_net_position': rent_net_position,
            'rent_net_cost': rent_net_cost,
            'recommendation': 'BUY' if buy_net_position > rent_net_position else 'RENT',
            'advantage_amount': abs(position_advantage),
            'advantage_description': f"Buying is better by ${abs(position_advantage):,.2f}" if position_advantage > 0 else f"Renting is better by ${abs(position_advantage):,.2f}",
            'monthly_costs': monthly_costs,
            'yearly_growth': yearly_growth
        }


def print_analysis_report(analysis_results):
    """Print a formatted analysis report."""
    print("\n" + "=" * 80)
    print("RENT VS BUY ANALYSIS REPORT".center(80))
    print("=" * 80)
    
    years = analysis_results['analysis_period_years']
    print(f"\nAnalysis Period: {years} years")
    
    # Recommendation
    print("\n" + "-" * 80)
    print(f"RECOMMENDATION: {analysis_results['recommendation']}")
    print(f"Advantage: {analysis_results['advantage_description']}")
    print("-" * 80)
    
    # Buying Analysis
    print("\nBUYING SCENARIO:")
    print("-" * 80)
    buying = analysis_results['buying']
    print(f"  Initial Down Payment:        ${buying['initial_down_payment']:>15,.2f}")
    print(f"  Closing Costs:               ${buying['closing_costs']:>15,.2f}")
    print(f"  Monthly Mortgage Payment:    ${buying['monthly_mortgage_payment']:>15,.2f}")
    print(f"  Total Mortgage Payments:     ${buying['total_mortgage_payments']:>15,.2f}")
    print(f"  Total Property Tax:          ${buying['total_property_tax']:>15,.2f}")
    print(f"  Total Maintenance:           ${buying['total_maintenance']:>15,.2f}")
    print(f"  Total Insurance:             ${buying['total_insurance']:>15,.2f}")
    print(f"  Total HOA Fees:              ${buying['total_hoa']:>15,.2f}")
    print(f"  Selling Costs:               ${buying['selling_costs']:>15,.2f}")
    print(f"  Total Costs:                 ${buying['total_costs']:>15,.2f}")
    print(f"\n  Final Home Value:            ${buying['final_home_value']:>15,.2f}")
    print(f"  Remaining Mortgage Balance:  ${buying['remaining_mortgage_balance']:>15,.2f}")
    print(f"  Home Equity (after sales):   ${buying['home_equity']:>15,.2f}")
    print(f"\n  NET COST OF BUYING:          ${buying['net_cost']:>15,.2f}")
    
    # Renting Analysis
    print("\nRENTING SCENARIO:")
    print("-" * 80)
    renting = analysis_results['renting']
    print(f"  Total Rent Paid:             ${renting['total_rent_paid']:>15,.2f}")
    print(f"  Down Payment Invested:       ${renting['investment_from_down_payment']:>15,.2f}")
    print(f"  Total Cash Outflow:          ${renting['total_outflow']:>15,.2f}")
    print(f"\n  NET POSITION (Rent + Invest):${renting['net_position']:>15,.2f}")
    
    # Summary
    print("\n" + "=" * 80)
    print("COMPARISON SUMMARY:")
    print("=" * 80)
    print(f"  Buy Net Cost:                ${analysis_results['buy_net_cost']:>15,.2f}")
    print(f"  Rent Total Cost:             ${analysis_results['rent_net_cost']:>15,.2f}")
    print(f"\n  Financial Advantage:         {analysis_results['advantage_description']}")
    print("=" * 80 + "\n")


# Example usage
if __name__ == "__main__":
    # Example parameters
    purchase_price = 500000
    down_payment = 100000
    monthly_rent = 2000
    analysis_years = 10
    
    # Create analysis
    analysis = RentVsBuyAnalysis(
        purchase_price=purchase_price,
        down_payment=down_payment,
        loan_term_years=30,
        annual_interest_rate=6.5
    )
    
    # Run comparison
    results = analysis.compare_scenarios(
        years=analysis_years,
        monthly_rent=monthly_rent,
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
