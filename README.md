# Website Content Scraper using BeautifulSoup
This repository contains a Python script for web scraping using BeautifulSoup that can scrape all the HTML content of the website and store them into the JSON format. This also creates JSON output for each of the individual tags. This can be used to train machine learning models to automate creating HTML page layout elements.

The script will prompt you for the URL of the website you want to scrape. Enter the URL and press enter. The script will then use BeautifulSoup to scrape the HTML content from the website and save it in JSON format. The JSON file will be saved in the same directory as the script. Note that it stores the JSON format of the whole website as well as tag-wise JSON are also exported.

One of the use-case of this script is that the scraped data can be used to create machine learning algorithm that can generate landing pages from gathered source code data from various sites!

### Requirements
- Python 3.x installed
- BeautifulSoup

### Contributing

If you have any suggestions or find any bugs, feel free to open an issue or submit a pull request.
