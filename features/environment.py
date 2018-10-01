import os
import allure
from sys import platform
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

CHROMEDRIVER_PATH = ""
CHROMEDRIVER_PATH_lINUX = "/usr/local/bin/chromedriver"
CHROMEDRIVER_PATH_WIN = r'C:/Python37/Scripts/chromedriver'
CHROMEDRIVER_PATH_MAC = "/usr/local/bin/chromedriver"
WINDOW_SIZE = "1920,1080"
SCREENSHOTS_PATH = ""
SCREENSHOTS_PATH_LINUX = "/home/circleci/project/"
SCREENSHOTS_PATH_WIN = "/screenshots"
SCREENSHOTS_PATH_MAC = "/Users/silfredomora/Desktop/workspace/puc_testing/screenshots"



def before_all(context):
    print('Before all started')
    # Here we define if we want to run headless or not
    context.headless = context.config.userdata.get("headless", "no")
    # Here we define context, so we can change browser or domain.
    context.timeout = 30
    # Here we define if we take a screen_capture after an error or assertion failure default no
    context.screen_capture_required = context.config.userdata.get("screen_capture", "no")



def before_scenario(context, scenario):
    print('New scenario started: ')
    print(scenario)
    print("setting the path according " + platform)

    if platform == "win32":
        CHROMEDRIVER_PATH = context.config.userdata.get("path", CHROMEDRIVER_PATH_WIN)
    if platform == "darwin":
        CHROMEDRIVER_PATH = context.config.userdata.get("path", CHROMEDRIVER_PATH_MAC)
    else:
        CHROMEDRIVER_PATH = context.config.userdata.get("path", CHROMEDRIVER_PATH_lINUX)
    chrome_options = Options()
    if context.headless == "yes":
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
        chrome_options.add_argument("--disable-gpu ")
    print("path to chromedriver: " + CHROMEDRIVER_PATH)
    # just use this if we need a profile on the browser
    #chrome_options.add_argument("user-data-dir=path /to/profile")  # Path to your chrome profile
    context.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=CHROMEDRIVER_PATH)
    context.driver.maximize_window()



def after_scenario(context, scenario):
    print('scenario has been finished')
    if 'ui' in scenario.tags:
        print("closing the browser")
        if scenario.status == "failed" and context.screen_capture_required == "yes":
            print('screen capture required by sys parameters')
            now = datetime.now().strftime('%d-%m-%y_%H-%M-%S')
            filename = scenario.filename + now + ".png"
            if platform == "win32":
                SCREENSHOTS_PATH = SCREENSHOTS_PATH_WIN
            if platform == "darwin":
                SCREENSHOTS_PATH = SCREENSHOTS_PATH_MAC
            else:
                SCREENSHOTS_PATH = SCREENSHOTS_PATH_LINUX
            screenshot_path = os.path.join(SCREENSHOTS_PATH, filename)
            print('screen capture taken: ' + filename)
            print("into: "+screenshot_path)
            print("file: "+filename)
            context.driver.save_screenshot(screenshot_path)
            allure.attach(context.driver.get_screenshot_as_png(), name='screenshot', attachment_type=allure.attachment_type.PNG)
        print("===============================================================================================================")
        context.driver.quit()


