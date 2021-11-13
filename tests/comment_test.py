import unittest
from app.models import Post, User, Comment

class TestPost(unittest.TestCase):

  def setUp(self):
      self.user_Larvine = User(first_name="Larvine",
                            last_name="Asande",
                            username="monkey",
                            password="monkey",
                            email="monkey@mail.com")
      self.new_post = Post(post_title="Sample Title",
                            post_content="Hey Yooh!!.",
                            user_id=self.user_Larvine.id)
      self.new_comment = Comment(comment="Awesome",
                                post_id=self.new_post.id,
                                user_id=self.user_Larvine.id)

  def test_instance(self):
      self.assertTrue(isinstance(self.user_Larvine, User))
      self.assertTrue(isinstance(self.new_post, Post))
      self.assertTrue(isinstance(self.new_comment, Comment))