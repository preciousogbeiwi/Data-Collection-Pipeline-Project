# Import the Necessary Libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import uuid
from selenium.common.exceptions import NoSuchElementException
from unittest.main import main

s = Service('C:/Users/preco/Anaconda3/Library/bin/chromedriver.exe')

class Scraper_project:
    def __init__(self, url: str = 'https://www.waterstones.com' ): 
        self.driver = webdriver.Chrome(service=s) 
        self.driver.get(url)
    
    def accept_cookies(self, xpath: str='//button[@id="onetrust-accept-btn-handler"]'):
        time.sleep(1)
        self.cookies_button = self.driver.find_element(By.XPATH, xpath)
        return self.cookies_button

    def accept_cookies_click(self):
        return self.accept_cookies().click()

    def bestsellers(self, xpath: str='//*[@id="pagesmain"]/div[3]/header[1]/a'):
        self.bestsellers_button = self.driver.find_element(By.XPATH, xpath)
        return self.bestsellers_button
   
    def bestsellers_click(self):
        return self.bestsellers().click()    

    def find_container(self, xpath: str = '//div[@class="search-results-list"]'): 
        return self.driver.find_element(By.XPATH, xpath)

    def extract_data(self):
        self.book_dict = {
            'ID':[],
            'Link': [],
            'src': [],
            'Title': [],
            'Author': [],
            'Old Price': [],
            'New Price': [],
            'Listing Type': [],
            'No_Reviews':[],
            'Ratings': [] 
            }
        
        self.container = self.find_container()
        book_list= self.container.find_elements(By.XPATH, './div')
        self.link_list = []
        for book in book_list:
            self.link_list.append(book.find_element(By.TAG_NAME, 'a').get_attribute('href')) 
            
        for link in self.link_list[0:]:
            id = str(uuid.uuid4())
            self.book_dict['ID'].append(id) 
            self.driver.get(link) 
            time.sleep(1)
            self.book_dict['Link'].append(link)
            try:
                src_path = self.driver.find_elements(By.XPATH, '//div[@class="book-image-main"]')
                for path in src_path:
                    src = path.find_element(By.TAG_NAME, 'img').get_attribute('src')
                    self.book_dict['src'].append(src)
            except NoSuchElementException:
                self.book_dict['src'].append('N/A')
            try:
                title = self.driver.find_element(By.XPATH, '//div[@class="title-wrap"]/a')
                self.book_dict['Title'].append(title.text)
            except NoSuchElementException:
                self.book_dict['Title'].append('N/A')
            try:
                author = self.driver.find_element(By.XPATH, '//span[@itemprop="author"]')
                self.book_dict['Author'].append(author.text)
            except NoSuchElementException:
                self.book_dict['Author'].append('N/A')
            try:
                old_Price = self.driver.find_element(By.XPATH, '//span[@class="price-rrp"]')
                self.book_dict['Old Price'].append(old_Price.text)
            except NoSuchElementException:
                self.book_dict['Old Price'].append('N/A')
            try:
                new_Price = self.driver.find_element(By.XPATH, '//span[@class="price"]')
                self.book_dict['New Price'].append(new_Price.text)
            except NoSuchElementException:
                self.book_dict['New Price'].append('N/A')
            try:
                listing_Type = self.driver.find_element(By.XPATH, '//span[@itemprop="bookFormat"]')
                self.book_dict['Listing Type'].append(listing_Type.text)
            except NoSuchElementException:
                self.book_dict['Listing Type'].append('N/A')
            try:
                reviews = self.driver.find_element(By.XPATH, '//div[@class="star-rating"]')
                rev = reviews.find_element(By.XPATH, '//a[@class="reviews-trigger"]')
                self.book_dict['No_Reviews'].append(rev.text)
            except NoSuchElementException:
                self.book_dict['No_Reviews'].append('N/A')
            try:
                ratings = self.driver.find_elements(By.XPATH, '//div[@class="star-rating"]')
                for rating in ratings:
                   try:
                        full_star = rating.find_elements(By.XPATH, '//span[@class="star-icon full"]')
                        len_full_star = len(full_star)
                   except NoSuchElementException:
                        len_full_star = 0
                   try:
                        half_star = rating.find_elements(By.XPATH, '//span[@class="star-icon half"]')
                        len_half_star = len(half_star)
                   except NoSuchElementException:
                        len_half_star = 0
                   try:
                        no_star = rating.find_elements(By.XPATH, '//span[@class="star-icon"]')
                        len_no_star = len(no_star)
                   except NoSuchElementException:
                        len_no_star = 0
                    
                self.book_dict['Ratings'].append(len_full_star+(len_half_star/2)-len_no_star)
                    
            except NoSuchElementException:
                self.book_dict['Ratings'].append('N/A')
        return self.book_dict