import polars as pl
import calculator as calc

calc.add(1, 1)
calc.add(1.0, 1.0)

calc.add(3, "x")
calc.add(3, "2")

calc.add(-1, 1)


df = pl.DataFrame(
    {
        "X": ["A", "B", "C"],
        "Y": [1, 2, 3],
    }
)

calc.add_df(df, 1)
calc.add_df(1, 1)
