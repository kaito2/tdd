class TestCase:
    def __init__(self, name: str):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()

    def tear_down(self):
        pass


class WasRun(TestCase):
    def set_up(self):
        self.log = 'set_up '

    def test_method(self):
        self.was_run = 1
        self.log += 'test_method '

    def tear_down(self):
        self.log += 'tear_down '
