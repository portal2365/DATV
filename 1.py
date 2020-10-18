
import pandas as pd

import csv

import plotly.express as px


df = pd.read_csv("data.csv")

mean = df.groupby(["the_students_id", "level"], as_index=False)["attempt"].mean()

fig = px.scatter(mean, a="the_students_id", b="level", size="attempt", color="attempt")
fig.show()