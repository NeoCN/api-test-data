'''
Author: your name
Date: 2020-08-05 08:42:59
LastEditTime: 2020-08-05 09:37:42
LastEditors: Please set LastEditors
Description: In User Settings Edit
FilePath: /api_test/send_report.py
'''
import requests

from datetime import datetime
from _pytest import terminal


def send_report_to_slack(message):
    url = "https://hooks.slack.com/services/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"
    data = {
        'text':message
    }
    r = requests.post(url,json=data)

    
def pytest_terminal_summary(terminalreporter,exitstatus,config):
    result = {}
    result['total'] = terminalreporter._numcollected
    result['passed'] = len(terminalreporter.stats.get('passed',[]))
    result['failed'] = len(terminalreporter.stats.get('failed',[]))
    result['error'] = len(terminalreporter.stats.get('error',[]))
    result['skiped'] = len(terminalreporter.stats.get('skiped',[]))
    report = {
        'report':'connector api test result',
        'run time':datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        'result':result
    }
    send_report_to_slack(str(report))
    print(result)
    # return result

if __name__ == "__main__":
    message = {
            'scc':12,
            'fail':12,
            'skip':29
        }
    send_report_to_slack(str(message))
    