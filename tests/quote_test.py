import unittest
from app.models import Quote

class TestQuote(unittest.TestCase):
  def setUp(self):
      """
      Set up method that will run before every Test
      """
      self.random_quote = Quote("Larvine Asande", "Hey")

  def test_instance(self):
      self.assertTrue(isinstance(self.random_quote, Quote))

  def test_init(self):
      self.assertEqual(self.random_quote.author, "Larvine Asande")
      self.assertEqual(self.random_quote.quote,"Hey")