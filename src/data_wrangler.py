from datetime import datetime
from typing import List


class DataWrangler:
    def __init__(self, calendar_data: List[str]):
        self.calendar_data = calendar_data

    def run(self):
        print("Wrangling the data.")
        start_date = [datetime.strptime(x.split(' - ')[0], '%A %d, %B %Y') for x in self.calendar_data]
        calendar_day = [x.split(' ')[0] for x in self.calendar_data]
        subject = [f"Take out the {x.split(' - ')[1]}" for x in self.calendar_data]
        description = [f"Take out the {x.split(' - ')[1]} before 7AM on {calendar_day[0]}!" for x in self.calendar_data]
        print("Data wrangling complete.")
        return [
            {'subject': subject, 'start_date': start_date, 'description': description}
            for subject, start_date, description in zip(subject, start_date, description)
        ]
        
