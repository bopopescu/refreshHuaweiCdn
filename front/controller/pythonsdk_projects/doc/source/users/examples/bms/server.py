# Copyright 2017 OpenStack.org
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#      Huawei has modified this source file.
#            Copyright 2018 Huawei Technologies Co., Ltd.
#            Licensed under the Apache License, Version 2.0 (the "License"); you may not
#            use this file except in compliance with the License. You may obtain a copy of
#            the License at
#
#                http://www.apache.org/licenses/LICENSE-2.0
#
#            Unless required by applicable law or agreed to in writing, software
#            distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#            WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#            License for the specific language governing permissions and limitations under
#            the License.


def create_server_ext(conn):
    data = {
        "availability_zone": "az1.dc1",
        "name": "newserverkak",
        "imageRef": "ad134bba-dfca-4aa1-a307-26b51e4c608b",
        "root_volume": {
            "volumetype": "SATA"
        },
        "data_volumes": [
            {
                "volumetype": "SATA",
                "size": 50
            },
            {
                "volumetype": "SSD",
                "size": 10,
                "multiattach": "true",
                "hw:passthrough": "false"
            }
        ],
        "isAutoRename": "true",
        "flavorRef": "c1.xlarge",
        "personality": [
            {
                "path": "/etc/banner.txt",
                "contents": "ICAgICAgDQoiQmFjaA=="
            }
        ],
        "security_groups": [
            {
                "id": "53234334-9c3d-4344-b577-2cdd6c244707"
            }
        ],
        "vpcid": "5b2a6c9a-093d-4d56-8889-a7917e44229c",
        "nics": [
            {
                "subnet_id": "a8f622a7-0d10-470e-ae80-c8e0e8bc7d12"
            }
        ],
        "publicip": {
            "eip": {
                "iptype": "5_bgp",
                "bandwidth": {
                    "size": 1,
                    "sharetype": "PER"
                }
            }
        },
        "key_name": "KeyPair-1565",
        "count": 1,
        "metadata": {
            "ss": "ss"
        },
        "os:scheduler_hints": {
            "group": "cc10d0d1-d371-4f33-9452-fd5fbf14dc06"
        }
    }

    ff = conn.bms.create_server(**data)
    print ff
