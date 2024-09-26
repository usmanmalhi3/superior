def luhn_check(card_number):
    card_number = [int(digit) for digit in str(card_number)]
 
    card_number.reverse()

    for i in range(1, len(card_number), 2):
        card_number[i] *= 2
        if card_number[i] > 9:
            card_number[i] -= 9

    
    return sum(card_number) % 10 == 0


card_number = input("Enter a card number to validate: ")
if luhn_check(card_number):
    print("The card number is valid.")
else:
    print("The card number is invalid.")
