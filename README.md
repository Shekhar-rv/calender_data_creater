# Create a calender file to import bin collection date
The aim of this project was to remind me which days and which bins do I need to take out on the respective bin collection dates. I'm aware that there is an app for this, I thought there wasn't a need for an app itself as my need was just a reminder and I could achieve the same using the in-build calender app on the phone. To achieve this I scrape the data of all the data required such as the dates, color of the bin and create a csv file that I can import onto my google calendar.

## Approach 
1. Check city council website (Sheffield) to see if you can get the data from website. You need to input the postcode and then select the address (Need to test this)
    ```link
    https://wasteservices.sheffield.gov.uk/
    ```
2. What format are calender files and what data can we feed it to construct the file.
    ```link
    https://support.google.com/calendar/answer/37118?hl=EN#zippy=%2Ccreate-or-edit-an-icalendar-file
    ```

## To Do
1. Get the selenium crawler working, as of now I have manually saved the html file and scraped from that. Need to bypass recapta!
2. Write tests for possible function.
3. Check test coverage.
