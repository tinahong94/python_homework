number = int(input("Give me a number: "))

divisor = [x for x in range(1, number + 1) if number % x == 0]
print(divisor)

def get_primality(n):
    divisor.remove(1)
    # divisor.remove(number)
    if not divisor:
        print("This number " + str(number) + " is prime number")
    else:
        print("This number " + str(number) + " is not prime")

get_primality(6)






# def get_primality(n):
#     if divisor == 1 and divisor == n:
#             print("This number " + str(number) + " is prime number")
#             print(divisor)
#     else:
#         if divisor in {1, n}:
#             print("This number " + str(number) + " is not prime")


# def main():
#     number = int(input("Give me a number: "))
#     get_primality(number)
#
#
# def get_primality(n):
#     return [n % x for x in range(2, n)]
#
# main()
