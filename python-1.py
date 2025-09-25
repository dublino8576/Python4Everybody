'''
hrs = int(input("Enter hours: "))
rate = float(input("Enter rate: "))

pay = rate * hrs
print("Pay:", pay)



x = 2.0
if x == 6 :
    print('Is 6')
    print('Is Still 6')
    print('Third 6')

if x >= 6 :
        print("hello")

if x < 2 :
    print('Below 2')
elif x >= 2 :
     print('Two or more')
else :
    print('Something else')'''

hrs = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

if hrs >= 40 :
 overtime = hrs - 40
 gross_pay = 40 * rate +  overtime  * rate * 1.5
else :
 gross_pay = hrs * rate 

print(gross_pay)