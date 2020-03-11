class TestCase:
    def __init__(self, name: str):
        self.name = name

    def set_up(self):
        pass

    def run(self):
        result = TestResult()
        result.test_started()
        self.set_up()
        method = getattr(self, self.name)
        method()
        self.tear_down()
        return result

    def tear_down(self):
        pass


class TestResult:
    def __init__(self):
        self.runCount = 0

    def test_started(self):
        self.runCount += 1

    def summary(self):
        return f"{self.runCount} run, 0 failed"


class WasRun(TestCase):
    def set_up(self):
        self.log = 'set_up '

    def test_method(self):
        self.was_run = 1
        self.log += 'test_method '

    def test_broken_method(self):
        raise Exception

    def tear_down(self):
        self.log += 'tear_down '
