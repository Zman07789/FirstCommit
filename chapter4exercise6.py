hrs = input("Enter Hours:")
rate = input("Enter Rate:")

def computepay(hrs,rate):
    h = float(hrs)
    r = float(rate)
    if h > 40:
       otp = (h-40.0) *(r*1.5)
       reg = (40.0*r)
       pay = (otp + reg)
        
    else:
       pay = (h*r)
    return pay
p = computepay(hrs,rate)
print("Pay: ", p )

