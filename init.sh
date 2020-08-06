###
 # @Author: your name
 # @Date: 2020-08-04 17:07:36
 # @LastEditTime: 2020-08-05 17:00:18
 # @LastEditors: Please set LastEditors
 # @Description: In User Settings Edit
 # @FilePath: /api_test/init.sh
### 
rm -rf testcases
rm -rf testdata 
rm -rf config
rm debugtalk.py 
rm -rf apienv

if [ ! -d "$HOME/tmp/api_test/apienv" ]; then
  python3 -m venv apienv
fi

mv $HOME/.jenkins/workspace/api_test_data/* $HOME/tmp/api_test/
cd $HOME/tmp/api_test/

source $HOME/tmp/api_test/apienv/bin/activate
pip install httprunner
pip install slackclient

hrun testcases --html=report.html --self-contained-html
