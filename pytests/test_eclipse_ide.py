from unittest import TestCase
from library.EclipseIDELibrary import EclipseIDELibrary


class EclipseIDETest(TestCase):
    """
    Test - Eclipse IDE
    """

    def setUp(self):
        print('EclipseIDETest.setUp()')
        self.eclipse_ide = EclipseIDELibrary()
        self.eclipse_ide.open_eclipse_ide()

    def test_about_screen(self):
        print('EclipseIDETest.test_about_screen()')
        self.eclipse_ide.click_menu('Help')
        self.eclipse_ide.click_menu('About Eclipse')
        self.eclipse_ide.click_button('OK')

    def tearDown(self):
        print('EclipseIDETest.tearDown()')
        self.eclipse_ide.close_eclipse_ide()
