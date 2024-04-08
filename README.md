# Create a calender file to import bin collection date



## Approach 
1. Check city council website (Sheffield) to see if you can get the data from website
	1. You need to input the postcode and then select the address (Need to test this)
        ```link
        https://wasteservices.sheffield.gov.uk/
        ```
2. What format are calender files and what data can we feed it to construct the file.
    ```link
    https://support.google.com/calendar/answer/37118?hl=EN#zippy=%2Ccreate-or-edit-an-icalendar-file
    ```

## Implementation ideas
1. Find a good scrapper/crawler to get the data from the website.
2. Decide the approach to handle the data (should you hold it in memory or as a csv)
3. From the csv construct the ics file (decide if you want to use the ics or csv)
4. The postcode, flat/house number, street name, and city should be environment variables