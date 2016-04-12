import os
import unittest

from os.path import exists
from unittest.mock import patch

from pythonbackend.Exercise import Exercise
from pythonbackend import utils

import helper

class TestMcRight(unittest.TestCase):

  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
selected_option = 2
''',
      "DC_SOLUTION": '''
'''
    }

  def test_mcSuccess(self):
    self.data["DC_SCT"] = '''
test_mc(2, ["This is wrong", "This is right"])
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], True)
    self.assertEqual(sct_payload['message'], "This is right")


class TestMcWrong(unittest.TestCase):

  def setUp(self):
    self.data = {
      "DC_PEC": '''
# pec comes here
      ''',
      "DC_CODE": '''
selected_option = 3
''',
      "DC_SOLUTION": '''
'''
    }

  def test_mcFail(self):
    self.data["DC_SCT"] = '''
test_mc(2, ["This is wrong", "This is right", "Oh no, not correct"])
    '''
    self.exercise = Exercise(self.data)
    self.exercise.runInit()
    output = self.exercise.runSubmit(self.data)
    sct_payload = helper.get_sct_payload(output)
    self.assertEqual(sct_payload['correct'], False)
    self.assertEqual(sct_payload['message'], "Oh no, not correct")