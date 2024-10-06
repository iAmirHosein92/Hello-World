a = float(input("Please Input A Value : "))
b = float(input ("Please Input A Value : "))
c = float(input("Please Input A Value : "))
average = round( ((a + b + c) / 3) , 2 )
print(average)
if average < 0 :
    print ("Average Is Negative")
elif 0 <= average <= 10 :
    print ("Average Is Between 0 , 10")
elif 11 <= average <= 20 :
    print("Average Is Between 11 , 20")
else :
    print("Average Is Bigger Than 20") 