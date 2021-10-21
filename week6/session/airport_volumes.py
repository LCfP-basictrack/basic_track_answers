import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# read the dataset and inspect it - make sense of what this means

df = pd.read_csv(r"../pdf/covid_impact_on_airport_traffic.csv")
print(df.columns)
print(df.shape)

# some basic stats - there is only a single numerical column in the data frame
# we will get results only for this

print(df.describe())
# only numbers as output

# see first which countries are in the data set

print(df["Country"].unique())

# let us visualize the airport utilization per country using horizontal bar plots

sns.set(font_scale=2)
plt.figure(figsize=(12, 5))
plt.title("COUNTRY VS PERCENT OF BASELINE")
sns.barplot(data=df, y="Country", x="PercentOfBaseline")
plt.show()

# or with a vertical bar plot
sns.set(font_scale=1.2)
plt.figure(figsize=[10, 7])
sns.barplot(data=df, x='Country', y='PercentOfBaseline', palette='GnBu_r')
plt.ylabel('Percent of baseline')
plt.show()

# or with a boxplot
plt.figure(figsize=(10, 5))
sns.boxplot(data=df, x="Country", y="PercentOfBaseline")
plt.show()

# or a pie chart
plt.figure(figsize=(15, 15))
df.Country.value_counts().plot(kind='pie', legend=True)
plt.xlabel("Daily data entries of all airports per country")
plt.show()

# now per city
print(df["City"].unique())
print(len(df["City"].unique()))

sns.set(font_scale=2)
plt.figure(figsize=(24, 22))
sns.barplot(y=df.City, x=df.PercentOfBaseline, capsize=.2, palette="Blues_d")
plt.title("City VS PercentOfBaseline")
plt.show()

# now per airport
print(df["AirportName"].unique())
print(len(df["AirportName"].unique()))

sns.set(font_scale=3)
plt.figure(figsize=(25, 16))
sns.barplot(x=df.PercentOfBaseline, y=df.AirportName, palette="Blues_d", capsize=.2)
plt.show()

# scatter plot per state
print(df["State"].unique())
print(len(df["State"].unique()))

sns.set(font_scale=2)
plt.figure(figsize=(32, 26))
sns.scatterplot(y=df.State, x=df.PercentOfBaseline, s=200)
plt.show()

# temporal linear visualisations per country
# first reformat the date
df['date_parsed'] = pd.to_datetime(df['Date'], format="%Y-%m-%d")

plt.figure(figsize=(20, 5))
sns.lineplot(data=df, x="date_parsed", y="PercentOfBaseline", hue="Country", ci=None)
plt.show()

# only for Australia
group_country = df.groupby('Country')
country_Aus = group_country.get_group('Australia')
plt.figure(figsize=(20, 5))
sns.lineplot(data=country_Aus, x="date_parsed", y="PercentOfBaseline")
plt.show()

# on a map - a bit more complex thingy with plotly express - output is given in the default browser

df["lon"] = df.Centroid.apply(lambda x: x.split(" ")[0].replace("POINT(", " "))
df["lat"] = df.Centroid.apply(lambda x: x.split(" ")[1].replace(")", " "))

df1 = df.groupby(["Country", "City", 'lat', 'lon'])['PercentOfBaseline'].mean().sort_values(
    ascending=False).reset_index()
fig = px.scatter_geo(df1,
                     lat='lat',
                     lon='lon',
                     hover_name="Country",
                     color='Country',
                     hover_data=['PercentOfBaseline', "City"],
                     labels={"PercentOfBaseline": "Percent of Baseline"}

                     )

fig.update_geos(showocean=True,
                oceancolor='LightCyan',
                lakecolor='LightSteelBlue',
                showlakes=True,

                )
fig.show()
