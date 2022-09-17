from behave import when, given, then

@given('Open product catalog page')
def open_catalog(context):
    context.app.main_page.open_url('shop/')

@when('Hover over product image')
def hover_product_image(context):
    context.app.catalog_page.hover_product_image()

@when('Click on Quick view link')
def quick_view_click(context):
    context.app.catalog_page.quick_view_click()

@then('Click on Add to cart button')
def add_to_cart_click(context):
    context.app.catalog_page.add_to_cart_click()

@then('Quick view overlay window is open')
def quick_view_window_open(context):
    context.app.catalog_page.quick_view_window_presence()

@then('Click on closing X')
def quick_view_close_click(context):
    context.app.catalog_page.quick_view_close()

@then('Catalog page is back')
def catalog_page_open(context):
    context.app.catalog_page.catalog_page_1_open()

@then('Header cart features one item')
def header_cart_item_count(context):
    context.app.header.cart_icon_count()
