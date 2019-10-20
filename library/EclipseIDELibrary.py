from appium import webdriver
import time


class BaseWinAppDriverLibrary:
    """
    Base/Wrapper class for interacting with WinAppDriver (Appium)
    """

    def __init__(self):
        print('BaseWinAppDriverLibrary - __init__')

    def log(self, msg):
        print(msg)

    def tear_down(self):
        print('BaseWinAppDriverLibrary.tear_down()')


class EclipseIDELibrary(BaseWinAppDriverLibrary):
    """
    EclipseIDE Library
    """

    def __init__(self):
        super().__init__()
        self.log('EclipseIDELibrary.__init__')

    def open_eclipse_ide(self):
        self.log('Setup Eclipse IDE')
        desired_caps = {}
        desired_caps['app'] = 'C:\\Users\\GSPANN Guest\\sw\\eclipse\\eclipse.exe'
        self.win_app_driver = webdriver.Remote(
             command_executor='http://127.0.0.1:4723',
             desired_capabilities=desired_caps)
        self.win_app_driver.implicitly_wait(5)
        self.handle_workspace_dialog()

    def handle_workspace_dialog(self):
        self.log('title: ' + self.win_app_driver.title + ' , Page: '  + self.win_app_driver.page_source)
        ok_btn = self.win_app_driver.find_element_by_name('OK')
        ok_btn.click()
        time.sleep(15)
        self.switch_window()

    def switch_window(self):
        self.log('switch to window')
        try:
            current_window_handle = self.win_app_driver.current_window_handle
            self.log('Current Window Handle: ' + current_window_handle)
            window_handles = self.win_app_driver.window_handles
            self.log('Number of Windows: ' + str(len(window_handles)))
            for wh in window_handles:
                self.log('Window Handle: ' + wh)
                if wh is not current_window_handle:
                    self.win_app_driver.switch_to.window(wh)
                    self.log('Switched to window with title: ' + self.win_app_driver.title + ', Page Source: ' + self.win_app_driver.page_source)
                    return True
        except Exception as ex:
            self.log('Exception in switch_window: ' + str(ex))
        return False

    def wait_for_element(self, element_name, max_wait):
        wait_per_poll = 5
        while max_wait > 0:
            try:
                self.win_app_driver.find_element_by_name(element_name)
                self.log("Element Found by Name: " + element_name)
            except Exception as ex:
                self.log('Unable to find element by name')

            # helps to debug! - try using alternate locator!
            try:
                self.win_app_driver.find_element_by_class_name(element_name)
                self.log('Element found by class name: ' + element_name)
                return
            except Exception as ex:
                self.log('Unable to find element by class')

            time.sleep(wait_per_poll)
            max_wait = max_wait - wait_per_poll

        raise Exception('Unable to find element: ' + element_name + ' , Waited For: ' + max_wait)

    def click_menu(self, element_name):
        self.click(element_name)
        self.wait(3)

    def click_button(self, element_name):
        self.click(element_name)
        self.wait(3)

    def click(self, element_name):
        self.win_app_driver.find_element_by_name(element_name).click()

    def wait(self, seconds):
        time.sleep(int(seconds))

    def verify_about_menu(self):
        self.log('verify_about_menu')
        try:
            self.win_app_driver.find_element_by_name('Help').click()
            time.sleep(3)
            self.win_app_driver.find_element_by_name('About Eclipse').click()
            time.sleep(3)
            self.win_app_driver.find_element_by_name('OK').click()
        except Exception as ex:
            raise Exception('Unable to verify About Menu!')

    def close_eclipse_ide(self):
        self.log('Teardown Eclipse IDE')
        if self.win_app_driver:
            try:
                self.win_app_driver.close()
                ok_btn = self.win_app_driver.find_element_by_name('OK')
                ok_btn.click()
            except Exception as ex:
                self.log('Unable to close Eclipse IDE: ' + str(ex))
            finally:
                self.win_app_driver.quit()
                self.win_app_driver = None
