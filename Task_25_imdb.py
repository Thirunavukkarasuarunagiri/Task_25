from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearch:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.imdb.com/search/name")

    def fill_search_criteria(self, name, birth_year, profession):
        # Input name
        name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search_name")))
        name_input.clear()
        name_input.send_keys(name)

        # Input birth year
        birth_year_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search_birth_year")))
        birth_year_input.clear()
        birth_year_input.send_keys(birth_year)

        # Select profession
        profession_select = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "search_primary_profession")))
        profession_select.click()
        profession_option = profession_select.find_element(By.XPATH, f"//option[text()='{profession}']")
        profession_option.click()

    def perform_search(self):
        # Click on the search button
        search_button = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Search']")))
        search_button.click()

    def close(self):
        self.driver.quit()

if __name__ == "__main__":
    imdb_search = IMDbSearch()
    imdb_search.fill_search_criteria("Tom Cruise", "1962", "Actor")
    imdb_search.perform_search()
    imdb_search.close()