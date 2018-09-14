#!/usr/bin/python
# coding=utf-8


import os
import sys
import time
from openstack import connection

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'https://cdn.myhwclouds.com/v1.0')

username = "xxxxxxxxxxx"
password = "xxxxxxxxxxx"
projectId = "xxxxxxxxxxxxxxxxxxxx"
userDomainId = "xxxxxxxxxxxxxxxxxxxxx"
auth_url = "https://iam.cn-north-1.myhuaweicloud.com/v3"

conn = connection.Connection(
    auth_url=auth_url,
    user_domain_id=userDomainId,
    project_id=projectId,
    username=username,
    password=password
)

def domain_create(domain_name, enterprise_project_id):
    print('Create a new acceleration domain name: ')
    attrs = {
        'domain_name': domain_name,
        'business_type': 'web',
        'sources': [
            {
                'ip_or_domain': '1.2.3.4',
                'origin_type': 'ipaddr',
                'active_standby': 1         # 1 means this source is active
            }
        ],
        'enterprise_project_id': enterprise_project_id
    }
    domain = conn.cdn.create_domain(**attrs)


def domains_query(_enterprise_project_id):
    print('List all domains:')
    for domain in conn.cdn.domains(enterprise_project_id='ALL'):
        print(domain)

    # Also support filtering by some attributes
    print('List domains by enterprise_project_id in "online" status: ')
    for domain in conn.cdn.domains(enterprise_project_id=_enterprise_project_id, domain_status='online'):
        print(domain)

    print('List domains in "web" type: ')
    for domain in conn.cdn.domains(enterprise_project_id='ALL', business_type='web'):
        print(domain)

    # You can list domains by page.
    print('List 3rd and 4th domains: ')
    for domain in conn.cdn.domains(enterprise_project_id='ALL', page_size=10, page_number=1):
        print(domain)


def domain_query_detail(domain_id, enterprise_project_id='ALL'):
    print('Get the domain detail:')
    domain = conn.cdn.get_domain(domain_id, enterprise_project_id)
    print(domain)
    print(domain.sources)



if __name__ == "__main__":
    domain_name = 'cdn-python-sdk.jiasuyuming.com'
    enterprise_project_id='xxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    enterprise_project_id=0 #default project
    domain_create(domain_name, enterprise_project_id)
    
    
    domains_query(enterprise_project_id)

    domain_id = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
    domain_query_detail(domain_id, enterprise_project_id)
