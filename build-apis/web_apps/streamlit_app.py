import streamlit as st
import pandas as pd
# streamlit is a web framework that hosts web apps and data dashboards for us. It runs on a cloud backend so when we
# push something it is available immediately.
# This app is just a simple website with text and some pandas df that we can manipulate in the dashboard

data = {'AA':[1, 2, 3, 4, 5],
        'BB':[10, 20, 30, 40, 50],
        'CC':[100, 200, 300, 400, 500],
        }

df = pd.DataFrame(data)

st.title("Our first streamlit app")
st.subheader("Introducing Streamlit in Udemy - Automate Everything")
st.write("This is our first web app.\nEnjoy it!")

# to deploy we use github - can connect directly on streamlit and tell it to pull from github
# When you push new code to github, it picks it up automatically
st.write(df)
st.line_chart(df)
st.area_chart(df)


myslider = st.slider("Celsius")
st.write(myslider, "in Fahrenheit is", (myslider * 9/5) + 32)