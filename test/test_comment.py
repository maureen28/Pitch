from app.models import Comment, User
from app import db


def setUp(self):
        self.user_rain = User(username = 'Rain',password = 'banana', email = 'nimo@gmail.com')
        self.new_comment = Comment(post_id=123,comment='I love pitch', user = self.user_rain )
  
        
def tearDown(self):
        Comment.query.delete()
        User.query.delete()
        
        
def test_check_instance_variables(self):
        self.assertEquals(self.new_comment.post_id,123)
        self.assertEquals(self.new_comment.comment,'I love pitch')
        self.assertEquals(self.new_comment.user,self.user_rain)
        
        
def test_save_comment(self):
        self.new_comment.save_comment()
        self.assertTrue(len(Comment.query.all())>0)
        
        
def test_get_comment_by_id(self):

        self.new_comment.save_comment()
        got_comments = Comment.get_comments(12345)
        self.assertTrue(len(got_comments) == 1)