from selenium import webdriver
from behave import *

@step("User initialize the browser")
def step_impl(context):
    context.driver=webdriver.Chrome()
    
@when("User launch the application")
def step_impl(context):
    context.driver.get('https://www.amazon.in/')
    