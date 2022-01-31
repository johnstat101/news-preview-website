import unittest
from app.models import Sources

class SourcesTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Sources class
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test
        '''
        self.new_source = Sources('Bloomberg','Bloomberg News','Bloomberg delivers business and markets news, data, analysis, and video to the world','bloomberg.com','general','U.S.A','en')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Sources))

    def test_variables(self):
        self.assertEquals(self.new_source.id,'Bloomberg')
        self.assertEquals(self.new_source.name,'Bloomberg News')
        self.assertEquals(self.new_source.description,'Bloomberg delivers business and markets news, data, analysis, and video to the world')
        self.assertEquals(self.new_source.url,'bloomberg.com')
        self.assertEquals(self.new_source.category,'general')
        self.assertEquals(self.new_source.country,'U.S.A')
        self.assertEquals(self.new_source.language,'en')