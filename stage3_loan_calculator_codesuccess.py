import math

print('What do you want to calculate?')
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
reply = input()

if reply == 'n':
    print('Enter the loan principal:')
    l_prin = int(input())
    print('Enter the monthly payment:')
    m_pay = int(input())
    print('Enter the loan interest:')
    l_intrst = float(input())
    interest = (l_intrst/100)/12
    formula_n = math.ceil(math.log(m_pay/(m_pay-interest*l_prin), 1+interest))
    years = math.floor(formula_n/12)
    months = formula_n % 12
    print(f'It will take {years} years and {months} months to repay this loan!')
elif reply == 'a':
    print('Enter the loan principal:')
    l_prin = int(input())
    print('Enter the number of periods:')
    num_periods = int(input())
    print('Enter the loan interest:')
    l_intrst = float(input())
    interest = (l_intrst/100)/12
    annuity = math.ceil(l_prin * ((interest*math.pow((1+interest),num_periods))/(math.pow((1+interest),num_periods)-1)))
    print(f'Your monthly payment = {annuity}!')
else:
    print('Enter the annuity payment:')
    annui_pay = float(input())
    print('Enter the number of periods:')
    num_periods = int(input())
    print('Enter the loan interest:')
    l_intrst = float(input())
    interest = (l_intrst/100)/12
    loan_principal = round(annui_pay/((interest*math.pow((1+interest),num_periods))/(math.pow((1+interest),num_periods)-1)))
    print(f'Your loan principal = {loan_principal}!')
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
