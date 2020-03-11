from src.tdd.was_run import WasRun, TestCase


class TestCaseTest(TestCase):
    def test_template_method(self):
        self.test = WasRun("test_method")
        self.test.run()
        assert ('set_up test_method tear_down ' == self.test.log)


TestCaseTest("test_template_method").run()
