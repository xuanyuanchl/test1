# -*- coding: utf-8 -*-
'''
Created on May 10, 2020

@author: O5LT
'''
from selenium.webdriver.common.by import By

from Control.Link import link
from PageBase.pageBase import pageBase


class homePage(pageBase):
    def __init__(self, pageUrl):
        super().__init__(pageUrl)

    @property
    def AccountsManagement(self):
        return link(self.webDriver, {By.ID: 'Menu_AccountsManagement'})

    @property
    def UserProfile(self):
        return link(self.webDriver, {By.ID: 'Logged_Menu_User'})

    @property
    def OperatorTools(self):
        return link(self.webDriver, {By.ID: 'Menu_OperatorTools'})
