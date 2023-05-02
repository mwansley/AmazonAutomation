from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.webelement import WebElement
import time
import args

un = args.username
pswd = args.password


# open web page
driver = webdriver.Chrome(
    executable_path="c:\\WebDriver\\Chrome\\chromedriver.exe")


driver.delete_all_cookies()


WebDriverWait(driver, 3.0)
driver.get("https://amazon.com")
WebDriverWait(driver, 3.0)


# find search box, enter "socks"
driver.delete_all_cookies()
srchBox = driver.find_element(
    By.XPATH, '//*[@id="twotabsearchtextbox"]')
WebDriverWait(driver, 2.0)
if (srchBox.is_displayed):
    srchBox.send_keys('socks')
    srch = driver.find_element(By.ID, "nav-search-submit-button").click()
else:
    print("Searchbox Not Found!")

socks = driver.find_element(
    By.XPATH, '//*[@id="B07WRYDFVD-best-seller"]')
if (socks.is_displayed):
    product = driver.find_element(
        By.XPATH,
        '//*[@id="search"]/div[1]/div[1]/div/span[1]/div[1]/div[4]/div/div/div/div/div/div/div[2]/div/span/a/div/img')
    WebDriverWait(driver, 2.0)
    if (product.is_displayed):
        print("Socks Found...")
        print()
        product.click()
        WebDriverWait(driver, 2.0)

sockPage = driver.find_element(
    By.XPATH, '//*[@id="submit.add-to-cart-announce"]')
if (sockPage.is_displayed):
    adToCartBtn = driver.find_element(
        By.XPATH, '//*[@id="add-to-cart-button"]')
    if (adToCartBtn.is_displayed):
        WebDriverWait(driver, 2.0)
        adToCartBtn.click()
        WebDriverWait(driver, 2.0)

soxAdded = driver.find_element(
    By.XPATH, '//*[@id="NATC_SMART_WAGON_CONF_MSG_SUCCESS"]/span')
if (soxAdded.is_displayed):
    print('Socks added to cart...')
    print()

toCheckOut = driver.find_element(
    By.XPATH, '//*[@id="sc-buy-box-ptc-button"]/span/input')
WebDriverWait(driver, 2.0)
if (toCheckOut.is_displayed):
    toCheckOut.click()
    print('Signing in...')
    print()
    WebDriverWait(driver, 2.0)


signInPg = driver.find_element(
    By.XPATH, '//*[@id="ap_email"]')
WebDriverWait(driver, 2.0)
if (signInPg.is_displayed):
    signInPg.send_keys(un)

signInBtn = driver.find_element(
    By.XPATH,
    '/html/body/div[1]/div[1]/div[2]/div/div[2]/div/div[1]/form/div/div/div/div[2]/span/span/input')
WebDriverWait(driver, 2.0)
if (signInBtn.is_displayed):
    print('Entering user name...')
    print()
    signInBtn.click()
WebDriverWait(driver, 2.0)
# until(driver.find_element_by_xpath())
# driver.find_element(By.XPATH, '//*[@id="ap_password"]')
WebDriverWait(driver, 2.0)
pswdBx = driver.find_element(By.XPATH, '//*[@id="ap_password"]')
if pswdBx.is_displayed:
    print('Password box found...')
    print()
    print('Entering user password...')
    pswdBx.send_keys(pswd)


ordBtn = driver.find_element(
    By.XPATH, '//*[@id="signInSubmit"]')
WebDriverWait(driver, 2.0)
if (ordBtn.is_displayed):
    print()
    print('Order button found...')
    ordBtn.click()
WebDriverWait(driver, 3.0)

noThanks = driver.find_element(
    By.XPATH,
    '/html/body/div[5]/div[1]/div/div/div/div/ms3-selection/table/tbody/tr/td/div/div[1]/div/form/div/div/div/div[1]/a')
WebDriverWait(driver, 2.0)
if (noThanks.is_displayed):
    noThanks.click()
WebDriverWait(driver, 3.0)


plcOrderBtn = driver.find_element(
    By.XPATH,
    '/html/body/div[5]/div[1]/div/div[2]/div/div/div[2]/div/div[1]/div/div[1]/div[1]/div/span/span/input')
WebDriverWait(driver, 3.0)
if (plcOrderBtn.is_displayed):
    print()
    print('Place order button found...')
# here would go the code to complete the order but I've already ordered
# two pair of socks today...

    driver.close()
