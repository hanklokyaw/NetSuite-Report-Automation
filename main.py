"""
main.py

This script sets up the necessary NetSuite login details and initiates the download of reports.
"""

from netsuite_login import download_reports

# Set up NetSuite login details
net_suite_username = 'NS_USERNAME'
net_suite_password = 'NS_PASSWORD'
net_suite_question_1 = 'NS_QUES1'
net_suite_answer_1 = 'NS_ANS1'
net_suite_question_2 = 'NS_QUES2'
net_suite_answer_2 = 'NS_ANS2'
net_suite_question_3 = 'NS_QUES3'
net_suite_answer_3 = 'NS_ANS3'

# Define the URLs for the reports
url1 = "your report url"
url2 = "your report url"
url3 = "your report url"

# Initiate the download of reports
download_reports(net_suite_username, net_suite_password, net_suite_question_1, net_suite_answer_1,
                 net_suite_question_2, net_suite_answer_2, net_suite_question_3, net_suite_answer_3,
                 url1, url2, url3)
