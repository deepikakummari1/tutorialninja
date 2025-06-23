import os
from datetime import datetime

import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver


@pytest.fixture()
def setup(browser):
    if browser == 'edge':
        opt = webdriver.EdgeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Edge(options=opt)
        print("Launching Edge browser.........")

    elif browser == 'firefox':
        opt = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=opt)
        print("Launching Firefox browser.........")
    else:
        opt = webdriver.ChromeOptions()
        opt.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=opt)
        print("Launching Chrome browser.........")

    yield driver
    driver.quit()


def pytest_addoption(parser):
    parser.addoption("--browser")


# Fixture to fetch browser option
@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

# Hook 1: Configure report path and add custom metadata
@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    config.option.htmlpath = (
        os.path.abspath(os.getcwd()) + "\\reports\\" + datetime.now().strftime("%d-%m-%Y %H-%M-%S") + ".html"
    )

    config.stash[metadata_key]['Project Name'] = 'TutorialNinja'
    config.stash[metadata_key]['Module Name'] = 'CustRegistration'
    config.stash[metadata_key]['Tester Name'] = 'Deepika'

# Hook 2: Remove default metadata
@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("Python", None)
    metadata.pop("Plugins", None)


# Hook 3: Capture screenshot on test failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == "call" and rep.failed:
        driver = item.funcargs.get("setup")
        if driver:
            screenshot_dir = os.path.abspath(os.getcwd()) + "/screenshots/"
            os.makedirs(screenshot_dir, exist_ok=True)
            driver.save_screenshot(f"{screenshot_dir}{item.name}.png")



