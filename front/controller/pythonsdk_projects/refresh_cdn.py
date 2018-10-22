#!/usr/bin/python2.7
# coding=utf-8
import os
import sys
import time
from openstack import connection
from openstack import utils

# utils.enable_logging(debug=True,stream=sys.stdout)


os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'https://cdn.myhwclouds.com/v1.0')

username = "your account"
password = "your password"
projectId = "projectId"
userDomainId = "your userId"
auth_url = "https://iam.cn-north-1.myhuaweicloud.com/v3"

conn = connection.Connection(
	auth_url=auth_url,
	user_domain_id=userDomainId,
	project_id=projectId,
	username=username,
	password=password
)


def refreshTask(refreshTask):
	refreshtask = conn.cdn.create_refresh_task(**refreshTask)
	#print(refreshtask)
	#print(type(refreshtask))
	print(refreshtask.id)
	return refreshtask


if __name__ == "__main__":
	try:
		file_type = sys.argv[1]
		url = sys.argv[2]
		refreshFileTask = {
			"type": file_type,
			"urls": [url],
		}
		refreshTask(refreshFileTask)
	except Exception as e:
		print("error")

