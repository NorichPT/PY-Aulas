def print_multiplication_table(number, limit):
    for i in range(1, limit+1):
        result = number * i
        print(f"{number} x {i} = {result}")
n1 = int(input("Digite um numero:"))
# Print the multiplication table for 5, up to 10
print_multiplication_table(n1, 10)
