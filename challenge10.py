bill = float(input("How much is the total bill?: "))
diners = float(input("How many diners are there?: "))
ans = bill/diners


print(f"Each diner should pay ₱ {('%.2f'%ans)} each")