from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BinusmayaTester:
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self):
        url = "https://lms.binus.ac.id/get-your-username"
        self.driver.get(url)

    def enter_student_id(self, student_id):
        input_xpath = "//input[@placeholder='Enter your Student ID']"
        input_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, input_xpath)))
        input_box.clear()
        input_box.send_keys(student_id)

    def click_element(self, xpath):
        elem = self.wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        elem.click()

    def pick_date(self, dob):
        self.click_element("//button[contains(@aria-label, 'choose date')]")
        self.click_element("//button[contains(@class, 'MuiPickersCalendarHeader-switchViewButton')]")
        self.click_element(f"//button[text()='{dob['year']}']")
        self.click_element(f"//button[text()='{dob['month']}']")
        self.click_element(f"//button[normalize-space()='{dob['day']}']")

    def submit_form(self):
        submit_xpath = "//button[span[text()='Submit']]"
        self.click_element(submit_xpath)

    def wait_for_response(self):
        expected_texts = ["We found a match", "Invalid", "Incorrect"]
        self.wait.until(
            lambda d: any(text in d.page_source for text in expected_texts)
        )

    def verify_result(self, expected_success):
        page = self.driver.page_source
        actual = "We found a match" in page
        return actual == expected_success

    def execute_test(self, test_case):
        print(f"\nExecuting test case: {test_case['desc']}")
        self.open_target_page()
        self.input_student_id(test_case['student_id'])
        self.pick_date(test_case['dob'])
        self.submit_form()
        self.wait_for_response()

        if self.verify_result(test_case['expect_success']):
            print("Test passed")
        else:
            print("Test failed")

    def close_browser(self):
        self.driver.quit()