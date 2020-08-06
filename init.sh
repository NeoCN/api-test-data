###
 # @Author: gq.guo
 # @Date: 2020-08-04 17:07:36
 # @LastEditTime: 2020-08-06 17:57:28
 # @LastEditors: gq.guo
 # @Description: In User Settings Edit
 # @FilePath: /api_test/init.sh
### 
rm -rf $HOME/tmp/apitest/

if [ ! -d "$HOME/tmp/api_test/apienv" ]; then
  python3 -m venv apienv
fi

mv $HOME/.jenkins/workspace/api_test_data/* $HOME/tmp/api_test/
cd $HOME/tmp/api_test/

source $HOME/tmp/api_test/apienv/bin/activate
pip install httprunner
pip install slackclient

hrun testcases --html=report.html --self-contained-html
