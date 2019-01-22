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
    #unittest测试套件
    suite = unittest.TestSuite()
    suite.addTests(loadTestsList())

    #测试报告文件名
    time_str = time.strftime('%Y%m%d_%H%M%S', time.localtime())
    report_dir = time_str.split('_')[0]
    file_name = 'Report_{}.html'.format(time_str)
    portdir = os.path.join(gl.reportPath, report_dir)

    #按日期创建测试报告文件夹
    if not os.path.exists(portdir):
        os.mkdir(os.path.join(gl.reportPath,report_dir))
    rpath = os.path.join(gl.reportPath, report_dir)
    filePath = os.path.join(rpath, file_name)  # 确定生成报告的路径
    print filePath

    #执行测试并生成测试报告文件
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

    #复制report下子文件夹到 templates/report/下
    split_path = os.path.dirname(filePath).split("\\")
    low_path = split_path[split_path.__len__() - 1]
    web_path = os.path.join(gl.templatesReportPath,low_path)
    if not os.path.exists(web_path):
        shutil.copytree(os.path.dirname(filePath), web_path)
    else:
        shutil.copy(filePath, os.path.join(web_path, file_name))

    #发送钉钉模版测试结果
    result_str = """共{}个用例, 通过{}, 失败{}, 错误{}, 通过率{}""".format(
        gl.get_value('sum'),
        gl.get_value('passed'),
        gl.get_value('failed'),
        gl.get_value('error'),
        gl.get_value('passrate')
    )

    # 发送钉钉消息
    msg = """预发布接口自动化测试已完成,{}\n测试报告地址:http://60.205.217.8:5000/report/{}/{}""".format(result_str, low_path, file_name)
    scripts.send_msg_dding(msg)

    #发送测试报告To Email
    EmailClass().send
