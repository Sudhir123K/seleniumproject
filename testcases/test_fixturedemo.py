
def test_browselogin(browser):
 browser.implicitly_wait(5)
 browser.maximize_window()
 browser.get("http://google.com")
 assert 5 == 5
