# Data Collection Pipeline Project

In this project, I implement an industrial-standard fata collection pipeline project that runs scalaby in the cloud.

In this project, I collect data from the book retailer, [Waterstones](https://www.waterstones.com/)  website. The aim of the project would be to collect relevant data about books in the the bestsellers category using the Selenium Chrome Webdriver written in Python. The README.md file presentts the actions taken and the decisions made during this project.

The techologies used in this project include:
* Python (
* SQL (Postgresql)
* Prometheus
* Docker
* Grafana

The steps taken in this code can be summarised as follows:
* Loading the necessary libraries.

* Loading the website and a that clicks on accept cookies button.

* Clicking on the header leading the the books in the best sellers category.
  This category is made up of 50 pages.
  
* Extracting data regarding the titles, names of authors, prices, format, and ratings of the books in this category.

* Scraping these data for the 50 pages, and saving them in a .csv file called book_scraping_pagination.csv.

The test_scraper folder contains script to test the webscraping process
