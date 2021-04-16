import json
import os

import pandas as pd
from datetime import datetime

from gather_weather_data import get_startdate_enddate_for_month

PATH_PREFIX = "."
COLUMNS = ["tempC", "windspeedKmph", "cloudcover", "uvIndex"]

def parse(response):

    month_hourly_DF = pd.DataFrame(columns=COLUMNS)

    weather_days = response['data']['weather']

    for weather_day in weather_days:
        date = weather_day["date"]

        # print(date)

        date = pd.to_datetime(date, infer_datetime_format=True).date()

        weather_hours = weather_day['hourly']

        for weather_hour in weather_hours:

            while len(weather_hour["time"]) < 4:
                weather_hour["time"] = f"0{weather_hour['time']}"

            assert len(weather_hour["time"]) == 4, weather_hour["time"]

            time = pd.to_datetime(weather_hour["time"], format="%H%M").time()

            dt = datetime.combine(date, time)

            hour_series = pd.Series(weather_hour, name=dt)

            hour_series = hour_series[COLUMNS]


            month_hourly_DF = month_hourly_DF.append(hour_series)

    month_hourly_DF = month_hourly_DF.sort_index()
    
    return month_hourly_DF

if __name__ == '__main__':

    full_hourly_DF = pd.DataFrame(columns=COLUMNS)


    for year in range(2021, 2022): # Weather until 2020
        for month in range(1, 4):
            print(f"year: {year}, month: {month}")

            start_date, end_date = get_startdate_enddate_for_month(year, month)

            file_path = f"{PATH_PREFIX}/responses-raw/weather_{start_date}_{end_date}_{200}.json"

            response_exists = os.path.isfile(file_path)

            if not response_exists:
                print("QUITTING")
                print(f"No response with {start_date}, {end_date} exists")
                exit(-1)

            response = pd.read_json(file_path)

            monthly_df = parse(response)

            full_hourly_DF = full_hourly_DF.append(monthly_df)

        full_hourly_DF.index.name = "Date"

        full_hourly_DF.to_csv(f"Weather_{year}.csv")

    print(full_hourly_DF.head())
    print(len(full_hourly_DF))
