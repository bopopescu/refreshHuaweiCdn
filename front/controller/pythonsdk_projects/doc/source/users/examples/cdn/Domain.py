#!/usr/bin/python
# coding=utf-8


import os
import sys
import time
from openstack import connection
from openstack import utils

os.environ.setdefault('OS_CDN_ENDPOINT_OVERRIDE', 'https://cdn.myhwclouds.com/v1.0')

#utils.enable_logging(debug = True, stream = sys.stdout)


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
    domain_name = 'cdn-python-sdk-c9.it-ba.com'
    domain_id = 'ff80808265d147770165d1d1a98711fa'
    enterprise_project_id='721f6aca-27ea-4a34-a1ae-dbe5d8d50558'
    #domain_id = 'ff808082658e59f201658f802a0c270a'   
    #domain_create(domain_name, enterprise_project_id)
    
    #domains_query(enterprise_project_id)
    
    domain_query_detail(domain_id, enterprise_project_id)
