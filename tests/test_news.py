import unittest
from app.models import Sources,Articles,Top



class SourceTest(unittest.TestCase):

    def setUp(self):

        self.new_source = Sources('123','cnn','best news','https://blabla.com','blabla','en','us')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source, Sources))
    
class ArticlesTest(unittest.TestCase):

    def setUp(self):

        self.new_article = Articles('123','cnn','best news','https://blabla.com','blabla','jjj','dddnnsbbbsb','gg','ggg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article, Articles))

class TopTest(unittest.TestCase):

    def setUp(self):

        self.new_headline = Top('123','cnn','best news','https://blabla.com','blabla','jjj','dddnnsbbbsb','gg','ggg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_headline, Top))
