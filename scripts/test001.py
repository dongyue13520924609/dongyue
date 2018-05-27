import pytest,allure

class Test_001:
    @allure.step(title="测试步骤001")
    @pytest.mark.parametrize("a",[1,2,3])
    def test_abc(self,a):
        assert a != 2

    @allure.step(title="测试步骤002")
    @pytest.mark.parametrize("a",[1,3,5])
    def test_bcd(self,a):
        allure.attach("描述","我是测试步骤002")
        assert a != 2

