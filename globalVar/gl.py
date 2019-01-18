#_*_coding:utf-8_*_
import os,sys

global globalPath #global包路径
global configPath #config包路径
global dataPath #Data路径
global dataScenarioPath #场景路径
global tcodePath #t-code路径
global reportPath #报告路径
global configFile
global debugFile
global webPath
global templatesPath
global templatesReportPath


PATH =lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

globalPath = os.path.abspath(os.path.dirname(__file__))
configPath = os.path.join(os.path.dirname(globalPath),'config')
dataPath = os.path.join(PATH(os.path.dirname(globalPath)),'data')
dataScenarioPath = os.path.join(dataPath,'Scenario')
tcodePath = os.path.join(dataPath,'TCode')
reportPath = os.path.join(os.path.dirname(globalPath),'report')
configFile = os.path.join(configPath,'config.yaml')
debugFile = os.path.join(reportPath,'logging.log')
webPath = os.path.join(os.path.dirname(globalPath), 'web')
templatesPath = os.path.join(webPath, 'templates')
templatesReportPath = os.path.join(templatesPath, 'report')

if __name__=="__main__":
    print( templatesPath)
    print( templatesReportPath)
    print globalPath
    print configPath
    print dataPath
    print dataScenarioPath
    print tcodePath
    print reportPath
    print configFile