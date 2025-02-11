# calculator/df_calculations.py

import pandera.polars as pa
import polars as pl
from pydantic import ConfigDict, validate_call


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
def add_df(a: pl.DataFrame, b: int | float):
    schema = pa.DataFrameSchema(
        {
            "X": pa.Column(str),
            "Y": pa.Column(int),
        }
    )

    return schema.validate(a).with_columns(Y=pl.col("Y") + pl.lit(b))


def add_csv(f, b):
    df = pl.read_csv(f)
    return add_df(df, b)


def add_db(f, b, con=None):
    df = pl.read_database("SELECT * FROM table", connection=con)
    return add_df(df, b)
