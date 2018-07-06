import allure

class Test_01:
    @allure.step(title="第一个测试")
    def test_001(self):
        assert 1