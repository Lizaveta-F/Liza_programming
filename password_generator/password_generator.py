import random
digits = '0123456789'
lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
ambSymb = 'il1Lo0O'
chars = []
amount_passwords = int(
    input("Please, enter the amount of passwords you want to generate: "))
length_passwords = int(
    input("Please, enter the length of the passwords you want to generate: "))
ifDigits = input(
    f"Please, clarify whether to include digits {digits} in the password (yes/no): ")
ifUpcase = input(
    f"Please, clarify whether to include Upper case letters {uppercase_letters} in the password (yes/no): ")
ifLower = input(
    f"Please, clarify whether to include Lower case letters {lowercase_letters} in the password (yes/no): ")
ifSymbols = input(
    f"Please, clarify whether to include Symbols {punctuation} in the password (yes/no): ")
ifExclude = input(
    f"Please, clarify whether to exclude ambiguous symbols {ambSymb} from the password (yes/no): ")
if ifDigits.lower() == 'yes':
    chars.append(digits)
if ifUpcase.lower() == 'yes':
    chars.append(uppercase_letters)
if ifLower.lower() == 'yes':
    chars.append(lowercase_letters)
if ifSymbols.lower() == 'yes':
    chars.append(punctuation)


chars_new = "".join(chars)


if ifExclude.lower() == 'yes':
    for i in ambSymb:
        if i in chars_new:
            chars_new = chars_new.replace(i, "")


def generate_password(length, chars):
    password = ""
    for _ in range(length):
        password += random.choice(chars)
    return password


for _ in range(amount_passwords):
    print(generate_password(length_passwords, chars_new))
