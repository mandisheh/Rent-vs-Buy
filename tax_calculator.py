"""
Tax Calculator for Affordability Analysis
Calculates federal and state income taxes based on gross income
"""

class TaxCalculator:
    # 2024 Federal Tax Brackets (Single Filer)
    FEDERAL_BRACKETS_SINGLE_2024 = [
        (11600, 0.10),      # 10% up to $11,600
        (47150, 0.12),      # 12% up to $47,150
        (100525, 0.22),     # 22% up to $100,525
        (191950, 0.24),     # 24% up to $191,950
        (243725, 0.32),     # 32% up to $243,725
        (609350, 0.35),     # 35% up to $609,350
        (float('inf'), 0.37) # 37% above $609,350
    ]
    
    # 2024 Federal Tax Brackets (Married Filing Jointly)
    FEDERAL_BRACKETS_MARRIED_2024 = [
        (23200, 0.10),      # 10% up to $23,200
        (94300, 0.12),      # 12% up to $94,300
        (201050, 0.22),     # 22% up to $201,050
        (383900, 0.24),     # 24% up to $383,900
        (487450, 0.32),     # 32% up to $487,450
        (731200, 0.35),     # 35% up to $731,200
        (float('inf'), 0.37) # 37% above $731,200
    ]
    
    # Standard deduction for 2024
    STANDARD_DEDUCTION_SINGLE_2024 = 14600
    STANDARD_DEDUCTION_MARRIED_2024 = 29200
    
    # State tax rates (simplified flat rates or brackets)
    STATE_TAX_RATES = {
        'AL': 0.05,  # Alabama
        'AK': 0.00,  # Alaska (no income tax)
        'AZ': 0.0455,
        'AR': 0.0588,
        'CA': 0.093,  # Approximate average
        'CO': 0.0425,
        'CT': 0.0699,
        'DE': 0.065,
        'FL': 0.00,  # Florida (no income tax)
        'GA': 0.0575,
        'HI': 0.088,
        'ID': 0.0575,
        'IL': 0.0495,
        'IN': 0.0323,
        'IA': 0.0583,
        'KS': 0.057,
        'KY': 0.0575,
        'LA': 0.0575,
        'ME': 0.0715,
        'MD': 0.0775,
        'MA': 0.05,
        'MI': 0.0425,
        'MN': 0.0985,
        'MS': 0.05,
        'MO': 0.0595,
        'MT': 0.0675,
        'NE': 0.0684,
        'NV': 0.00,  # Nevada (no income tax)
        'NH': 0.00,  # New Hampshire (no income tax)
        'NJ': 0.0637,
        'NM': 0.059,
        'NY': 0.0685,
        'NC': 0.058,
        'ND': 0.0290,
        'OH': 0.04,
        'OK': 0.0575,
        'OR': 0.0775,
        'PA': 0.0307,
        'RI': 0.0675,
        'SC': 0.07,
        'SD': 0.00,  # South Dakota (no income tax)
        'TN': 0.00,  # Tennessee (no income tax)
        'TX': 0.00,  # Texas (no income tax)
        'UT': 0.0495,
        'VT': 0.0635,
        'VA': 0.0575,
        'WA': 0.00,  # Washington (no income tax)
        'WV': 0.065,
        'WI': 0.0671,
        'WY': 0.00,  # Wyoming (no income tax)
    }
    
    @staticmethod
    def calculate_federal_tax(annual_income, filing_status='single'):
        """Calculate federal income tax using 2024 brackets"""
        # Select appropriate brackets and standard deduction
        if filing_status.lower() == 'married':
            brackets = TaxCalculator.FEDERAL_BRACKETS_MARRIED_2024
            standard_deduction = TaxCalculator.STANDARD_DEDUCTION_MARRIED_2024
        else:
            brackets = TaxCalculator.FEDERAL_BRACKETS_SINGLE_2024
            standard_deduction = TaxCalculator.STANDARD_DEDUCTION_SINGLE_2024
        
        if annual_income <= standard_deduction:
            return 0
        
        taxable_income = annual_income - standard_deduction
        tax = 0
        previous_limit = 0
        
        for limit, rate in brackets:
            if taxable_income <= previous_limit:
                break
            
            taxable_in_bracket = min(taxable_income, limit) - previous_limit
            tax += taxable_in_bracket * rate
            previous_limit = limit
        
        return max(0, tax)
    
    @staticmethod
    def calculate_state_tax(annual_income, state_code):
        """Calculate state income tax"""
        if state_code not in TaxCalculator.STATE_TAX_RATES:
            state_code = 'CA'  # Default to California if invalid state
        
        # Simplified calculation - apply state rate to gross income
        # In reality, some states have deductions and brackets
        state_rate = TaxCalculator.STATE_TAX_RATES[state_code]
        return annual_income * state_rate
    
    @staticmethod
    def calculate_fica_taxes(annual_income):
        """Calculate FICA taxes (Social Security and Medicare)"""
        social_security_rate = 0.062
        medicare_rate = 0.0145
        additional_medicare_rate = 0.009  # For income over $200,000
        
        # Social Security is capped at $168,600 (2024)
        ss_wage_base = 168600
        ss_tax = min(annual_income, ss_wage_base) * social_security_rate
        
        # Medicare taxes
        medicare_tax = annual_income * medicare_rate
        
        # Additional Medicare tax for high earners
        if annual_income > 200000:
            additional_medicare = (annual_income - 200000) * additional_medicare_rate
        else:
            additional_medicare = 0
        
        total_fica = ss_tax + medicare_tax + additional_medicare
        return total_fica
    
    @staticmethod
    def calculate_after_tax_income(gross_annual_income, state_code='CA', filing_status='single'):
        """
        Calculate after-tax income including federal, state, and FICA taxes
        
        Args:
            gross_annual_income: Annual income before taxes
            state_code: Two-letter state code
            filing_status: 'single' or 'married'
        
        Returns:
            dict with breakdown of taxes and after-tax income
        """
        federal_tax = TaxCalculator.calculate_federal_tax(gross_annual_income, filing_status)
        state_tax = TaxCalculator.calculate_state_tax(gross_annual_income, state_code)
        fica_tax = TaxCalculator.calculate_fica_taxes(gross_annual_income)
        
        total_tax = federal_tax + state_tax + fica_tax
        after_tax_income = gross_annual_income - total_tax
        
        return {
            'gross_annual_income': round(gross_annual_income, 2),
            'federal_tax': round(federal_tax, 2),
            'state_tax': round(state_tax, 2),
            'fica_tax': round(fica_tax, 2),
            'total_tax': round(total_tax, 2),
            'after_tax_income': round(after_tax_income, 2),
            'after_tax_monthly_income': round(after_tax_income / 12, 2),
            'effective_tax_rate': round((total_tax / gross_annual_income * 100), 2) if gross_annual_income > 0 else 0
        }
    
    @staticmethod
    def get_available_states():
        """Return list of available states and their codes"""
        return sorted(TaxCalculator.STATE_TAX_RATES.keys())
