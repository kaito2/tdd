from typing import Callable, List


class TestResult:
    def __init__(self) -> None:
        self.run_count: int = 0
        self.error_count: int = 0

    def test_started(self) -> None:
        self.run_count += 1

    def test_failed(self) -> None:
        self.error_count += 1

    def summary(self) -> str:
        return f"{self.run_count} run, {self.error_count} failed"


class TestCase:
    def __init__(self, name: str) -> None:
        self.name: str = name

    def set_up(self) -> None:
        pass

    def run(self, result: TestResult) -> None:
        result.test_started()
        self.set_up()
        try:
            method: Callable = getattr(self, self.name)
            method()
        except:
            result.test_failed()
        self.tear_down()

    def tear_down(self) -> None:
        pass


class TestSuite:
    def __init__(self) -> None:
        self.tests: List[TestCase] = []

    def add(self, test) -> None:
        self.tests.append(test)

    def run(self, result: TestResult) -> None:
        for test in self.tests:
            test.run(result)


class WasRun(TestCase):
    def set_up(self) -> None:
        self.log: str = 'set_up '

    def test_method(self) -> None:
        self.was_run: int = 1
        self.log += 'test_method '

    def test_broken_method(self) -> None:
        raise Exception

    def tear_down(self) -> None:
        self.log += 'tear_down '
