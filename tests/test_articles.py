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
        self.new_article = Articles('bloomberg','Max Reyes','Deutsche Bank Staff Back in NYC Offices as Covid Cases Decline','Deutsche Bank AG employees returned to the lenders U.S. headquarters in New York','assets.bwbx.io','assets.bwbx.io/is0woRr8jhN4.jpg','2022-01-31T17:36:33Z')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article,Articles))

    def test_to_check_instance_variables(self):
        self.assertEquals(self.new_article.id,'bloomberg')
        self.assertEquals(self.new_article.author,'Max Reyes')
        self.assertEquals(self.new_article.title,'Deutsche Bank Staff Back in NYC Offices as Covid Cases Decline')
        self.assertEquals(self.new_article.description,'Deutsche Bank AG employees returned to the lenders U.S. headquarters in New York')
        self.assertEquals(self.new_article.url,'assets.bwbx.io')
        self.assertEquals(self.new_article.image,'assets.bwbx.io/is0woRr8jhN4.jpg')
        self.assertEquals(self.new_article.date,'2022-01-31T17:36:33Z')