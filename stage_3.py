import math
    
#   calculate the interest
def i(b):
    return ((b/100)/12)
    
#   calculate the annuity
def a(principal,interest,num_pay):
    interest = i(b)
    num_pay = n(annuity,interest,principal)
    return principal*((interest*(math.pow((1+interest),num_pay)))/((math.pow((1+interest),num_pay))-1))

#   calculate the loan principal
def p(annuity,interest,num_pay):
    interest = i(b)
    num_pay = n(annuity,interest,principal)
    return annuity/((interest*(math.pow((1+interest),num_pay)))/((math.pow((1+interest),num_pay))-1))
    
#   calculate the number of payments
def n(annuity,interest,principal):
    interest = i(b)
    annuity = a(principal,interest,num_pay)
    return math.log((1+interest))*(annuity/(annuity-interest*principal))
    

    

print('What do you want to calculate?')
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')

reply = input()

if reply == 'n':
    print('Enter the loan principal: ')
    ans1 = int(input())
    print('Enter the monthly payment: ')
    ans2 = int(input())
    print('Enter the loan interest: ')
    ans3 = int(input())
    
    months = ceil(n(ans2,i(ans3),ans1))
    years = floor(month/12)
    spec_month = month%12
    print(f'It will take {years} years and {spec_months} months to repay this loan!')
elif reply == 'a':
    print("Enter the loan principal: ")
    nana = int(input())
    print('Enter the number of periods: ')
    nunu = int(input())
    print('Enter the loan interest: ')
    nene = int(input())
    
    a_ans = a(nana,i(nene),nunu)
    print(f'Your monthly payment = {a_ans}')
elif reply == 'p':
    print('Enter the annuity payment:')
    baba = float(input())
    print('Enter the number of periods: ')
    bubu = int(input())
    print('Enter the loan interest: ')
    bebe = float(input())
    
    p_ans = p(baba,i(bebe),bubu)
    print(f'Your loan principal = {p_ans}')
