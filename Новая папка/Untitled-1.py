def count_digits(n):

    digit_count = {str(i): 0 for i in range(10)}
    
    
    for digit in str(n):
        if digit in digit_count:
            digit_count[digit] += 1
    
    for digit, count in sorted(digit_count.items()):
        if count > 0:
            print(f"{digit} - {count}")


number = int(input("Enter a float number: "))
count_digits(number)
