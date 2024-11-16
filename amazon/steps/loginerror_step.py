from behave import *
from po.loginerror import LoginError

@step('user should see "{passworderrormsg}"')
def step_impl(context,passworderrormsg):
    passworderrormsgobj=LoginError(context.driver)
    passworderrormsgobj.passworderrormsg(passworderrormsg)
@step('User should see phonenumber eror "{phonenoerrormsg}"')
def step_impl(context,phonenoerrormsg):
    phonenoerrormsgobj=LoginError(context.driver)
    phonenoerrormsgobj.passworderrormsg(phonenoerrormsg)
