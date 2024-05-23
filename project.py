import yfinance as yf
import pandas as pd
import requests
from bs4 import BeautifulSoup
import plotly.graph_objects as go
from plotly.subplots import make_subplots
def make_graph(stock_data, revenue_data, stock):
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, subplot_titles=("Historical Share Price", "Historical Revenue"), vertical_spacing = .3)
    fig.add_trace(go.Scatter(x=pd.to_datetime(stock_data.Date, infer_datetime_format=True), y=stock_data.Close.astype("float"), name="Share Price"), row=1, col=1)
    fig.add_trace(go.Scatter(x=pd.to_datetime(revenue_data.Date, infer_datetime_format=True), y=revenue_data.Revenue.astype("float"), name="Revenue"), row=2, col=1)
    fig.update_xaxes(title_text="Date", row=1, col=1)
    fig.update_xaxes(title_text="Date", row=2, col=1)
    fig.update_yaxes(title_text="Price ($US)", row=1, col=1)
    fig.update_yaxes(title_text="Revenue ($US Millions)", row=2, col=1)
    fig.update_layout(showlegend=False,
    height=900,
    title=stock,
    xaxis_rangeslider_visible=True)
    fig.show()
    

# use yfinance 
Tesla = yf.Ticker("TSLA")
Tesla_data = Tesla.history(period="max")

Tesla_data.reset_index(inplace=True)
Tesla_data.head()

# Use Webscraping to Extract Tesla Revenue Data
url = " https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"
html_data = requests.get(url).text
import yfinance as yf

# Use yfinance to Extract Stock Data for Tesla
Tesla = yf.Ticker("TSLA")
Tesla_data = Tesla.history(period="max")

# Reset the index of the dataframe
Tesla_data.reset_index(inplace=True)

# Display the first five rows of the tesla_data dataframe
print(Tesla_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume', 'Dividends', 'Stock Splits']].head())
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage containing Tesla's revenue data
url = "https://www.macrotrends.net/stocks/charts/TSLA/tesla/revenue"

# Use requests library to download the webpage and save the text of the response as html_data
html_data = requests.get(url).text

# Parse the html data using BeautifulSoup
soup = BeautifulSoup(html_data, "html.parser")

# Find the table with Tesla Quarterly Revenue and store it into a dataframe named tesla_revenue
table_index = 0
tables = soup.find_all('table')
for index, table in enumerate(tables):
    if "Tesla Quarterly Revenue" in str(table):
        table_index = index

tesla_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if col != []:
        Date = col[0].text
        Revenue = col[1].text.replace("$", "").replace(",", "")
        tesla_revenue = tesla_revenue.append({"Date": Date, "Revenue": Revenue}, ignore_index=True)

# Remove the rows in the dataframe that are empty strings or are NaN in the Revenue column
tesla_revenue = tesla_revenue[tesla_revenue['Revenue'] != ""]

# Print the entire tesla_revenue DataFrame
print(tesla_revenue)
# Call the make_graph function with Tesla stock data and revenue data
make_graph(Tesla_data, tesla_revenue, 'Tesla')

import yfinance as yf

# Use Ticker function to create a ticker object for GameStop with ticker symbol GME
gme = yf.Ticker("GME")

# Extract stock information and save it in a dataframe named gme_data
gme_data = gme.history(period="max")

# Reset the index of the dataframe
gme_data.reset_index(inplace=True)

# Display the first five rows of the gme_data dataframe
print(gme_data.head())
import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the webpage containing GameStop's revenue data
url = "https://www.macrotrends.net/stocks/charts/GME/gamestop/revenue"

# Use requests library to download the webpage and save the text of the response as html_data
html_data = requests.get(url).text

# Parse the html data using BeautifulSoup
soup = BeautifulSoup(html_data, "html.parser")

# Extract the table with GameStop Quarterly Revenue and store it into a dataframe named gme_revenue
tables = soup.find_all('table')
for index, table in enumerate(tables):
    if "GameStop Quarterly Revenue" in str(table):
        table_index = index

gme_revenue = pd.DataFrame(columns=["Date", "Revenue"])
for row in tables[table_index].tbody.find_all("tr"):
    col = row.find_all("td")
    if col != []:
        Date = col[0].text
        Revenue = col[1].text.replace("$", "").replace(",", "")
        gme_revenue = gme_revenue.append({"Date": Date, "Revenue": Revenue}, ignore_index=True)

# Display the last five rows of the gme_revenue dataframe
print(gme_revenue.tail())
make_graph(gme_data, gme_revenue, 'GameStop')



