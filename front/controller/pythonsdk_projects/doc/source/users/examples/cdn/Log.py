#!/usr/bin/python
# coding=utf-8


import os
import sys
import time
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'https://cdn.myhwclouds.com/v1.0')
"""
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

"""
projectId = "7cd3305592004a8c8c0de3684ead0392"
domain = "3e15951cbe4f49559f987c9e96013c63"   # example: domain = "myhuaweicloud.com"
region= "cn-north-1"    # example: region = "cn-north-1"
AK = "8Y20CJ5GY9QIXEKIOYHM"
SK = "xipVpbLERJ5nLnxiJsjcgTX3EWBhcmkUpbgVgoFG"
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

def list_logs(domain_name, today):
    #today = '1532620800000'
    logs = conn.cdn.logs(domain_name=domain_name, query_date=today, page_number=1, page_size=10, enterprise_project_id="ALL")
    log_list = list(logs)
    print(log_list)
    # for log in conn.cdn.logs(domain_name=domain_name, query_date=today):
    #     print(log)

if __name__ == "__main__":
    today = int(time.time() * 1000) - 24 * 3600 * 1000
    #domain = "xwdiliantest2.it-ba.com"
    domain = "yingxionghuyu.it-ba.com"
    #domain = "jst.it-ba.com"
    list_logs(domain, today)


