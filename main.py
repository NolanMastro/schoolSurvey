import random
import names
import random
import time
import string
from selenium import webdriver
from random_word import RandomWords
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service






def fill_out_survey(num_times):
    for _ in range(num_times):
        options = Options()
        service = webdriver.ChromeService(executable_path = r'/Users/nolan/Desktop/sc/chromedriver')
        driver = webdriver.Chrome(service=service)
        driver.get("https://byu.az1.qualtrics.com/jfe/form/SV_5tABnbXNhgZPeKi?Q_CHL=qr")
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/ul/li[1]/span/label'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/ul/li[1]/span/label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()


        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/div/input'))
            )
        except Exception as e:
            driver.quit()

        first_name = names.get_first_name()
        last_name = names.get_last_name()

        full_name = f"{first_name} {last_name}"

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/div/input').send_keys(full_name)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/div/input').send_keys(random.randint(16,18))

        random_username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        email = f"{random_username}@nolanmastro.com"
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[8]/div[3]/div/fieldset/div/div/input').send_keys(email)

        random_numbers = ''.join(random.choices('0123456789', k=4))
        student_email = f"55{random_numbers}@my.cuhsd.org"
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[10]/div[3]/div/fieldset/div/div/input').send_keys(student_email)

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[12]/div[3]/div/fieldset/div/div/input').send_keys('Branham High School')
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[14]/div[3]/div/fieldset/div/ul/li[1]/span/label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/ul/li[1]/span/label'))
            )
        except Exception as e:
            driver.quit()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/ul/li[1]/span/label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#QID7-4-label'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.CSS_SELECTOR, '#QID7-4-label').click()
        driver.find_element(By.CSS_SELECTOR, '#QID8-4-label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()


        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/div/input'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/div/input').send_keys(random.choice([
            "Computer Science", "Biology", "Psychology", "Engineering", "Business Administration",
            "English Literature", "Physics", "Chemistry", "Mathematics", "History",
            "Political Science", "Sociology", "Economics", "Art History", "Music",
            "Philosophy", "Environmental Science", "Nursing", "Communications", "Anthropology"
        ]))
        for i in range(2):
            driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/div/div[2]/table/tbody/tr/td[2]/div/div/div[1]').send_keys(Keys.ARROW_RIGHT)

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()

        try:
            element = WebDriverWait(driver, timeout=float('inf')).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[2]/th'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[2]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[3]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[4]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[5]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[6]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[7]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()

        try:
            element = WebDriverWait(driver, timeout=float('inf')).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/ul/li[4]/span/label'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/ul/li[4]/span/label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[6]/div[3]/div/fieldset/div/ul/li[5]/span/label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[8]/div[3]/div/fieldset/div/ul/li[5]/span/label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()

        try:
            element = WebDriverWait(driver, timeout=float('inf')).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#QR\~QID13\~1'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.CSS_SELECTOR, '#QR\~QID13\~1').send_keys(random.choice([
            "Financial Analyst", "Economist", "Market Research Analyst", "Data Analyst",
            "Investment Banker", "Economic Consultant", "Policy Analyst", "Budget Analyst",
            "Actuary", "Business Journalist", "Credit Analyst", "Statistician"
        ]))
        driver.find_element(By.CSS_SELECTOR, '#QR\~QID13\~2').send_keys(random.choice([
            "Financial Analyst", "Economist", "Market Research Analyst", "Data Analyst",
            "Investment Banker", "Economic Consultant", "Policy Analyst", "Budget Analyst",
            "Actuary", "Business Journalist", "Credit Analyst", "Statistician"
        ]))

        driver.find_element(By.CSS_SELECTOR, '#QR\~QID54\~1').send_keys(random.choice([
            "Analytical skills", "Statistical knowledge", "Data interpretation",
            "Mathematical proficiency", "Critical thinking", "Problem solving ability",
            "Research skills", "Financial modeling", "Econometrics", "Market analysis",
            "Quantitative reasoning", "Economic theory understanding"
        ]))
        driver.find_element(By.CSS_SELECTOR, '#QR\~QID54\~2').send_keys(random.choice([
            "Analytical skills", "Statistical knowledge", "Data interpretation",
            "Mathematical proficiency", "Critical thinking", "Problem solving ability",
            "Research skills", "Financial modeling", "Econometrics", "Market analysis",
            "Quantitative reasoning", "Economic theory understanding"
        ]))

        driver.find_element(By.CSS_SELECTOR, '#NextButton').click()

        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[5]/label[1]'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[2]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[3]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[4]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[5]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/table/tbody/tr[2]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/table/tbody/tr[3]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/table/tbody/tr[4]/td[5]/label[1]').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()


        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#QID33-4-label'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.CSS_SELECTOR, '#QID33-4-label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()


        

        try:
            element = WebDriverWait(driver, timeout=float('inf')).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/div/table/tbody/tr[2]/td[2]/input'))
            )
        except Exception as e:
            driver.quit()


        for i in range(2):
            driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/div/div[2]/table/tbody/tr/td[2]/div/div/div[1]').send_keys(Keys.ARROW_RIGHT)

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/div/table/tbody/tr[1]/td[2]/input').send_keys(random.randint(20,50))
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/div/table/tbody/tr[2]/td[2]/input').send_keys(random.randint(20,50))
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/div/table/tbody/tr[3]/td[2]/input').send_keys(random.randint(20,50))
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/div/table/tbody/tr[4]/td[2]/input').send_keys(random.randint(20,50))

        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()
        try:
            element = WebDriverWait(driver, timeout=float('inf')).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#QID38-1-label'))
            )
        except Exception as e:
            driver.quit()
        driver.find_element(By.CSS_SELECTOR, '#QID38-1-label').click()
        driver.find_element(By.CSS_SELECTOR, '#QID39-2-label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()


        try:
            element = WebDriverWait(driver, timeout=float('inf')).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, '#QID40-3-label'))
            )
        except Exception as e:
            driver.quit()


        driver.find_element(By.CSS_SELECTOR, '#QID40-3-label').click()
        driver.find_element(By.CSS_SELECTOR, '#QID58-3-label').click()
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()

        try:
            element = WebDriverWait(driver, timeout=float('inf')).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/ul/li[2]/span/label'))
            )
        except Exception as e:
            driver.quit()
        time.sleep(4)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/ul/li[2]/span/label').click()
        time.sleep(2)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()

        try:
            element = WebDriverWait(driver, timeout=float('inf')).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[4]/div[3]/div/fieldset/div/div/table/tbody/tr[1]/td[2]/input'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.CSS_SELECTOR, '#QR\~QID37\~1').send_keys(random.choice(['Organize events', 'Delegate tasks', 'Motivate members', 'Set goals', 'Coordinate activities']))
        time.sleep(0.3)
        driver.find_element(By.CSS_SELECTOR, '#QR\~QID37\~2').send_keys(random.choice(['Organize events', 'Delegate tasks', 'Motivate members', 'Set goals', 'Coordinate activities']))
        time.sleep(0.3)
        driver.find_element(By.CSS_SELECTOR, '#QR\~QID50').send_keys('5 hours')
        time.sleep(0.3)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()



        try:
            element = WebDriverWait(driver, timeout=float('inf')).until(
                EC.presence_of_element_located((By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[3]/label[1]'))
            )
        except Exception as e:
            driver.quit()

        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[1]/td[3]/label[1]').click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[2]/td[3]/label[1]').click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[1]/div[2]/div[3]/div/fieldset/div/table/tbody/tr[3]/td[3]/label[1]').click()
        time.sleep(0.3)
        driver.find_element(By.CSS_SELECTOR, '#QR\~QID66\#1\~1\~1\~TEXT').send_keys(random.randint(20,50))
        time.sleep(0.3)
        driver.find_element(By.CSS_SELECTOR, '#QR\~QID66\#1\~2\~1\~TEXT').send_keys(random.randint(20,50))
        time.sleep(0.3)
        driver.find_element(By.CSS_SELECTOR, '#QR\~QID66\#1\~3\~1\~TEXT').send_keys(random.randint(20,50))
        time.sleep(0.3)
        driver.find_element(By.XPATH, '/html/body/div[3]/div/form/div/div[2]/div[2]/div[3]/div[2]/input').click()

        time.sleep(5)

        driver.quit()


fill_out_survey(100)
