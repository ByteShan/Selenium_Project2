from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

class AmazonProductSearch:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.amazon.in/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def select_category(self, category):
        category_dropdown = Select(self.driver.find_element(By.XPATH, "//select[@id='searchDropdownBox']"))
        category_dropdown.select_by_visible_text(category)
        time.sleep(2)

    def search_product(self, search_term):
        search_box = self.driver.find_element(By.ID, "twotabsearchtextbox")
        search_box.send_keys(search_term)
        time.sleep(2)
        search_icon = self.driver.find_element(By.ID, "nav-search-submit-button")
        search_icon.click()
        time.sleep(2)

    def capture_results(self, num_results=5):
        products = self.driver.find_elements(By.CSS_SELECTOR, "[data-component-type=s-search-result]")
        prod_info = []

        for product in products[:num_results]:
            name = product.find_element(By.CSS_SELECTOR, "h2 a").text
            price = product.find_element(By.CSS_SELECTOR, "span.a-price-whole").text
            prod_info.append({"Name": name, "Price": price})

        with open("search_results.txt", "w") as file:
            for item in prod_info:
                file.write(f"Name: {item['Name']} \n Price: {item['Price']} \n\n ")
        time.sleep(2)

    def close_browser(self):
        self.driver.quit()

if __name__ == "__main__":
    amazon_search = AmazonProductSearch()
    
    try:
        amazon_search.select_category("All Categories")
        amazon_search.search_product("iPhones")
        amazon_search.capture_results()
    finally:
        amazon_search.close_browser()