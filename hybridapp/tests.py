from django.test import TestCase

from hybridapp.models import Bid, ProseLint, PyEnchant, Pedant

# Create your tests here.
class BidTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_scoring(self):
        text = "THis is no grammar.Lol"
        bid = Bid(text)
        score = bid.get_quality_score()
        print(score)
        
class ProseLintTestCase(TestCase):
    def setUp(self):
        pass

    def test_suggestions(self):
        text = "Hello.   People have said\
                You don't have much code, that to do some review. \
                Only I want say, that not need place business-logic in models. Like this"
        suggestions = ProseLint.get_suggestions(text)
        if suggestions is None:
            print("No suggestions")
        else:
            for suggestion in suggestions:
                print(suggestion)
                
class PyEnchantTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_error_count(self):
        text = "Thiz txtt hazz three errors"
        error_count = PyEnchant.get_error_count(text)
        actual_error_count = 3
        self.assertEquals(error_count, actual_error_count)
        
class PedantTestCase(TestCase):
    def setUp(self):
        pass
        
    def test_validate(self):
        text = "Full stop.Without a space before."
        Pedant.validate(text)
