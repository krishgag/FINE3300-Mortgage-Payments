class Periodic_Payments:
    def __init__(self, principle, rate, amortization):
        self.principle=principle
        self.rate= rate/100
        self.amortization=amortization    


    def effective_rate(self,payments_per_year):
        m = 2 #note:there is semi-annual compounding
        return (1+self.rate/m)**(m/payments_per_year)-1
    
    def payments_due(self, effective_rate, total_payments):
        pv = self.principle
        i = effective_rate
        n = total_payments
        return ((pv*i)/(1-(1+i)**(-n)))
    
    def calc_payments(self):
        #measure effedtive periodic rates.
        monthly_i = self.effective_rate(12)
        semi_monthly_i = self.effective_rate(24)
        bi_weekly_i=self.effective_rate(26)
        weekly_i=self.effective_rate(52)

        #calculate total number of payments for the amortization time
        monthly_n =self.amortization * 12
        semi_monthly_n = self.amortization*24
        bi_weekly_n    = self.amortization * 26
        weekly_n       = self.amortization * 52


        #Calculare the payments due based on payment timing
        monthly_payment      = self.payments_due(monthly_i, monthly_n)
        semi_monthly_payment = self.payments_due(semi_monthly_i, semi_monthly_n)
        bi_weekly_payment    = self.payments_due(bi_weekly_i, bi_weekly_n)
        weekly_payment       = self.payments_due(weekly_i, weekly_n)
        rapid_bi_weekly_payment = monthly_payment / 2
        rapid_weekly_payment    = monthly_payment / 4

        return (round(monthly_payment, 2), round(semi_monthly_payment, 2), round(bi_weekly_payment, 2), (round(weekly_payment, 2)),
                round(rapid_bi_weekly_payment, 2), round(rapid_weekly_payment, 2))
    
def main():
        principle_input=(float(input("principle")))
        rate_input=(float(input("rate")))
        amortization_input=(float(input("amortization in years")))

        payments = Periodic_Payments(principle_input,rate_input,amortization_input)

        (monthly, semi_monthly, bi_weekly, weekly, rapid_bi_weekly, rapid_weekly) = payments.calc_payments()

        print("Monthly Payment: ${}".format(monthly))
        print("Semi-monthly Payment: ${}".format(semi_monthly))
        print("Bi-weekly Payment: ${}".format(bi_weekly))
        print("Weekly Payment: ${}".format(weekly))
        print("Rapid Bi-weekly Payment: ${}".format(rapid_bi_weekly))
        print("Rapid Weekly Payment: ${}".format(rapid_weekly))

if __name__ == "__main__":
    main()

    

