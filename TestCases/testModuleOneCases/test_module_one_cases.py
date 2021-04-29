# coding=utf-8
import os, allure, pytest, logging.config


@allure.feature("模块名XXX")
class Test_layerlevel_management:

    @pytest.mark.smoke()
    @allure.title("展开和关闭图层")
    @pytest.mark.run(order=1)
    def test_xxx1(self, po_layer):
        po_layer.layer_hide()

    @pytest.mark.smoke()
    @allure.title("最小级别全部加1")
    @pytest.mark.run(order=1)
    def test_xxx2(self, po_layer):
        po_layer.layer_edit_min()

    @pytest.mark.smoke()
    @allure.title("重置图层")
    @pytest.mark.run(order=1)
    def test_xxx3(self, po_layer):
        po_layer.layer_resert()
        assert po_layer.title == "tfjiao"


if __name__ == '__main__':
    pytest.main(['Test_layerlevel_management::test_xxx1'])