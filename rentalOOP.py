class rentalIncome: 

    def __init__(self, expenses={}, investment ={}): 
        self.expenses = expenses #ALl the exspenses for the house
        self.investment = investment

    def rental_expenses(self):
        '''Collect all expenses for the rental property and place them into a dictionary. The keys will be what the expense is and the values will be the amount to be paid in integer'''
        #take in all inputs and place into expesnes dictionary 
        self.expenses
        
        while True:
            try: 
                hoa = 'HOA Dues'
                hoa_dues = int(input("What is the total monthly HOA dues? If none, type '0' "))
                break
            except: 
                print('Not a valid response. Provide an integer value.')
                continue
        while True:
            try: 
                tax = 'Annual Property Taxes'
                property_taxes = int(input("How much are the annual property taxes?: "))
                break
            except: 
                print("Not a valid response. Provide an integer value. \nIf none, type '0'")
                continue

        while True:
            try: 
                mortgage = 'Estimated Monthly Mortgage'
                mortgage_payment = int(input("What is estimated total monthly mortgage payment? If paid in full, enter '0': "))
                break
            except: 
                print("Not a valid response. Provide an integer value. \nIf none, type '0'")
                continue

        while True:
            try: 
                utility = 'Utilities'
                monthly_utilities = int(input("What is the estimated total amount for all utilities?: "))
                break
            except: 
                print("Not a valid response. Provide an integer value. \nIf none, type '0'")
                continue

        while True:
            try: 
                misc = 'Miscellanous'
                monthly_misc = int(input("How much do you want to budget for unexpected costs like lawn maintenance or repairs?: "))
                break
            except: 
                print("Not a valid response. Provide an integer value. \nIf none, type '0'")
                continue

        #assing it to a variable and not key. assing variable to keys later. se #if/else on each item to account fo stirng N and Quit) 

        self.expenses[hoa] = hoa_dues
        self.expenses[tax] = property_taxes
        self.expenses[mortgage] = mortgage_payment
        self.expenses[utility] = monthly_utilities
        self.expenses[misc] = monthly_misc
        self.total_expenses_entered = sum(self.expenses.values())
        

        
        #try/except on each one so that they dont repeat entering the whole thing
    def initial_investment(self): 
        self.investment
        
        while True:
            try: 
                payment_amount = "Initial Paid Amount"
                deposit = int(input("What is your initial cash payment on the rental home minus closing costs? If none, type '0' "))
                break
            except: 
                print("Not a valid response. Provide an integer value. \nIf none, type '0' ")
                continue
        while True:
            try: 
                c_cost = 'CLosing Costs'
                c_costb = int(input("What is the estimated closing costs?: "))
                break
            except: 
                print("Not a valid response. Provide an integer value. \nIf none, type '0'")
                continue
        while True:
            try: 
                rent = 'Estmated Monthly Rent'
                rental_value = int(input("How much can the property rent for per month?: "))
                break
            except: 
                print("Not a valid response. Provide an integer value.")
                continue
        self.investment[payment_amount] = deposit
        self.investment[c_cost] = c_costb
        self.investment[rent] = rental_value

        self.total_initial_cost = sum(self.investment.values())

    def roi(self):

        annual_return = (((self.investment['Estmated Monthly Rent'] + self.expenses['HOA Dues']) * 12) + (self.total_expenses_entered - (self.investment['Estmated Monthly Rent'] + self.expenses['HOA Dues'])))
        
        paid_investment = ((self.investment["Initial Paid Amount"] * 12)+(self.total_initial_cost - (self.investment['Estmated Monthly Rent'])))

        roi_shown = ((annual_return % paid_investment) * 100) 

        print(f'Your return on investment (ROI) based on your annual returns and initial cost of your investment is {roi_shown}%')



while True:
    action = input("Hi! So you're thinking of buying a rental home?\nAnd, you wanna know if there'll be a return on your investment?\n Yes/No: ")
    if action.lower() == 'no' or action.lower() == 'n':
        print("GoodBye")
    elif action.lower() == 'yes' or action.lower() == 'y': 
        my_calc = rentalIncome()
        my_calc.rental_expenses()
        my_calc.initial_investment()
        my_calc.roi()
        break
    else: 
        print('Not a valid entry. Please enter "Y" or "N" to continue: ')  
