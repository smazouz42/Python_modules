import sys
from ft_filter import ft_filter

def contains_no_special_chars(s: str) -> bool:
    """Checks if the given string contains only
    alphanumeric characters and spaces."""
    for char in s:
        if not (char.isalnum() or char.isspace()):
            return False
    return True

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        sys.exit(1)
    try:
        num = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the second argument is not an integer")
        sys.exit(1)

    input_str = sys.argv[1]
    input_str = input_str.split(" ")
    filtered_words = list(ft_filter(contains_no_special_chars, input_str))
    final_list = [word for word in filtered_words if (lambda x: len(x) > num)(word)]
    print(final_list)
