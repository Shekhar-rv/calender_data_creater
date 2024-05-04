import container


if __name__ == "__main__":
    address_str = container.get_address_str()
    print(f"Address: {address_str}")
    # webcrawler = container.get_webcrawler()
    # webcrawler.run()
    webscraper = container.get_webscraper()
    print(webscraper.get_li_titles())