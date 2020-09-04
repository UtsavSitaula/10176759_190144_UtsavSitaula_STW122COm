from assignment.qury import qry
import unittest

class testing(unittest.TestCase):
    o=qry()

    def test_login(self):
        actual_result = self.o.login("0010","utsav","001A","000","aug 5")
        self.assertTrue(actual_result)


    def test_delete(self):
        actual_result = self.o.delete(1415)
        self.assertTrue(actual_result)

    def test_search(self):
        actual_result = self.o.search(00)
        self.assertTrue(actual_result)

    def test_login1(self):
        actual_result = self.o.userlogin("nayan","guessme")
        self.assertTrue(actual_result)

    def test_autentication(self):
        actual_result = self.o.authentication("nayan","guessme")
        self.assertTrue(actual_result)



