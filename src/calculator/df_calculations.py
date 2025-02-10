# calculator/calculations.py

import pandera.polars as pa
import polars as pl
from pandera.typing.polars import DataFrame
from pydantic import BaseModel, ConfigDict, validate_call


class Schema(pa.DataFrameModel):
    X: str = pa.Field(unique=True)
    Y: int = pa.Field(in_range={"min_value": 0, "max_value": 10})


class DataFrameModel(BaseModel, arbitrary_types_allowed=True):
    df: DataFrame[Schema]


@validate_call(config=ConfigDict(arbitrary_types_allowed=True))
def add_df(a: DataFrameModel, b: int | float):
    return a.with_columns(Y=pl.col("Y") + pl.lit(b))


def add_csv(f, b):
    df = pl.read_csv(f)
    return add_df(df, b)


def add_db(f, b, con=None):
    df = pl.read_database("SELECT * FROM table", connection=con)
    return add_df(df, b)
