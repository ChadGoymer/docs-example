from pathlib import Path

import polars as pl
import pytest
from polars.testing import assert_frame_equal

from calculator.df_calculations import add_csv, add_db, add_df


@pytest.fixture
def test_df():
    return pl.DataFrame(
        {
            "X": ["A", "B", "C"],
            "Y": [1, 2, 3],
        }
    )


class TestAddDF:
    def test_add_integer(self, test_df):
        expected_data = pl.DataFrame(
            {
                "X": ["A", "B", "C"],
                "Y": [2, 3, 4],
            }
        )

        assert_frame_equal(add_df(test_df, 1), expected_data)

    def test_add_float(self, test_df):
        expected_data = pl.DataFrame(
            {
                "X": ["A", "B", "C"],
                "Y": [2.0, 3.0, 4.0],
            }
        )

        assert_frame_equal(add_df(test_df, 1.0), expected_data)


@pytest.fixture
def test_csv():
    temp_csv = Path("./temp.csv")
    pl.DataFrame(
        {
            "X": ["A", "B", "C"],
            "Y": [1, 2, 3],
        }
    ).write_csv(temp_csv.name)
    yield temp_csv
    temp_csv.unlink()


class TestAddCSV:
    def test_add_integer(self, test_csv):
        expected_data = pl.DataFrame(
            {
                "X": ["A", "B", "C"],
                "Y": [2, 3, 4],
            }
        )

        assert_frame_equal(add_csv(test_csv, 1), expected_data)


@pytest.fixture
def mock_polars_read_database(monkeypatch):
    def mock_read_database(*args, **kwargs):
        return pl.DataFrame(
            {
                "X": ["A", "B", "C"],
                "Y": [1, 2, 3],
            }
        )

    monkeypatch.setattr(pl, "read_database", mock_read_database)


class TestAddDB:
    def test_add_integer(self, mock_polars_read_database):
        expected_data = pl.DataFrame(
            {
                "X": ["A", "B", "C"],
                "Y": [2, 3, 4],
            }
        )

        assert_frame_equal(add_db(test_csv, 1), expected_data)
