'''
@Author: your name
@Date: 2020-08-05 09:38:19
LastEditTime: 2020-08-06 17:33:22
LastEditors: gq.guo
@Description: In User Settings Edit
@FilePath: /automate_test_paltform/conftest.py
'''
import os
import ssl
import json
import requests
import pytest

from datetime import datetime
from _pytest import terminal
from debugtalk import get_slack_channel
from slack import WebClient
from slack.errors import SlackApiError

def send_report_to_slack(channel, message, report_file):

    ssl_context = ssl.create_default_context()
    ssl_context.check_hostname = False
    ssl_context.verify_mode = ssl.CERT_NONE
    channel = get_slack_channel(channel)
    blocks = [
            {
                "type": "section",
                "text": {
                        "type": "mrkdwn",
                        "text": "Connector Api Test Report:\n`{}`\n↓↓↓ please check the report file ↓↓↓".format(message)
                }
            }]
    slack_token = os.environ['SLACK_TOKEN']
    client = WebClient(token=slack_token, ssl=ssl_context)
    try:
        client.chat_postMessage(channel=channel,blocks=blocks)
        client.files_upload(channels=channel,file=report_file,title="connector_api_test_report")
    except SlackApiError as e:
        assert e.response["error"]
        raise KeyError("error->{}".format(e)) 

def pytest_terminal_summary(terminalreporter, exitstatus, config):
    result = {}
    result['total'] = terminalreporter._numcollected
    result['passed'] = len(terminalreporter.stats.get('passed', []))
    failed_cases = terminalreporter.stats.get('failed', [])
    result['failed'] = len(failed_cases)
    result['error'] = len(terminalreporter.stats.get('error', []))
    result['skiped'] = len(terminalreporter.stats.get('skiped', []))

    report = {
        'run time': datetime.now().strftime('%Y/%m/%d %H:%M:%S'),
        'result': result
    }
    send_report_to_slack(channel='connector_api_test_report',message=report,report_file='report.html')
    return result


if __name__ == "__main__":
    message = {
        'scc': 12,
        'fail': 12,
        'skip': 29
    }
    print(message)
    send_report_to_slack(channel='connector_api_test_report', message=message, report_file='report.html')
    # print(r.json())
