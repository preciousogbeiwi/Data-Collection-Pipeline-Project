
# Data Collection Pipeline Project
2
​
3
In this project, I implement an industrial-standard fata collection pipeline project that runs scalaby in the cloud.
4
​
5
In this project, I collect data from the book retailer, [Waterstones](https://www.waterstones.com/)  website. The aim of the project would be to collect relevant data about books in the the bestsellers category using the Selenium Chrome Webdriver written in Python. The README.md file presentts the actions taken and the decisions made during this project.
6
​
7
The techologies used in this project include:
8
* Python (pandas, boto3, math, os, selenium, setuptools, sqlalchemy time, unicodedata, urllib, uuid)
9
* Cloud: AWS (RDS, S3, EC2)
10
* SQL (Postgresql)
11
* Prometheus
12
* Docker
13
* Grafana
* Version Control (Git, Github)
14
​
15
The steps taken in this code are described as follows:

# Milestone 1: Settin up the environment and the technologies used.
Here, the technologies used in the project were set up.

# Milestone 2: Decide the website to collect data from.
The book retailer, [Waterstones](https://www.waterstones.com/) was chosen as the website to scrape data from. Relevant data about books in the the bestsellers category were intended for extraction. The online bookstore is one of the largest online retailers of books, toys, etc.

17
* Loading the necessary libraries.
18
​
19
* Loading the website and a that clicks on accept cookies button.
20
​
21
* Clicking on the header leading the the books in the best sellers category.
22
  This category is made up of 50 pages.
23
  
24
* Extracting data regarding the titles, names of authors, prices, format, and ratings of the books in this category.
25
​
26
* Scraping these data for the 50 pages, and saving them in a .csv file called book_scraping_pagination.csv.
27
​
28
The test_scraper folder contains script to test the webscraping process
The test_scraper folder contains script to test the webscraping process
