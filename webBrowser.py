# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 02:47:08 2020

@author: jsoumen
"""
from selenium import webdriver

server_name = input("Enter server name e.g QC1: ")


browser = webdriver.Chrome("chromedriver.exe")
browser.get("https://help.kodiakhandset.com/lcms/docs/HSserver/WSCR_links.htm")


elem = browser.find_element_by_link_text(server_name.upper())
elem.click()