import sys
import os
import unittest
from appium import webdriver
from time import sleep


PROJECT_ROOT =os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, PROJECT_ROOT)
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'extras_apps'))
sys.path.insert(0, os.path.join(PROJECT_ROOT, 'libs'))  


# set  Desired Capabilities
desired_caps = {}
desired_caps['appium-version'] = '1.0'
desired_caps['platformName'] = 'iOS'
desired_caps['platformVersion'] = '9.2'
desired_caps['deviceName'] = 'iPhone 5s'
desired_caps['app'] = os.path.abspath(os.path.join(PROJECT_ROOT, 'apps/AppName.app'))


class Test(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        super(Test, cls).setUpClass()
        # create new session with appium server
        cls.wd =  webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        # set default find control time
        cls.wd.implicitly_wait(60)
        
    @classmethod
    def tearDownClass(cls):
        super(Test, cls).tearDownClass()
        # close the session of  with appium server.
        cls.wd.quit()