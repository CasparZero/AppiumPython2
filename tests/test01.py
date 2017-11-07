"""
The smoke test
"""


import unittest
import sys
#close automation compile
sys.dont_write_bytecode=True
sys.path.append("../config")
import settings
from UIModels import Home
        
        
class Demo(settings.Test):
    
    def test01(self):
        self.wd.find_element_by_xpath(Home.menu_button.xpath).click()


def main():
    unittest.main()
if __name__ == '__main__':
        main()