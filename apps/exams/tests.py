from django.test import TestCase, LiveServerTestCase
from django.contrib.auth.models import User

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

from apps.accounts.forms import RegistrationForm
from apps.accounts.views import *
from apps.exams.models import Exam, Test, Answer
from apps.questions.models import Question, Option
from apps.exams import views


# Create your tests here.

class ExamTestCase(LiveServerTestCase):

	def setUp(self):
		self.selenium = webdriver.Firefox()
		self.selenium.maximize_window()
		super(ExamTestCase, self).setUp()

	# def tearDown(self):
	# 	self.selenium.quit()
	# 	super(ExamTestCase, self).tearDown()

	def test_question_display(self):
		# link = self.selenium.get('127.0.0.1:8000/exams/home')
		# self.selenium.find
		login_page = self.selenium.get('http://127.0.0.1:8000/accounts/login/')
		username = self.selenium.find_element_by_id('id_username')
		username.send_keys('testuser')
		password = self.selenium.find_element_by_id('id_password')
		password.send_keys('test')
		self.selenium.find_element_by_xpath('//input[@value = "Login"]').click()
		next_page = self.selenium.find_element_by_link_text(
			"Click to go to your Exam page").click()
		# WebDriverWait(10, self.selenium)
		question_page = self.selenium.find_element_by_link_text(
			"exam2").click()
		# self.selenium.quit()

	def test_option_selection(self):
		self.test_question_display()
		self.selenium.find_element_by_xpath('//input[@id = "option3"]').click()
		self.selenium.find_element_by_xpath('//input[@value="Submit"]').click()
		self.selenium.find_element_by_xpath('//input[@id = "option1"]').click()
		self.selenium.find_element_by_xpath('//input[@value="Submit"]').click()

	def test_result_page(self):
		self.test_option_selection()
		self.assertEquals(self.selenium.current_url, 'http://127.0.0.1:8000/exams/2/result')




		

