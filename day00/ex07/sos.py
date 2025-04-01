import sys


def encode_morse(input_str):
    """
    Encodes a string into Morse code.
    Args:
        input_str (str): The input string to encode.
    Returns:
        str: The Morse code representation of the input string.
    """
    NESTED_MORSE = {
        " ": "/ ",
        "A": ".- ",
        "B": "-... ",
        "C": "-.-. ",
        "D": "-.. ",
        "E": ". ",
        "F": "..-. ",
        "G": "--. ",
        "H": ".... ",
        "I": ".. ",
        "J": ".--- ",
        "K": "-.- ",
        "L": ".-.. ",
        "M": "-- ",
        "N": "-. ",
        "O": "--- ",
        "P": ".--. ",
        "Q": "--.- ",
        "R": ".-. ",
        "S": "... ",
        "T": "- ",
        "U": "..- ",
        "V": "...- ",
        "W": ".-- ",
        "X": "-..- ",
        "Y": "-.-- ",
        "Z": "--.. ",
        "0": "----- ",
        "1": ".---- ",
        "2": "..--- ",
        "3": "...-- ",
        "4": "....- ",
        "5": "..... ",
        "6": "-.... ",
        "7": "--... ",
        "8": "---.. ",
        "9": "----. "
    }

    if not all(char.upper() in NESTED_MORSE for char in input_str):
        raise AssertionError("the arguments are bad")

    encode_str = ""
    for char in input_str:
        encode_str += NESTED_MORSE[char.upper()]

    return encode_str


def main():
    """ Main function to process command-line input
    and encode to Morse code."""
    if len(sys.argv) != 2:
        raise AssertionError("the arguments are bad")

    input_str = sys.argv[1]

    morse_code = encode_morse(input_str)
    print(morse_code)


if __name__ == "__main__":
    """ Main entry point for the script."""
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
