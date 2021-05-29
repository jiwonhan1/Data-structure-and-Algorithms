input = 20
output = [2, 3, 5, 7, 11, 13, 17, 19]

def find_prime_list_under_number(number):
    primes = [2]
    for index in range(1, number):
        if index > 1:
            for index2 in range(2, index):
                if (index % index2 == 0):
                    break
                else:
                    primes.append(index)
                    break
    return primes


result = find_prime_list_under_number(input)
print(result)