# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''

from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException


class webDriverExtensions():

    @staticmethod
    def FindElement(driver, selector, timeoutInSeconds):
        locator, objectstring = sorted(selector.items())[0]
        if timeoutInSeconds > 0:
            waiter = WebDriverWait(driver, timeoutInSeconds)
            try:
                return waiter.until(lambda d: d.find_element(locator, objectstring))
            except NoSuchElementException as e:
                print('No such web element')
            except TimeoutException as e:
                print('Cannot find web element')
        return driver.find_element(locator, objectstring)

    @staticmethod
    def FindElements(driver, selector, timeoutInSeconds):
        locator, objectstring = sorted(selector.items())[0]
        if timeoutInSeconds > 0:
            waiter = WebDriverWait(driver, timeoutInSeconds)
            waiter.until(lambda d: d.find_elements(locator, objectstring) if (
                    len(d.find_elements(locator, objectstring)) > 0) else None)
        return driver.find_elements(locator, objectstring)
