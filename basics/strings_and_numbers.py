from decimal import Decimal
from fractions import Fraction
from utilities import print_result, print_title


def demo_strings_numbers():
    """
    demo the basic usage of python strings and numbers.
    """
    print_title(1, "Strings and numbers Demo")
    demo_numbers()
    demo_strings()


def demo_numbers():
    print_title(2, "Numbers Demo")
    # -----------------------
    print_title(3, "Real numbers")
    # Demonstrating floating point precision issues
    f1 = 0.1
    f2 = 0.2
    print_result("float: 0.1 + 0.2", f1 + f2, ValueError("precision error"))  # shows floating point precision issues

    # Demonstrating exact decimal arithmetic using Decimal
    d1 = Decimal(0.1)
    d2 = Decimal(0.2)
    print_result("decimal from float: 0.1 + 0.2", d1 + d2, "👎 PRECISION ERROR")  # shows exact decimal arithmetic
    d1 = Decimal("0.1")
    d2 = Decimal("0.2")
    print_result('decimal from string: "0.1" + "0.2"', d1 + d2, "🆗 EXACT")  # shows exact decimal arithmetic

    # Note: 1.23e3 = 1.23 * 10^3 = 1.23 * 1000 = 1230
    d1 = Decimal("-1.23e3")
    print_result(
        # shows exact decimal arithmetic
        f'decimal from string scientific notation: "-1.23e3" ({d1})',
        int(d1),
    )

    # Demonstrating fractions arithmetic
    # -----------------------
    print_title(3, "Fractions")
    f = 0.1 + 0.2
    print_result("float: 0.1 + 0.2", f, ValueError("precision error"))  # shows floating point precision issues
    fr = Fraction(1, 10) + Fraction(2, 10)
    print_result(f"Fraction: 1/10 + 2/10 = {fr}", float(fr), "🆗 no precision error with fractions")  # Résultat : 3/10

    # -----------------------
    print_title(3, "Complex numbers")
    print("Not implemented yet\n")


def demo_strings():
    print_title(2, "Strings Demo")
    print_title(3, "String literals Demo")
    # string literal : multiple lines in a single string
    # -----------------------
    print("""\
line1 (the end of line antislash prevents to insert a new line)
line2 \
line2 continuation
    line3""")

    # string auto-concat : multiple strings in a single line
    # -----------------------
    print_title(3, "Strings auto-concat Demo")
    print(
        "this is a very very long string to demonstrate the auto-concat feature of python :"
        "it only works if the total length of the string is more than the line length limit, which is 120 characters in this case."
    )

    # indexd strings : accessing characters in a string
    # -----------------------
    print_title(3, "Indexed Strings Demo")
    s = "Hello world"
    print_result("first char: s[0]", s[0])
    print_result("last char: s[-1]", s[-1])
    print_result("chars from ... to ... : s[0:2]", s[0:2])  # from 0 to 2 (exclusive)
    print_result("chars from start to ... : s[:2]", s[:2])  # from start to 2 (exclusive)
    print_result("chars from ...  to end : s[2:]", s[2:])  # from 2 (included) to end

    # format strings : progress bar exercise
    # -----------------------
    print_title(3, "Progress Bar Exercise")
    print("This is a progress bar exercise, it should be implemented with a format string.")
    print("Download in Progress:")
    import time  # move import outside the loop for efficiency

    for i in range(0, 101):
        percent = i / 100
        bar = "/" * i + " " * (100 - i)
        print(f"\r[{bar}] {percent:.0%}", end="", flush=True)
        time.sleep(0.05)
    print("\nDownloaded successfully!\n")  # move to next line after progress bar

    print("-" * 30)
    print("TODO: Strings Demo :'https://docs.python.org/3/library/string.html#grammar-token-format-spec-format_spec'")
