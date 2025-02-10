# calculator/calculations.py
import polars as pl


def add_df(a, b):
    return a.with_columns(Y=pl.col("Y") + pl.lit(b))


def add_csv(f, b):
    df = pl.read_csv(f)
    return add_df(df, b)


def add_db(f, b, con=None):
    df = pl.read_database("SELECT * FROM table", connection=con)
    return add_df(df, b)
