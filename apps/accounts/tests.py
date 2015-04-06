from django.test import TestCase, LiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver

from apps.accounts.forms import RegistrationForm
from apps.accounts.views import *
from apps.exams import views

# Create your tests here.

class RegistrationTestCase(TestCase):
	
	def setUp(self):
	# 	# User.objects.create_user(
	# 	# 	username='test1',
	# 	# 	email='test1@test.com',
	# 	# 	password='test1',
	# 	# 	# password_confirm='test1'
	# 	# 	)
		
		self.selenium = webdriver.Firefox()
		self.selenium.maximize_window()
		super(RegistrationTestCase, self).setUp()
		# pass

	# def tearDown(self):
	# 	self.selenium.quit()
	# 	super(RegistrationTestCase, self).tearDown()

	
	def test_login_fail(self):
		"""
		Test case where user inputs wrong password

		"""
		print "testing login failure..."
		login_page = self.selenium.get('http://127.0.0.1:8000/accounts/login/')
		username = self.selenium.find_element_by_id('id_username')
		username.send_keys('testuser')
		password = self.selenium.find_element_by_id('id_password')

		password.send_keys('tes')
		self.selenium.find_element_by_xpath('//input[@value = "Login"]').click()
		current_page = self.selenium.current_url
		self.assertEquals(current_page, 'http://127.0.0.1:8000/accounts/login/')

	
	def test_login_pass(self):
		"""
		Test case where user inputs accurate password
	
		"""
		login_page = self.selenium.get('http://127.0.0.1:8000/accounts/login/')
		username = self.selenium.find_element_by_id('id_username')
		username.send_keys('testuser')
		password = self.selenium.find_element_by_id('id_password')

		password.send_keys('test')
		self.selenium.find_element_by_xpath('//input[@value = "Login"]').click()
		current_page = self.selenium.current_url
		self.assertEquals(current_page, 'http://127.0.0.1:8000/accounts/home/')

	def test_exam_page(self):
		"""
		Test case for checking exam link on user home page
		
		"""
		login_page = self.selenium.get('http://127.0.0.1:8000/accounts/login/')

		username = self.selenium.find_element_by_id('id_username')
		username.send_keys('testuser')
		password = self.selenium.find_element_by_id('id_password')
		password.send_keys('test')
		self.selenium.find_element_by_xpath('//input[@value = "Login"]').click()
		current_page = self.selenium.get('http://127.0.0.1:8000/accounts/home/')
		next_page = self.selenium.find_element_by_link_text(
			"Click to go to your Exam page").click()
		self.assertEquals(self.selenium.current_url, 'http://127.0.0.1:8000/exams/home/')


	


