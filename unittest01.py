'''
Author:
Date  :
'''
# coding=utf-8

import os, time
import unittest
# 导入HTMLTestRunner库，放在脚本的开头也是一样
import HTMLTestRunnerCN
# import HTMLTestRunner
from selenium import webdriver


class TestAuto(unittest.TestCase):
    # cls.dr = webdriver.Chrome(r'D:\Chromedriver\chromedriver.exe')
    # cls.dr.maximize_window()
    # print('测试浏览器为:{0}'.format(cls.dr.name))
    # time.sleep(1)
    dr = webdriver.Chrome(r'D:\Chromedriver\chromedriver.exe')
    dr.maximize_window()
    print('测试浏览器为:{0}'.format(dr.name))
    time.sleep(1)

    @classmethod
    def setUpClass(cls):
        print('start!')

        print(u'访问巡服带教测试环境后台管理系统')
        cls.dr.get('http://119.145.99.218:17182/#/login')
        print('测试地址为:{0}'.format(cls.dr.current_url))
        time.sleep(1)
        xpath = cls.dr.find_element_by_xpath
        print(u'点击账号登录，进入账号密码待输入界面')
        # 捕捉账号文本栏 , 进行输入账号
        xpath('//*[@id="app"]/div/div[2]/div[1]/form/div[2]/div/div/input').send_keys(u'NBTEST4')
        time.sleep(0.3)
        # 捕捉密码文本栏 , 进行输入密码
        xpath('//*[@id="app"]/div/div[2]/div[1]/form/div[3]/div/div/input').send_keys(u'123456')
        time.sleep(0.3)
        print(u'点击登录')
        xpath('//*[@id="app"]/div/div[2]/div[1]/form/button').click()
        time.sleep(2)
        cls.dr.refresh()
        time.sleep(2)
        print(u'初始环境，进入下一步验证')

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
        print('end')

    def testCase_001(cls):
        '''验证用户是否登录完成'''
        print(u'test_001:验证后台登录')
        cls.assertEqual('http://119.145.99.218:17182/#/dashboard', cls.dr.current_url)
        url = 'http://119.145.99.218:17182/#/dashboard'
        if url == 'http://119.145.99.218:17182/#/dashboard':
            print('..登录成功')
        else:
            print('..登录失败')

    def testCase_002(cls):
        '''验证明细功能'''
        print(u'test_002:验证功能')
        xpath = cls.dr.find_element_by_xpath
        time.sleep(2)
        print(u'..点击页面')
        xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/div[4]/li/div/span').click()
        time.sleep(1)
        xpath('//*[@id="app"]/div/div[1]/div[1]/div/ul/div[4]/li/ul/a[2]/li/span').click()
        time.sleep(5)
        print(u'..点击设备详情')
        # xpath('//*[@id="complex-panel-scroll"]/div[1]/div/div/div[1]/div[1]/span[2]/span').click()
        # 断言
        restext = xpath('//*[@id="complex-panel-scroll"]/div[1]/div/div/div[1]/div[1]/span[2]/span').text
        if restext == '广州分公司':
            print('..断言成功')
        else:
            print('..断言失败')


# 添加Suite
# def Suite():
#     #定义一个单元测试容器
#     suiteTest = unittest.TestSuite()
#     #将测试用例加入到容器
#     suiteTest.addTest(TestAuto("testCase_001"))
#     suiteTest.addTest(TestAuto("testCase_002"))
#     return suiteTest

if __name__ == '__main__':
    suiteTest = unittest.TestSuite()  # 将测试用例加入到容器
    suiteTest.addTest(TestAuto("testCase_001"))
    suiteTest.addTest(TestAuto("testCase_002"))
    now = time.strftime('%Y-%m-%d  %H-%M-%S')
    report_file = r"D:\\A-result\\report\\" + now + "_test_report.html"
    print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
    with open(report_file, 'wb') as report:
        runner = HTMLTestRunnerCN.HTMLTestReportCN(stream=report, title='单元测试报告', description=u'用例执行结果', )
        runner.run(suiteTest)
        report.close()
