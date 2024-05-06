from pandas import DataFrame
import datetime
from typing import List, Dict


class CalendarCreator:
    def __init__(self, data_dict: List[Dict]):
        self.df = DataFrame(data_dict)

    def create_calendar(self):
        self.df["end_date"] = self.df['start_date']
        self.df["start_time"] = "12:00 AM"
        self.df["end_time"] = "11:59 PM"
        self.df["all_day_event"] = "True"
        self.df["location"] = "Home"
        self.df["private"] = "True"
        print("Added all additional columns to the DataFrame.")
    
    def rename_columns(self):
        self.df = self.df.rename(columns={
            'subject': 'Subject',
            'start_date': 'Start Date',
            'start_time': 'Start Time',
            'end_date': 'End Date',
            'end_time': 'End Time',
            'all_day_event': 'All Day Event',
            'description': 'Description',
            'location': 'Location',
            'private': 'Private'
        })
        print("Renamed all columns in the DataFrame.")

    def save_calendar(self):
        self.df.to_csv("output/calendar_data.csv", index=False)
        print("Saved the calendar data to a CSV file.")

    def run(self):
        self.create_calendar()
        self.rename_columns()
        self.save_calendar()
