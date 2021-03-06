# -*- coding: utf-8 -*-

'''
Created on May 9, 2020

@author: O5LT
'''
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from Support.WebDriverExtensions import webDriverExtensions
from Support.Helper import helper


class controlBase:
    """web control base class"""
    __driver: webdriver
    __selector = None
    __actions = None
    __wrappedElement = None

    def __init__(self, driver, selector: dict = None, element=None):
        """
        :param driver: webdriver
        :param selector: selector contains locator and value like:
        {by.id: id1}
        {by.xpath: xpath1}"""
        self.__driver = driver
        self.__selector = selector
        self.__wrappedElement = element

    @property
    def Selector(self) -> dict:
        return self.__selector

    @property
    def isVisible(self) -> bool:
        return self.wrappedElement is not None and self.wrappedElement.is_displayed()

    @property
    def isPresent(self) -> bool:
        return self.wrappedElement is not None

    @property
    def isEnabled(self) -> bool:
        return self.wrappedElement.is_enabled()

    def getText(self) -> str:
        """
        get the text value of web element
        :return: text value
        """
        return self.wrappedElement.text

    def getAttribute(self, attributeName) -> str:
        """Gets the given attribute or property of the element.

        This method will first try to return the value of a property with the
        given name. If a property with that name doesn't exist, it returns the
        value of the attribute with the same name. If there's no attribute with
        that name, ``None`` is returned.

        Values which are considered truthy, that is equals "true" or "false",
        are returned as booleans.  All other non-``None`` values are returned
        as strings.  For attributes or properties which do not exist, ``None``
        is returned.

        :Args:
            - attributeName - Name of the attribute/property to retrieve.

        Example::

            # Check if the "active" CSS class is applied to an element.
            is_active = "active" in target_element.get_attribute("class")

        """
        return self.wrappedElement.get_attribute(attributeName)

    @property
    def wrappedElement(self):
        """
        get the web element
        :return: web element or None
        """
        # style_yellow = 'arguments[0].style.border="5px solid yellow"'
        if self.__wrappedElement is not None:
            # self.__driver.execute_script(style_yellow, self.__wrappedElement)
            return self.__wrappedElement
        if self.__selector is None:
            # print('do we need to specify the selector?')
            return None

        self.__wrappedElement = webDriverExtensions.FindElement(self.webDriver, self.Selector, 5)
        # self.__driver.execute_script(style_yellow, self.__wrappedElement)
        return self.__wrappedElement

    @property
    def webDriver(self):
        """
        get web driver
        :rtype: web driver
        """
        return self.__driver

    @property
    def actions(self):
        if self.__actions is None:
            self.__actions = ActionChains(self.webDriver)
        return self.__actions

    @property
    def _helper(self):
        return helper(self.webDriver)

    def HoverOn(self):
        self._helper.Browser.ScriptExecutor.execute_script('$(arguments[0]).mouseover();', self.wrappedElement)

    def MoveMouse(self):
        """
            Moving the mouse to the middle of an element.

        """
        self._helper.Browser.Actions.move_to_element(self.wrappedElement).perform()

    def ScrollToView(self):
        self._helper.Browser.ScriptExecutor.execute_script('arguments[0].scrollIntoView(true);', self.wrappedElement)

    def DragAndDrop(self, targetElement):
        """
            Holds down the left mouse button on the source element (self.wrappedElement),
               then moves to the target element and releases the mouse button.

            :Args:
             - targetElement: The element to mouse up.
        """
        self._helper.Browser.Actions.drag_and_drop(self.wrappedElement, targetElement).perform()
