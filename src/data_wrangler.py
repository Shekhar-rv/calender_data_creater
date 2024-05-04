from datetime import datetime

calendar_data = [
    'Wednesday 1, May 2024 - Brown Bin', 'Wednesday 8, May 2024 - Black Bin',
    'Wednesday 15, May 2024 - Blue Bin', 'Wednesday 22, May 2024 - Black Bin',
    'Wednesday 29, May 2024 - Brown Bin', 'Wednesday 5, June 2024 - Black Bin',
    'Wednesday 12, June 2024 - Blue Bin', 'Wednesday 19, June 2024 - Black Bin',
    'Wednesday 26, June 2024 - Brown Bin', 'Wednesday 3, July 2024 - Black Bin',
    'Wednesday 10, July 2024 - Blue Bin', 'Wednesday 17, July 2024 - Black Bin',
    'Wednesday 24, July 2024 - Brown Bin', 'Wednesday 31, July 2024 - Black Bin',
    'Wednesday 7, August 2024 - Blue Bin', 'Wednesday 14, August 2024 - Black Bin',
    'Wednesday 21, August 2024 - Brown Bin', 'Wednesday 28, August 2024 - Black Bin',
    'Wednesday 4, September 2024 - Blue Bin', 'Wednesday 11, September 2024 - Black Bin',
    'Wednesday 18, September 2024 - Brown Bin', 'Wednesday 25, September 2024 - Black Bin',
    'Wednesday 2, October 2024 - Blue Bin', 'Wednesday 9, October 2024 - Black Bin',
    'Wednesday 16, October 2024 - Brown Bin', 'Wednesday 23, October 2024 - Black Bin',
    'Wednesday 30, October 2024 - Blue Bin', 'Wednesday 6, November 2024 - Black Bin',
    'Wednesday 13, November 2024 - Brown Bin', 'Wednesday 20, November 2024 - Black Bin',
    'Wednesday 27, November 2024 - Blue Bin', 'Wednesday 4, December 2024 - Black Bin',
    'Wednesday 11, December 2024 - Brown Bin', 'Wednesday 18, December 2024 - Black Bin',
    'Wednesday 25, December 2024 - Blue Bin', 'Wednesday 1, January 2025 - Black Bin',
    'Wednesday 8, January 2025 - Brown Bin', 'Wednesday 15, January 2025 - Black Bin',
    'Wednesday 22, January 2025 - Blue Bin', 'Wednesday 29, January 2025 - Black Bin',
    'Wednesday 5, February 2025 - Brown Bin', 'Wednesday 12, February 2025 - Black Bin',
    'Wednesday 19, February 2025 - Blue Bin', 'Wednesday 26, February 2025 - Black Bin',
    'Wednesday 5, March 2025 - Brown Bin', 'Wednesday 12, March 2025 - Black Bin',
    'Wednesday 19, March 2025 - Blue Bin', 'Wednesday 26, March 2025 - Black Bin',
    'Wednesday 2, April 2025 - Brown Bin', 'Wednesday 9, April 2025 - Black Bin',
    'Wednesday 16, April 2025 - Blue Bin', 'Wednesday 23, April 2025 - Black Bin'
]

# calender_dates = [x.split(' - ')[0] for x in calender_data]
calendar_dates = [datetime.strptime(
    x.split(' - ')[0], '%A %d, %B %Y') for x in calendar_data]
calendar_day = [x.split(' ')[0] for x in calendar_data]
bin_color = [x.split(' - ')[1] for x in calendar_data]

# Create a list of dictionaries
calendar_list = [{'calendar_date': date, 'calendar_day': day, 'bin_color': color}
                 for date, day, color in zip(calendar_dates, calendar_day, bin_color)]

print(calendar_list)


[{'calendar_date': datetime.datetime(2024, 5, 1, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2024, 5, 8, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 5, 15, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2024, 5, 22, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 5, 29, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2024, 6, 5, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 6, 12, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2024, 6, 19, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 6, 26, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2024, 7, 3, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 7, 10, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2024, 7, 17, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 7, 24, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2024, 7, 31, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 8, 7, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2024, 8, 14, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 8, 21, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2024, 8, 28, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 9, 4, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2024, 9, 11, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 9, 18, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2024, 9, 25, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 10, 2, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2024, 10, 9, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 10, 16, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2024, 10, 23, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {
    'calendar_date': datetime.datetime(2024, 10, 30, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2024, 11, 6, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 11, 13, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2024, 11, 20, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 11, 27, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2024, 12, 4, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 12, 11, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2024, 12, 18, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2024, 12, 25, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2025, 1, 1, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2025, 1, 8, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2025, 1, 15, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2025, 1, 22, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2025, 1, 29, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2025, 2, 5, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2025, 2, 12, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2025, 2, 19, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2025, 2, 26, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2025, 3, 5, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2025, 3, 12, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2025, 3, 19, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2025, 3, 26, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2025, 4, 2, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Brown Bin'}, {'calendar_date': datetime.datetime(2025, 4, 9, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}, {'calendar_date': datetime.datetime(2025, 4, 16, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Blue Bin'}, {'calendar_date': datetime.datetime(2025, 4, 23, 0, 0), 'calendar_day': 'Wednesday', 'bin_color': 'Black Bin'}]
