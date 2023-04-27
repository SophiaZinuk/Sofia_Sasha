def roman_to_int(roman: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    summ = 0
    i = 0
    while i < len(roman):
        a1 = roman_dict.get(roman[i])
        if i == len(roman) - 1:
            summ += roman_dict.get(roman[i])
            break
        a2 = roman_dict.get(roman[i+1])
        if a1 >= a2:
            summ += roman_dict.get(roman[i])
            i += 1
        else:
            summ += roman_dict.get(roman[i+1]) - roman_dict.get(roman[i])
            i += 2
    return summ



def roman_to_int_v2(roman_num: str) -> int:
    roman_dict = {"I": 1, "V": 5, "X": 10,
                  "L": 50, "C": 100, "D": 500, "M": 1000}
    
    result_num = prev_digit = 0

    for digit in map(lambda x : roman_dict[x], reversed(roman_num)):
        if digit < prev_digit:
            result_num -= digit
        else:
            result_num += digit

        prev_digit = digit

    return result_num




print(roman_to_int_v2("MCMXCIV"))
# result1 = roman_to_int_v2("MCMXCIV")
# assert result1 == 1994
