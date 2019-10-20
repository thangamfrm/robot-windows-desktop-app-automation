
class SimpleTestLibrary:
    """
    Library to run from Jenkins
    """

    def __init__(self):
        print('SimpleTestLibrary.__init__')

    def setup_simple_test_library(self):
        print('setup_simple_test_library')

    def say_hello_world(self):
        print('Hello World!')

    def say_fail(self):
        print('Say Fail!')
        assert 1 == 2

    def teardown_simple_test_library(self):
        print('teardown_simple_test_library')
