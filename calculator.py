def add(x, y):
    return x + y



def subtract(x, y):
    return x - y


def multiplication(x, y):
    return x * y

    

def division(x, y):
    if y==0:
        return "0 cannot be proccessed"
        return x / y


print ("--------------------------------------------")
print ("--------------------Selection Menu--------------------")       
print ("1. Addition") 
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")
print ("--------------------------------------------")

# choice 
choice = input("Enter Choice : (1/2/3/4)!")

num1 = float(input("Input First Number :"))
num2 = float(input("Input Second Number:"))




# operation ( Main calculation part here )
if choice == '1':
    print(num1, "+", num2, "=", add(num1, num2))

elif choice == '2':
    print(num1, "-", num2, "=", subtract(num1, num2))

elif choice == '3':
    print(num1, "*", num2, "=", multiply(num1, num2))

elif choice == '4':
    print(num1, "/", num2, "=", divide(num1, num2))

else:
    print("Invalid input! Please select a valid choice from the Selection Menu!")
