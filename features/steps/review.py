from behave import when, given, then

@given('Open product page')
def open_product_page(context):
    context.app.main_page.open_url('product/asus-chromebook-flip-c434-2-in-1/')

@when('Click on Review Tab')
def click_review_tab(context):
    context.app.product_page.review_tab_click()

@when('Choose rating')
def assign_4_star_rating(context):
    context.app.product_page.choose_4_star()

@when('Review text is typed in')
def input_review(context):
    context.app.product_page.input_review_text()

@when('Fields Name and Email are filled out')
def input_name_and_mail(context):
    context.app.product_page.input_name_and_email()

@when('Submit button is clicked')
def submit_click(context):
    context.app.product_page.submit_click()

@then('Review is saved and added to reviews list')
def verify_review_is_added(context):
    context.app.product_page.verify_review_waiting_approval_status()
