from typing import Optional, Sequence

import pandas as pd


def _strip_capitalize(input_str: str) -> str:
    """Remove excess spaces and capitalize the first or last name(s)/."""
    output_str = " ".join([s.capitalize() for s in input_str.split()])
    return output_str


def make_address_book(
    numbers: Sequence[int],
    names: Sequence[str],
    surnames: Optional[Sequence[str]] = None,
    sep: str = ", ",
) -> pd.DataFrame:
    """A simple function to create an address book.

    A simple function to create an address book starting from a sequence of names,
    surnames and, optionally, surnames.

    Args:
        names: Contact names.
        numbers: Contact telephone numbers.
        surnames: Optional; Contact surnames.
        sep: Optional; Separator used to join first and last names. This parameter is
          ignored if surnames are not provided.

    Returns:
        The address book.
    """
    # Block comments generally apply to some (or all) code that follows them, and are
    # indented to the same level as that code. Each line of a block comment starts with
    # a # and a single space (unless it is indented text inside the comment).
    #
    # Paragraphs inside a block comment are separated by a line containing a single #.
    names = [_strip_capitalize(name) for name in names]
    if surnames is not None:  # Use inline comments sparingly.
        if len(names) != len(surnames):
            raise ValueError("surnames must be None or have the same length as names")

        surnames = [_strip_capitalize(surname) for surname in surnames]
        names = [sep.join([name, surname]) for name, surname in zip(names, surnames)]

    if len(names) != len(numbers):
        raise ValueError("numbers must have the same length as names")

    address_book = pd.DataFrame(zip(names, numbers), columns=["Name", "Number"])
    return address_book
