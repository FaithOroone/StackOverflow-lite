import json
import unittest
from unittest import TestCase

from question.views import app


class PostaQuestionTest(TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.request_data = {
            "question_id":1,
            "username":"username",
            "question":"question"
        }
#post a question
    def test_post_a_question(self):
        response = self.app.post('/api/v1/questions', data = json.dumps(self.request_data), content_type = 'application/json')
        self.assertEqual(response.status_code, 201)
        #self.assertIn("you have posted your first question", str(response.data))

    if __name__ == '__main__':
        unittest.main
