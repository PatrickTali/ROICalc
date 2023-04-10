class Rentalprop:
    
    def __init__(self, rent, expenses, down_payment, closing_cost, rehab):
        self.rent = rent
        self.expenses = expenses
        self.down_payment = down_payment
        self.closing_cost = closing_cost
        self.rehab = rehab
        
    def calculate_roi(self):
        total_rent = self.rent
        monthly_cashflow = total_rent - self.expenses
        annual_cashflow = monthly_cashflow * 12
        total_invested = self.down_payment + self.closing_cost + self.rehab
        roi = (annual_cashflow / total_invested) * 100
        return roi
    

property_ = Rentalprop(rent = 2000,
                        expenses = 1610,
                        down_payment = 40000,
                        closing_cost = 3000,
                        rehab = 7000)
                        
    



roi = property_.calculate_roi()
print("ROI for this property is {:.2f}%".format(roi))                        
                     

                            
                     




