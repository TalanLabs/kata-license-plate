from typing import List

def compute_central_number(numbers: List[str], nb: int):
    central_number = (int(numbers[1]) + nb) % 999
    if central_number < 10:
        central_number = '00' + str(central_number)
    elif central_number < 100:
        central_number = '0' + str(central_number)
    return str(central_number)

def get_char_by_number(number: int):
    chars = list()
    for i in range(26):
        chars.append(chr(65 + i))
    return chars[number % 26]



def next_license_plate(license_plate: str, nb: int):
    plate_numbers = license_plate.split('-')

    central_number = compute_central_number(plate_numbers, nb)

    ord_last_character = ord(plate_numbers[2][1]) + (int(plate_numbers[1]) + nb) // 999 - 65
    last_character = get_char_by_number(ord_last_character)

    ord_before_last_character = ord(plate_numbers[2][0]) - 65 + ord_last_character // 26
    before_last_character = get_char_by_number(ord_before_last_character)

    ord_second_character = ord(plate_numbers[0][1]) - 65 + ord_before_last_character // 26
    second_character = get_char_by_number(ord_second_character)

    ord_first_character = ord(plate_numbers[0][0]) - 65 + ord_second_character  // 26
    first_character = get_char_by_number(ord_first_character)

    return first_character + second_character + '-' + central_number + '-' + before_last_character + last_character
