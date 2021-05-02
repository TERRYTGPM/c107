import pandas as pd
import plotly.graph_objects as e
import csv

df = pd.read_csv("data.csv")
studentdf = df.loc[df["student_id"]=="TRL_xyz"]

print(df.groupby("level")["attempt"].mean())

fig = e.Figure(e.Bar(
    x=studentdf.groupby("level")["attempt"].mean(),
    y=["Level 1", "Level 2", "Level 3", "Level 4"],
    orientation="h"
))
fig.show()