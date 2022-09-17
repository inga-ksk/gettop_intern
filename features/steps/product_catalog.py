from behave import when, given, then

@given('First product catalog page is open')
def verify_catalog_page_1_open(context):
    context.app.catalog_page.catalog_page_1_open()

@given('Open product catalog page 2')
def open_catalog_page_2(context):
    context.app.main_page.open_url('shop/page/2/')

@when('Click on page 2 of product catalog')
def catalog_page_2_click(context):
    context.app.catalog_page.catalog_page_2_click()

@when('Click on > in page list')
def click_on_right_arrow_sign(context):
    context.app.catalog_page.catalog_switch_right_arrow_click()

@when('Click on < in page list')
def click_on_left_arrow_sign(context):
    context.app.catalog_page.catalog_switch_left_arrow_click()

@then('Second catalog page is open')
def verify_catalog_page_2_open(context):
    context.app.catalog_page.catalog_page_2_open()

@then('First product catalog page is open')
def verify_catalog_page_1_open(context):
    context.app.catalog_page.catalog_page_1_open()