import unittest
from app.models import Articles

class ArticlesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Articles class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_article = Articles('bloomberg','Max Reyes','Deutsche Bank Staff Back in NYC Offices as Covid Cases Decline','Deutsche Bank AG employees returned to the lender’s U.S. headquarters in New York','assets.bwbx.io','assets.bwbx.io/is0woRr8jhN4.jpg','2022-01-31T17:36:33Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'CNN')
        self.assertEquals(self.new_article.author,'Peter Polle')
        self.assertEquals(self.new_article.title,'The tech scene in Africa-Is it the next big thing?')
        self.assertEquals(self.new_article.description,'A look at various tech hubs in Africa and the impact they have on the worlds economy')
        self.assertEquals(self.new_article.url,'techie.com')
        self.assertEquals(self.new_article.image,'techie.com/7643t94.jpg')
        self.assertEquals(self.new_article.date,'2018-04-11T07:57:16Z')