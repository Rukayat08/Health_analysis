import pandas as pd 
import streamlit as st
import plotly.express as px

st.title(" Depression  Symptoms in US")
# create a data frame
df = pd.read_csv('depressive-symptoms-across-us-population.csv')
st.write(df)

#DATA INSPECTION 
#To display the first five items
st.markdown('## First Five Arguments')
top = df.head(5)
st.write(top)

#To display the last five items
st.markdown('## Last Five Arguments')
down = df.tail(5)
st.write(down)

#To display details about the data

st.markdown('# Details about the dataset')
details = df.describe()
st.write(details)

#Number of arguments by row
st.markdown('# Summary of Arguments')
details = df.shape
st.table(details)

#Univariate Analysis
duration = df["Nearly every day"].describe()
st.markdown('# Univariate Analysis')
st.markdown('## Hown Often Depression Occurs')
st.write(duration)

weekly_duration = df['Several days'].describe()
st.markdown('## Weekly Occurence')
st.write(weekly_duration)

state = df['Entity'].describe()
st.markdown('## Factors of Depression')
st.write(state)

#Graph Representation

st.title("Graphs")
st.title("Bar Graph")
state = df["Several days"].value_counts()
state.columns = ["Entity", "counts"]
state2 = px.bar(df["Entity"], x = "Entity", title = "Several days")
st.plotly_chart(state2, use_container_width = True)

st.title('Histogram')
Nearly_every_day = px.histogram(df['Nearly every day'], x = "Nearly every day", title = 'Entity')
st.plotly_chart(Nearly_every_day, use_container_width = True)

st.title('Weekly Occurence ')
counted = df["Several days"].value_counts().reset_index()
counted.columns = ["Several days", "count"]
Several_Days = px.pie(counted, names = "Several days", values = "count", title = "Entity")
st.plotly_chart(Several_Days, use_container_width = True)

st.title('Daily Occurence')
counted = df["Nearly every day"].value_counts().reset_index()
counted.columns = ["Nearly every day", "count"]
Duration = px.pie(counted, names = "Nearly every day", values = "count", title = "Entity")
st.plotly_chart(Duration, use_container_width = True)

st.title('NIL OCCURENCE')
counted = df["Not at all"].value_counts().reset_index()
counted.columns = ["Not at all", "count"]
Rate = px.pie(counted, names = "Not at all", values = "count", title = "Entity")
st.plotly_chart(Rate, use_container_width = True)