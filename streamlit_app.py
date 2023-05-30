import streamlit as st
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import numpy as np

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

URL = st.text_input("Enter Squad URL")
if URL:
  def func_run(URL):
    import requests
    from bs4 import BeautifulSoup
    import pandas as pd
    import re
    import numpy as np

    page = requests.get(URL)
    bs = BeautifulSoup(page.content, 'lxml')
    y =bs.find_all('span',class_='ds-text-title-m ds-font-bold ds-text-typo ds-underline ds-decoration-ui-stroke hover:ds-text-typo-primary hover:ds-decoration-ui-stroke-primary ds-block')
    for y1 in y:
      st.write(y1.get_text())
  func_run(URL)
