h=1
for h in range(0,24):
    if h==0:
        print("12 MID NIGHT")
        continue
    if(h<12):
        print(h,"AM")
    if h==12:
        print(h,"noon") 
    if h>13:
        print(h%13,"PM")
print("11 PM")
a=int(input("Enter the number  --->  "))
cube=0
for i in range (1,a+1):
    cube=i*i*i
    print("Number is",i,"cube of the",i ,"is :",cube)
print("Wow")
for i in range(1,51):
    if i%3==0 and i%5!=0:
        print("Multiple of Three")
        continue
    if i%5==0 and i%3!=0:
        print("Multiple of Five")
        continue
    if i%5==0 and i%3==0:
        print("Wow")
        continue
    else:
        print(i)
       