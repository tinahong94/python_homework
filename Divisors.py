number = int(input("Choose a number: "))
divisor_list = []

for num in range(1, number):
    if number % num == 0:
        divisor_list.append(num)
print(divisor_list)