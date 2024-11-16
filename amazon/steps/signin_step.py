from behave import *
from po.signin import signin

@step('User fills phone number "{phone_no}"')
def step_impl(context, phone_no):
    phonenoobj=signin(context.driver)
    phonenoobj.number(phone_no)
@step('user click continue')
def step_impl(context):
    conobj=signin(context.driver)
    conobj.continueclick()
@step('User enter password "{password}"')
def step_impl(context,password):
    passobj=signin(context.driver)
    passobj.enterpassword(password)
    
@step('User should see forgot password "{passtext}"')
def step_impl(context,passtext):
    passobj=signin(context.driver)
    passobj.forgotpassword(passtext)
    
@step('user click signin')
def step_impl(context):
    sinobj=signin(context.driver)
    sinobj.sinclick()
@step('user can see their name "{name}" at right top')
def step_impl(context,name):
    nameobj=signin(context.driver)
    nameobj.verifyname(name)
    
@step('user click forgot password')
def step_impl(context):
    forgotpassobj=signin(context.driver)
    forgotpassobj.forgotpass()
    
