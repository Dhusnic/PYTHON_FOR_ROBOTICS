import unittest
import coolify


class Test_coolify(unittest.TestCase):
    def test_name(self):
        name="dhusnic"
        self.assertTrue(coolify.coolify(name) == "dhusnic is cool")
        self.assetFalse(coolify.coolify(name) == "dhusnic")
        
if __name__ == '__main__':
    unittest.main()