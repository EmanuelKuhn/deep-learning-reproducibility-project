import os
import string
import time

import requests
from pandas.io import json
import calendar

BASE_URL = "https://api.worldweatheronline.com/premium/v1/past-weather.ashx/"

PARAMETERS = {
    "q": "50.641111,4.668056",  # Middle of belgium: https://en.wikipedia.org/wiki/Geography_of_Belgium#Extreme_points
    "tp": "1",  # Weather hourly
    "format": "json",
    "key": "YOUR_API_KEY"
}


def get_startdate_enddate_for_month(year, month):
    month_number_of_days = calendar.monthrange(year, month)[1]

    start_date = f"{year}-{format(month, '02d')}-01"
    end_date = f"{year}-{format(month, '02d')}-{format(month_number_of_days, '02d')}"

    return start_date, end_date


def request_weather(start_date, end_date):
   
    params = PARAMETERS.copy()

    params["date"] = start_date
    params["enddate"] = end_date

    response = requests.get(BASE_URL, params=params)

    return response


def request_and_save_weather(start_date, end_date):
    response = request_weather(start_date, end_date)

    print(f"status: {response.status_code}")

    if response.text.lower().find("error") != -1:
        print("ERROR:")
        print(response.text)

        with open(f"responses-raw/error_{start_date}_{end_date}_{response.status_code}.json", 'w') as f:
            f.write(response.text)
            f.close()
    else:
        with open(f"responses-raw/weather_{start_date}_{end_date}_{response.status_code}.json", 'w') as f:
            f.write(response.text)
            f.close()


if __name__ == '__main__':
    for year in range(2021, 2022): # Weather until 2020
        for month in range(1, 5):
            start_date, end_date = get_startdate_enddate_for_month(year, month)

            already_exists = os.path.isfile(f"responses-raw/weather_{start_date}_{end_date}_{200}.json")

            if not already_exists:
                request_and_save_weather(start_date, end_date)

                time.sleep(1)
