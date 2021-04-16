# Electricity prices
The electricity prices dataset can be downloaded from: [transparency.entsoe.eu](https://transparency.entsoe.eu/transmission-domain/r2/dayAheadPrices/show?name=&defaultValue=false&viewType=TABLE&areaType=BZN&atch=false&dateTime.dateTime=16.04.2021+00:00%7CCET%7CDAY&biddingZone.values=CTY%7C10YBE----------2!BZN%7C10YBE----------2&resolution.values=PT60M&dateTime.timezone=CET_CEST&dateTime.timezone_input=CET+(UTC+1)+/+CEST+(UTC+2)).

To use it with our notebook, the yearly csv format should be downloaded for each year. To download the files it is necessary to create an account on [transparency.entsoe.eu](https://transparency.entsoe.eu)

# Weather data
We obtained the weather data from [World Weather Online](https://www.worldweatheronline.com/developer/api/historical-weather-api.aspx)’s historical weather API. For this an API key is needed. However when we did a project a free trial was available. To gather the data and convert it to the right format, two pyton scripts are included in this gist.

# Use on colab
To use the data on Google colab, the obtained data files can be uploaded to a Google drive folder which can be accessed from the notebook.