import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np


URL = st.text_input("Enter Squad URL")
if URL:
  def func_run(URL):
    

    page = requests.get(URL)
    bs = BeautifulSoup(page.content, 'lxml')
    y =bs.find_all('span',class_='ds-text-compact-s ds-font-bold ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block')
    st.title("Squad:")
    for y1 in y:
      st.write(y1.get_text())
  func_run(URL)
