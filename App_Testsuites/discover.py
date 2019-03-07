# -*- coding: GBK -*-
import sys
import os
cur_path=os.path.dirname(os.path.dirname(__file__))
root_path=os.path.split(cur_path)
sys.path.append(root_path)
import unittest
import HTMLTestRunner

current_path=os.path.dirname(os.path.realpath(__file__))
reporter_path=os.path.join(current_path,"report")
if not os.path.exists(reporter_path):os.mkdir(reporter_path)
test_dir='./'
suite=unittest.TestLoader().discover(test_dir,pattern="Test*.py")
if __name__=="__main__":
    html_report=reporter_path+r"\result.html"
    fp=open(html_report,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,verbosity=2,title="��Ԫ���Ա���",description="����ִ�����")
    runner.run(suite)



