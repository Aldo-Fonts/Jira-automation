#####################################################################################################################################################################################
# File:         test.py
# Version:      1.0
# Author:       Aldo_Fonts
# Description:  The current file has the tests to start a selenium web driver for different browsers
#####################################################################################################################################################################################
# Library/ies
import drivers
# Test
browsers = ['chrome', 'firefox', 'edge', 'safari']

for browser in browsers:
    driver = drivers.webDriver(browser)
    driver.get("http://www.google.com")
    driver.quit()
