#!/usr/bin/python
# coding=utf-8


import os
import sys
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'https://cdn.myhwclouds.com/v1.0')

username = "c00353195"
password = "Huawei@1234"
projectId = "65972708b5bd4948b194352e897d429b"
userDomainId = "913eb32a20794910aab55d7339a8dad1"
auth_url = "https://iam.cn-north-1.myhuaweicloud.com/v3"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)
"""
projectId="65972708b5bd4948b194352e897d429b"
domain="913eb32a20794910aab55d7339a8dad1"
region="cn-north-1"
AK="FVMZATNRBWYHIRRIK1AC"
SK="8B9tTenfv0mYEeBVZjsly1uBdppxdje6caPsWNAK"

conn = connection.Connection(
              project_id=projectId,
              domain=domain,
              region=region,
              ak = AK,
              sk = SK)
"""
def refreshTask(refreshTask):
    print("refresh files or dirs:")
    refreshtask = conn.cdn.create_refresh_task(**refreshTask)
    print(refreshtask)



if __name__ == "__main__":
    refreshFileTask={
        "type": "file",
        "urls": ["http://cdn-python-sdk-c2.it-ba.com/img/a5.jpg",
                 "http://cdn-python-sdk-c2.it-ba.com/img/a7.jpg"]
    }
    refreshDirTask={
        "type": "directory",
        "urls": ["http://cdn-python-sdk-c2.it-ba.com/img/",
                "http://cdn-python-sdk-c2.it-ba.com/js/plugins/"]
    }
    refreshTask(refreshFileTask)
    refreshTask(refreshDirTask)

