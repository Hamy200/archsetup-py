import requests
import datetime
import json

API_URL = "https://api.aladhan.com/v1/calendar/2025/7?latitude=51.656490&longitude=-0.39032&method=15&shafaq=general&tune=5%2C3%2C5%2C7%2C9%2C-1%2C0%2C8%2C-6&school=0&midnightMode=0&timezonestring=Europe%2FBelfast&latitudeAdjustmentMethod=3&calendarMethod=UAQ"



def main():
    try:
        today = datetime.date.today()
        day = today.day if today.day >= 10 else "0" + str(today.day)
        month = today.month if today.month >= 10 else "0" + str(today.month)
        today_formatted = f"{day}-{month}-{today.year}"
        # print(today_formatted)
        res = requests.get(API_URL).json()["data"]
        
        for entry in res:
            if entry["date"]["gregorian"]["date"] == today_formatted:
                timings = {
                    "Fajr": entry["timings"]["Fajr"].split(" ")[0],
                    "Sunrise": entry["timings"]["Sunrise"].split(" ")[0],
                    "Dhuhr": entry["timings"]["Dhuhr"].split(" ")[0],
                    "Asr": entry["timings"]["Asr"].split(" ")[0],
                    "Maghrib": entry["timings"]["Maghrib"].split(" ")[0],
                    "Isha": entry["timings"]["Isha"].split(" ")[0]
                }
                print(json.dumps({"text": calc_closest_time(timings), "class": "prayer", "alt": generate_table(timings)}))
    except Exception as e:
        print(json.dumps({"text": f"Prayer Script Failed! {e}"}))

def calc_closest_time(timings):
    """Returns a string of text in the format 'PrayerName: Time'"""
    closest={"Name": "", "Num": 9999, "Time": "00:00"}
    current_time = hours_mins_to_num(datetime.datetime.now().strftime("%H:%M"))
    # print(current_time)
    for name, time in timings.items():
        as_minutes = hours_mins_to_num(time)
        calculated_as_minutes = current_time - as_minutes
        if calculated_as_minutes < closest["Num"] :
            closest["Num"] = calculated_as_minutes
            closest["Time"] = time
            closest["Name"] = name
    return f"{closest["Name"]}: {closest["Time"]}"

def hours_mins_to_num(time_string):
    """
    Convert hours and mins to a number for subtraction
    String should be in the format 24HR HH:MM
    """
    hours, minutes = (time_string.split(":")[0], time_string.split(":")[1])
    as_minutes = int(hours)*60 + int(minutes)
    return as_minutes


def generate_table(timings):
    """"Generate a nice table using timings"""
    return (
    f'''Prayer Times
-------------
Fajr:    {timings["Fajr"]}
Sunrise: {timings["Sunrise"]}
Dhuhr:   {timings["Dhuhr"]}
Asr:     {timings["Asr"]}
Maghrib: {timings["Maghrib"]}
Isha:    {timings["Isha"]}''')

if __name__ == "__main__":
    main()