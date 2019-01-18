#_*_coding:utf-8_*_
import unittest
import shutil
from testScenario import testScenarioCase
from testInterface import testActivity,testCharge,\
    testCoupon,testCredit,testDeal,testGrade,testManage,testProduct,\
    testSearch,testTag,testUser
import os,time,json
from globalVar import gl
from library import HTMLTESTRunnerCN
from library import scripts
from library.emailstmp import EmailClass


def loadTestsList():
    list = [testUser, testTag, testSearch, testProduct, testManage, testGrade, testDeal, testCredit,
            testCoupon, testCharge, testActivity]

    tests = [unittest.TestLoader().loadTestsFromModule(testScenarioCase)]
    for module in list:
        tests.append(unittest.TestLoader().loadTestsFromModule(module))
    return tests


if __name__=="__main__":
    suite = unittest.TestSuite()
    suite.addTests(loadTestsList())
    file_name = 'Report_{}.html'.format(int(time.time()  * 1000))

    filePath = os.path.join(gl.reportPath, file_name)  # 确定生成报告的路径
    print filePath

    with file(filePath, 'wb') as fp:
        runner = HTMLTESTRunnerCN.HTMLTestRunner(
            stream=fp,
            title=u'预发布-接口自动化测试报告',
            description=u'详细测试用例结果',  # 不传默认为空
            tester=u"yhleng"  # 测试人员名字，不传默认为小强
        )
        # 运行测试用例
        runner.run(suite)
        fp.close()

    #复制report到 templates/report/下
    shutil.copy(filePath, os.path.join(gl.templatesReportPath, file_name))

    # 发送钉钉消息
    msg = """★自动化测试消息★\n预发布接口自动化测试完成\n测试报告地址:http://60.205.217.8:5000/report/{}""".format(file_name)

    scripts.send_msg_dding(msg)
    #发送测试报告To Email
    EmailClass().send
