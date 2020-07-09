import os
from datetime import datetime
from settings import *


def gen_reports_dir():
    now = datetime.now()
    time_dir = now.strftime("%Y%m%d-%H%M%S")
    reports_dir = '/Users/gq.guo/tmp/api_test/reports/{}/{}'.format(TEST_PLATFORM,time_dir)
    if not os.path.exists(reports_dir):
        os.makedirs(reports_dir)
    return reports_dir

def run_test():
    reports_dir = gen_reports_dir()
    
    scripts = "{} --html={}/reports.html".format(COMMEND_SHELL,reports_dir)
    os.system(scripts)


if __name__ == "__main__":
    run_test()