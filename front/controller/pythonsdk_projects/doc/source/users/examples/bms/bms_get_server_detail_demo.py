from openstack import connection
import os
import time

#os.environ.setdefault(
#    'OS_BMS_ENDPOINT_OVERRIDE',
#    'https://bms.cn-north-1.myhuaweicloud.com/v1/%(project_id)s')



username = "test_user"
password = "test_password"
projectId = "000efdc5f9064584b718b181df137bd7"
userDomainId = "49d5b5a8dbc04efa806afcc323d35880"
auth_url = "https://iam.cn-north-1.myhuaweicloud.com/v3"

conn = connection.Connection(auth_url=auth_url,
                             user_domain_id=userDomainId,
                             project_id=projectId,
                             username=username,
                             password=password)

def get_bare_metal_server(server_id):
    server = conn.compute.get_server(server_id)
    print server

server_id = "3ad57ed6-e405-40bf-9f1b-f78ee03dab2e"
get_bare_metal_server(server_id)