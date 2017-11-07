"""
The Home view of application.
"""

from controls_core import IOSButton

   
class Home():
    
    menu_button = IOSButton('NMenu',
                          "//UIAApplication[1]/UIAWindow[1]/UIAButton[1]")
    