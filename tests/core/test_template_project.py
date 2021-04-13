import pandas as pd
import pytest
from pandas._testing import assert_frame_equal

from template_project.core.template_project import _strip_capitalize, make_address_book


def test__strip_capitalize() -> None:
    output_str_true = "Aaa Bbb Ccccc"
    output_str = _strip_capitalize(" AAA bBb  ccccc  ")
    assert output_str == output_str_true


def test_make_address_book_return() -> None:
    address_book_true = pd.DataFrame(
        [["Guido, Van Rossum", 3330000000], ["Holger, Krekel", 3331111111]],
        columns=["Name", "Number"],
    )
    address_book = make_address_book(
        [3330000000, 3331111111],
        [" GUIDO  ", " holger "],
        surnames=[" van  rossum ", " KrekeL "],
    )

    assert_frame_equal(address_book, address_book_true)


def test_make_address_book_missing_surnames_return() -> None:
    address_book_true = pd.DataFrame(
        [["Guido", 3330000000], ["Holger", 3331111111]],
        columns=["Name", "Number"],
    )
    address_book = make_address_book(
        [3330000000, 3331111111],
        [" GUIDO  ", " holger "],
        surnames=None,
    )

    assert_frame_equal(address_book, address_book_true)


def test_make_address_book_raise_surnames() -> None:
    with pytest.raises(
        ValueError, match="surnames must be None or have the same length as names"
    ):
        make_address_book(
            [3330000000], [" GUIDO  "], surnames=[" van  rossum ", " KrekeL "]
        )


def test_make_address_book_raise_numbers() -> None:
    with pytest.raises(ValueError, match="numbers must have the same length as names"):
        make_address_book(
            [3330000000, 3331111111],
            [" GUIDO  "],
            surnames=[" van  rossum "],
        )
