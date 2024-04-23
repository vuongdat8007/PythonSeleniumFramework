import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = None

def pytest_addoption(parser):
    parser.addoption(
        "--browser-name", action="store", default="chrome", help="my option: chrome or firefox or edge"
    )
    parser.addoption(
        "--disable-gpu", action="store_true", help="Disable browser's GPU rendering features"
    )
    parser.addoption(
        "--headless", action="store_true", help="Run tests in headless mode (No browser visualisation)"
    )

@pytest.fixture(scope="class")
def setup(request):
    global driver
    browser_name = request.config.getoption("--browser-name")
    headless = True if request.config.getoption("--headless") else False
    disable_gpu = True if request.config.getoption("--disable-gpu") else False
    if browser_name == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        if disable_gpu:
            chrome_options.add_argument("--disable-gpu")
        if headless:
            chrome_options.add_argument("headless")
        # https://googlechromelabs.github.io/chrome-for-testing/
        service_obj = Service("C:/Users/vuong/Downloads/chromedriver-win64/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj, options=chrome_options)

    elif browser_name == "firefox":
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument("--ignore-certificate-errors")
        # firefox_options.add_argument("--window-size=1920,1080") # firefox doesnt need this
        # to interact with button in headless mode
        firefox_options.add_argument("--start-maximized")
        if disable_gpu:
            firefox_options.add_argument("--disable-gpu")
        if headless:
            firefox_options.add_argument("--headless")
        # https://github.com/mozilla/geckodriver/releases
        service_obj=Service("C:/Users/vuong/Downloads/geckodriver-v0.34.0-win64/geckodriver.exe")
        driver = webdriver.Firefox(service=service_obj, options=firefox_options)

    elif browser_name == "edge":
        edge_options = webdriver.EdgeOptions()
        edge_options.add_argument("--ignore-certificate-errors")
        edge_options.add_argument("--window-size=1920,1080")
        edge_options.add_argument("--start-maximized")
        if disable_gpu:
            edge_options.add_argument("--disable-gpu")
        if headless:
            edge_options.add_argument("--headless")
        # https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/?form=MA13LH#downloads
        service_obj = Service("C:/Users/vuong/Downloads/edgedriver_win64/msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj, options=edge_options)
    else:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_argument("--window-size=1920,1080")
        chrome_options.add_argument("--start-maximized")
        if disable_gpu:
            chrome_options.add_argument("--disable-gpu")
        if headless:
            chrome_options.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_options)

    # wait for a maximum of 2 secs time
    driver.implicitly_wait(2)
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    #driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()

@pytest.mark.hookwrapper
def pytest_runtest_makereport(item):
    """
        Extends the PyTest Plugin to take and embed screenshot in html report, whenever test fails.
        :param item:
    """
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])

    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            #clean_nodeid = report.nodeid.replace("tests/", "")
            file_name = report.nodeid.replace("::", "_") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra

def _capture_screenshot(file_name):
    driver.get_screenshot_as_file(file_name)
