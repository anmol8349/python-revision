
# syntax erro--------------

# if x == 5
#     print("Hello")


# int("abc")   # ValueError
# 10 / 0       # ZeroDivisionError
# open("a.txt") # FileNotFoundError







# Exception Name	                When it Happens
# ZeroDivisionError                 	Divide by zero
# ValueError	                Wrong data type
# TypeError                 	Wrong operation
# FileNotFoundError	                File missing
# IndexError                	List index out of range
# KeyError              	Dictionary key missing
# NameError	                Variable not defined
# AttributeError	                Wrong object property









try:
    a=int(input("enter no..  "))
    b=int(input("enter second no : "))
    
    divide=a/b
    
    print(divide)
    
except :
    print('second no. cant divide by zero ')
    
    
#  ZeroDivisionError:
#      ValueError
#       FileNotFoundError:
#       finally:
# except (ZeroDivisionError, ValueError):  multiple Error
# except Exception as e:
#  raise ValueError("")





try:
    x = int("abc")
except Exception as e:
    print("Error occurred:", e)
    
    
    
    
class InsufficientBalanceError(Exception):
    pass

balance = 1000
withdraw = 1500

if withdraw > balance:
    raise InsufficientBalanceError("Not enough balance")






try:
    marks = int(input("Enter marks: "))

    if marks < 0 or marks > 100:
        raise ValueError("Marks must be between 0 and 100")

except ValueError as e:
    print("❌ Error:", e)
else:
    print("✅ Marks saved:", marks)
