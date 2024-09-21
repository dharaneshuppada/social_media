import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

# Load the data
df = pd.read_csv("Time-Wasters on Social Media.csv")

# Streamlit app title
st.title("Average Time Spent on Social Media Platforms")

# Group data and calculate the mean
mean_time_spent = df.groupby(['Platform'])['Total Time Spent'].mean().sort_values(ascending=False)

# Create a bar plot
plt.figure(figsize=(10, 6))
mean_time_spent.plot(kind='bar', color=['blue', 'green', 'red', 'orange'])
plt.title('Average Total Time Spent on Platform by User')
plt.ylabel('Average Time Spent')

# Show the plot in Streamlit
st.pyplot(plt)

# Optionally, display the data
st.write("Data Summary:")
st.dataframe(mean_time_spent)
