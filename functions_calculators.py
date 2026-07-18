#1st
def computepay (h,r):
    if h <= 40:
        pay = h * r
    else:
        reg_pay = 40 * r
        over_time = h - 40
        over_time_pay= (over_time*1.5)* r
        pay = reg_pay + over_time_pay
    return pay
wh= input("enter houre:")
wr= input("enter rate:")
try:
    whn= float(wh)
    wrn= float(wr)
except: 
    print("sorry, it is not number")
    quit()
gross_pay= computepay(whn,wrn)
print("Pay",gross_pay)
#2nd
def calculate_bonus (b,rate):
    if b == "Excellent" or b==" excellent" :
       return rate * 0.2
    elif b== "Good" or b== "good" :
       return rate * 0.1 
    elif b== "poor" or b=='Poor' :
       return rate * 0
    else:
        return("Eror")
enter_bonus = input ("Enter bonus :")
enter_rate = input("Enter rate:")
try:
    enter_raten= float(enter_rate)
    enter_bonuss= str(enter_bonus)
except: 
    print("that is not true")
    quit()
Calculate_bonus = calculate_bonus(enter_bonuss,enter_raten)
print(Calculate_bonus)