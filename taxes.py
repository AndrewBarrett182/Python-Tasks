money = float(input('Input your wage for tax calculation: ')) #ask user for input
tax = round(money * 0.2, 2) #calculate tax
#format so that values are to 2.d.p (standard for money)
money = '%.2f' % money 
tax = '%.2f' % tax
print(f'With your balance of {money}, you must pay {tax} for this tax year.') #output