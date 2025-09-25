hrs = float(input("Enter hours: "))
rate = float(input("Enter rate per hour: "))

if hrs >= 40 :
 overtime = hrs - 40
 gross_pay = 40 * rate +  overtime  * rate * 1.5
else :
 gross_pay = hrs * rate 

print(gross_pay)