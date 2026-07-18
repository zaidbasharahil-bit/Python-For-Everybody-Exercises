#first_code
hrs = input("Enter Hours:")
rate = input("Enter rate:")
try:
    h= float(hrs)
    r = float(rate)
except:
    print("eror, please change to number")
    quit()
print(h,r)
if h <= 40 :
    print(r*h)
else:
    rh = r*40
    oht = h - 40
    ohr= oht * (r*1.5)
    print(rh+ohr)

#2nd
score = input("Enter Score: ")
try:
    sco = float(score)
except: 
    print("sorry, it is not number")
    quit()
if 1.0 >= sco >= 0.0 :
    if sco>= 0.9 :
        print("A")
    elif sco>= 0.8:
        print("B")
    elif sco>= 0.7:
        print("C")
    elif sco>= 0.6:
        print("D")    
    elif sco< 0.6 :
        print("F")
else:
    print("write it again")    
