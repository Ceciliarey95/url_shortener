import pyshorteners
import streamlit as st

#url_shorted
def shorten_url(url):
    short = pyshorteners.Shortener()
    shortened_url = short.tinyurl.short(url)
    return shortened_url

#app_web
st.set_page_config(page_title="URL Shortener", layout="centered")
st.title("URL shortener")
url = st.text_input("Enter the URL: ")
if st.button("Generate new URL"):
    st.write("URL shortened: ",shorten_url(url))