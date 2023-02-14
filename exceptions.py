
num = input("Choose a number ")
try:
    print(f"Trying to cast {num} to a integer...")
    num = int(num)
    print(f"You entered the number {num}")
except ValueError:
    print(f"{num} is not a number, please try again")
except Exception as e:
    print("Exception was caught")
    print(type(e))
