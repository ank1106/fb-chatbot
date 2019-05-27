from django.test import TestCase
from .wiki_api import searchWiki
from .fb import FBMessenger

class WikiSearchTestCase(TestCase):
    def setUp(self):
        pass

    def test_ambuigation(self):
        res = searchWiki("Mercury")
        self.assertEqual(len(res) , 3)
        self.assertEqual(res , [{'title': 'Mercury', 'link': 'https://en.wikipedia.org/wiki/Mercury', 'des': 'Mercury usually refers to:'}, {'title': 'Mercury (element)', 'link': 'https://en.wikipedia.org/wiki/Mercury_(element)', 'des': 'Mercury is a chemical element with the symbol Hg and atomic number 80. It is commonly known as quicksilver and was formerly named hydrargyrum ( hy-DRAR-jər-əm).'}, {'title': 'Mercury (planet)', 'link': 'https://en.wikipedia.org/wiki/Mercury_(planet)', 'des': 'Mercury is the smallest and innermost planet in the Solar System. Its orbital period around the Sun of 87.97 days is the shortest of all the planets in the Solar System.'}])
    
    def test_single_page_search(self):
        res = searchWiki("India")
        self.assertEqual(len(res) , 1)
        self.assertEqual(res , [{'title': 'India', 'link': 'https://en.wikipedia.org/wiki/India', 'des': 'India (ISO: Bhārat), also known as the Republic of India (ISO: Bhārat Gaṇarājya), is a country in South Asia.'}])


    def test_value_error_for_non_string_query(self):
        with self.assertRaises(ValueError):
            res = searchWiki(23423)


class MessengerAPITestCase(TestCase):

    def test_hub_challenge_verification(self):
        response = self.client.get('/fb/?hub.verify_token=sdf3esdaf32&hub.challenge=secret_token')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'secret_token')
    
    def test_strip_tags_method(self):
        fb = FBMessenger("fb_access_token")
        self.assertEqual(fb.stripTags("<h4>hi from <b>bot</b></h4>"), "hi from bot")
        
