# -*- coding: GBK -*-
import unittest
from App_Testsuites.Base_testcase import BaseTestCase
from Pageobjects.App_Register import Register
from appium.webdriver.common.mobileby import By
import time
class Test_register(BaseTestCase):
    def test_register(self):
        re=Register(self.driver)
        re.register("lixiuzhi50","247834555@qq.com","1997080333333")
        re.register("lixiuzhi0","247834@qq.com","19960618",)
        try:
            self.assertEqual(self.aser,"���ܱ���¼")
            print("�ɹ�ע��")
        except Exception as e:
            print("ע��ʧ��")



if __name__=="__main__":
    unittest.main()

