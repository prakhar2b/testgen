#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Author : Prakhar Pratyush <prakharlabs@gmail.com>
#
#----------------------------------------------------------

import pytest
from selenium import webdriver

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def do_condition(condition, max_wait, driver):
	if condition == "url_changed":
		WebDriverWait(driver, max_wait).until(EC.url_changes(driver))


def step_1(driver):
	"""
	This test does 1
	"""

	elem = None

	try:
		elem = driver.find_element_by_name('q')
	except Exception as ex:
		print(ex)

	if not elem:
		try:
			elem = driver.find_element_by_css_selector("[key='Search']")
		except Exception as ex:
			print(ex)

		if not elem:
			raise Exception("No element found. Test Failed.")

	
	text = "dbmndbndbndjkbdkbdgbdgbdgbgdkbkgk"
	elem.send_keys(text)
	driver.implicitly_wait(0)

	
def step_2(driver):
	"""
	This test does 2
	"""

	elem = None

	try:
		elem = driver.find_element_by_css_selector("[key='Google Search']")
	except Exception as ex:
		print(ex)

	position = 2
	if not elem:
		try:
			elem =driver.find_elements_by_css_selector('center > input')
		except Exception as ex:
			print(ex)

		elem = elem[position] if len(elem) >= position else None
		

	if not elem:
		raise Exception("No element found. Test Failed.")
	elem_type = elem.get_attribute("type")


	if elem_type == "submit":
		elem.submit()
	else:
		elem.click()
	
	
	driver.implicitly_wait(0)
	
def step_3(driver):
	"""
	This test does 3
	"""

	# Explicit wait (Condition)
	do_condition('url_changed', 30, driver)
	driver.implicitly_wait(0)
	
def step_4(driver):
	"""
	This test does 4
	"""

	elem = None

	try:
		elem = driver.find_element_by_xpath('//div[@id="topstuff"]/div/div/p')
	except Exception as ex:
		print(ex)

	if not elem:
		raise Exception("No element found. Test Failed.")

	assert elem.text.__contains__("Your search - dbmndbndbndjkbdkbdgbdgbdgbgdkbkgk - did not match any documents")


	driver.implicitly_wait(5)



	
def step_5(driver):
	"""
	This test does 5
	"""

	try:
		elem = None

		elem = driver.find_element_by_id('ires')


		assert False, "Found element with id idres"

	except Exception:
		assert True

	driver.implicitly_wait(0)




def test_no_result_found(driver_):
	global driver
	driver = driver_

	driver.get("https://www.google.com")
	try:
		global_step_wait = 5
		driver.implicitly_wait(global_step_wait)
		
		step_1(driver)
	
		step_2(driver)
	
		step_3(driver)
	
		step_4(driver)
	
		step_5(driver)
		
	except Exception as ex:
		print(ex)

	driver.quit()

