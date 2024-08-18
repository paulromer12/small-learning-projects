# todo: known issue, the code doesn't keep the spaces in the words

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
translation_dict = {
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--.."
}

# translate from English to Morris Code:
def translate_to_morris(english_str):
    morris_code = ""
    for char in english_str.lower():
        if char == ' ':
            continue
        elif char in translation_dict:
            morris_code += translation_dict[char] + " "
        else:
            print(f"Warning: Character '{char}' not found in Morris Code dictionary.")
    return morris_code

# translate from Morris Code to English:
def translate_to_english(morris_str):
    english = ""
    for code in morris_str.split():
        if code == '0':
            english += " "
        elif code in translation_dict.values():
            key = [k for k, v in translation_dict.items() if v == code]
            english += key[0]
        else:
            print(f"Warning: Code '{code}' not found in Morris Code dictionary.")
    return english

input_str = input('Enter the english or morris code you want translated? ')

try:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    if input_str[0].lower() in alphabet:
        print(translate_to_morris(input_str))
    else:
        print(translate_to_english(input_str))
except ValueError as e:
    print(f"Error: {e}")
