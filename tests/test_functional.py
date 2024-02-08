from selenium import webdriver
from time import sleep
import pytest
import subprocess
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By

@pytest.fixture
def driver():
    process = subprocess.Popen(["streamlit","run","src/app.py"])
    options = Options()
    options.headless = True
    driver = webdriver.Edge(options=options)
    driver.set_page_load_timeout(5)
    yield driver

    driver.quit()
    process.kill()

def test_app_open(driver):
    driver.get("http://localhost:8501")
    sleep(5)

def test_check_title_is(driver):
    driver.get("http://localhost:8501")
    sleep(2)
    page_title = driver.title

    expect_title = "Excel Schema Validator"
    assert page_title == expect_title

def test_check_streamlit_h1(driver):
    driver.get("http://localhost:8501")
    sleep(2)
    h1_element = driver.find_element(By.TAG_NAME, "h1")

    expected_test = "Attach the excel file"
    assert h1_element.txt == expected_test