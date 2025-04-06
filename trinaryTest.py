def decimalToTrinary(n):
    if n == 0:
        return "0"

    trinaryDigits = []
    while n > 0:
        trinaryDigits.append(str(n % 3))  # Get remainder
        n //= 3  # Update number by integer division

    return ''.join(reversed(trinaryDigits))  # Reverse to get correct order

for n in range(0,20):
    print(decimalToTrinary(n))
