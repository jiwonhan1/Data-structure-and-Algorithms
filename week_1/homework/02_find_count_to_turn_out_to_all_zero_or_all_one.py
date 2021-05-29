input = "0001100"

def find_count_to_turn_out_to_all_zero_or_all_one(string):
    zeroCount = 0
    oneCount = 0
    arrString = list(string)
    # case for 0
    for index in range(len(arrString)):
        if index == len(arrString) -1:
            if arrString[index -1] == "1" and arrString[index] == "0":
                zeroCount += 1;
        elif arrString[index + 1] == "1" and arrString[index] == "0":
            zeroCount += 1;
    # case for 1
    for index in range(len(arrString)):
        if index == len(arrString) -1:
            if arrString[index -1]== "0" and arrString[index] == "1":
                oneCount += 1;
        elif arrString[index + 1] == "0" and arrString[index] == "1":
                oneCount += 1
    if (zeroCount > oneCount): return oneCount
    else: return zeroCount


result = find_count_to_turn_out_to_all_zero_or_all_one(input)
print(result)