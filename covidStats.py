import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import plotly.express as px

data = pd.read_csv('data/covid_19_data.csv')
print(data.head())

# interprete column data as int
data[["Confirmed", "Deaths", "Recovered"]] = data[["Confirmed", "Deaths", "Recovered"]].astype(int)

# simply replace name "Mainland China" with just "China"
data['Country/Region'] = data['Country/Region'].replace('Mainland China', 'China')

# create new category "Active_cases"
data['Active_case'] = data['Confirmed'] - data['Deaths'] - data['Recovered']

# create a new data frame starting at the latest update
Data = data[data['ObservationDate'] == max(data['ObservationDate'])].reset_index()

# don't really know it is necessary to use .groupby() when there is only one group (latest date) available
Data_world = Data.groupby(["ObservationDate"])["Confirmed", "Active_case", "Recovered", "Deaths"].sum().reset_index()
print(Data_world)

# creating pie chart of active, recovered and death cases worldwide
labels = ["Active cases", "Recovered", "Deaths"]
values = Data_world.loc[0, ["Active_case", "Recovered", "Deaths"]]
fig = px.pie(Data_world, values=values, names=labels, color_discrete_sequence=['royalblue', 'lightcyan', 'darkblue'])
fig.update_layout(
    title='Total cases : ' + str(Data_world["Confirmed"][0]),
)
fig.show()
