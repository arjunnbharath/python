#exception == an event that intrepets the flow of the program
#1.try ,2.execpt ,3. finally

try:
    numper = int(input("enter a number : "))
    print(1/0)
except ZeroDivisionError :
    print("you r in zero-division error")
except ValueError :
    print("you r in value error")
except Exception :
    print("something went wrong")    
finally:
    print("do some clean up here")
