import pandas as pd

def summarize_by_club(sim_df: pd.DataFrame) -> pd.DataFrame:
    """
    Summarizes shot data by club.
    
    Expected columns in sim_df:
    - club
    - carry_x
    - carry_y
    """

    summary = (
        sim_df.groupby("club")
        .agg(
            avg_carry_yds=("carry_x_yds", "mean"),
            std_carry_yds=("carry_x_yds", "std"),
            avg_offline_yds=("carry_y_yds", "mean"),
            std_offline_yds=("carry_y_yds", "std"),
            shot_count=("carry_x_yds", "size")
        )
        .reset_index()
    )

    return summary