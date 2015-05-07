from django.test import TestCase

from model_mommy import mommy

from apps.questions.models import Question, Option


class QuestionTestCase(TestCase):

    def setUp(self):
        self.question = mommy.make('Question')
        self.option = mommy.make('Option')
        print self.question.question_text
        print self.option.option_text
        print self.option.is_right_answer

    def test_question(self):
        self.assertEquals(isinstance(self.question, Question), True)

    def test_option(self):
        self.assertEquals(isinstance(self.option, Option), True)
