"""
Functional test case for todos application
"""
from selenium import webdriver

browser = webdriver.Firefox(executable_path="/usr/local/bin/geckodriver")
browser.get('http://localhost:8000')

assert 'Todo' in browser.title
browser.close()