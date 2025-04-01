import sys


def is_punctuation(c: str) -> bool:
    """Check if a character is a punctuation mark."""
    punctuations = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return c in punctuations


def count_characters(text: str):
    """
    Counts the number of uppercase letters, lowercase letters,
    punctuation marks, spaces, and digits in the given text.

    Args:
        text (str): The input text to analyze.

    Returns:
        tuple: A tuple containing counts of uppercase
        letters, lowercase letters, punctuation marks,
        spaces, and digits.
    """
    upper_count = 0
    lower_count = 0
    punctuation_count = 0
    space_count = 0
    digit_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        elif is_punctuation(char):
            punctuation_count += 1
        elif char.isspace():
            space_count += 1
        elif char.isdigit():
            digit_count += 1

    return (upper_count, lower_count, punctuation_count,
            space_count, digit_count)


def main():
    """
    Main function to process command-line input and count character types
    in the provided text.
    """
    if len(sys.argv) != 2:
        if len(sys.argv) > 2:
            raise AssertionError("more than one argument is provided")
        else:
            raise AssertionError("missing argument")

    text = sys.argv[1]
    counts = count_characters(text)
    uppers, lowers, punctuations, spaces, digits = counts
    total_characters = len(text)

    print(f"The text contains {total_characters} characters:")
    print(f"{uppers} upper letters")
    print(f"{lowers} lower letters")
    print(f"{punctuations} punctuation marks")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    """
    Entry point of the script. Handles exceptions and calls the main function.
    """
    try:
        main()
    except AssertionError as e:
        print(f"AssertionError: {e}")
