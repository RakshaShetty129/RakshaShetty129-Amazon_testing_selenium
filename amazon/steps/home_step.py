from behave import *
from po.home import HomePage

@step('user can see the title of page as "{title}"')
def step_impl(context, title):
    titleobj=HomePage(context.driver)
    titleobj.titleverifty(title)
@step('User clicks on the signin')
def step_impl(context):
    sihnobj=HomePage(context.driver)
    sihnobj.signin_click()
