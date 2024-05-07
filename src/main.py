import container


if __name__ == "__main__":
    address_str = container.get_address_str()
    print(f"Address: {address_str}")
    # webcrawler = container.get_webcrawler()
    # webcrawler.run()
    webscraper = container.get_webscraper()
    data_dict = container.get_data_wrangler(webscraper.get_li_titles()).run()
    calendar_creater = container.get_calendar_creator(data_dict=data_dict)
    calendar_creater.run()
    print("All done! You can find the calendar data in 'output/calendar_data.csv'.")