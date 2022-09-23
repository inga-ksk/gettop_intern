from behave import when, given, then

@given('Open url https://gettop.us/shop/?orderby=rating')
def open_filtered_by_rating_results(context):
    context.app.main_page.open_url('shop/?orderby=rating')

@when('Click on sorting dropdown list')
def click_sorting_dropdown(context):
    context.app.catalog_page.filter_dropdown_click()

@when('Select Sort by average rating')
def select_average_rating_filter(context):
    context.app.catalog_page.average_rating_filter_click()

@then('1st product has rating starts displayed after sorting')
def verify_1st_prod_has_rating(context):
    context.app.catalog_page.verify_1st_prod_rating_is_present()