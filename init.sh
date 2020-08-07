###
 # @Author: gq.guo
 # @Date: 2020-08-04 17:07:36
 # @LastEditTime: 2020-08-07 14:15:59
 # @LastEditors: gq.guo
 # @Description: In User Settings Edit
 # @FilePath: /api_test/init.sh
### 
rm -rf $HOME/tmp/apitest/

cd $HOME/tmp/api_test/
python3 -m venv apienv
mv $HOME/.jenkins/workspace/api_test_data/* $HOME/tmp/api_test/


source $HOME/tmp/api_test/apienv/bin/activate
pip install httprunner
pip install slackclient

hrun testcases --html=report.html --self-contained-html
