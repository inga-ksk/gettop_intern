#import allure
#from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
from selenium import webdriver
# from selenium.webdriver.support.events import EventFiringWebDriver
# from support.logger import logger, MyListener

# Register for BrowserStack, then grab it from https://www.browserstack.com/accounts/settings
#bs_user = ''
#bs_key = ''

# Allure command:
# behave -f allure_behave.formatter:AllureFormatter -o test_results/ features/tests/product_page.feature

def browser_init(context):
    """
    :param context: Behave context
    """
    #context.driver = webdriver.Chrome(executable_path="/Users/Inga/Documents/Careerist/Automation/gettop_intern/chromedriver.exe")
    # context.driver = webdriver.Safari()
    #context.driver = webdriver.Firefox(executable_path="/Users/Inga/Documents/Careerist/Automation/gettop_intern/geckodriver.exe")

    ## HEADLESS MODE ####
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('window-size=1920x1080');
    context.driver = webdriver.Chrome(chrome_options=options)

    # Mobile - run tests on mobile web browser
    # options = webdriver.ChromeOptions()
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # options.add_experimental_option("mobileEmulation", mobile_emulation)
    # context.driver = webdriver.Chrome(chrome_options=options)

    ### EventFiringWebDriver - log file ###
    ### for drivers ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(), MyListener())
    # for headless mode ###
    # context.driver = EventFiringWebDriver(webdriver.Chrome(chrome_options = options), MyListener())

    # for browerstack ###
    # desired_cap = {
    #     'browser': 'Firefox',
    #     'os_version': '11',
    #     'os': 'Windows',
    #     'name': test_name
    # }
    # url = f'http://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
    # context.driver = webdriver.Remote(url, desired_capabilities=desired_cap)

    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 10)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()