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

"""
Managing cts

"""


def create_update_tracker(conn):
    tracker_dict = {
        "bucket_name": "defaultbucket",
        "file_prefix_name": "mytracker1"
    }

    t = conn.cts.create_tracker(**tracker_dict)
    print("newly created tracker is:")

    update_dict = {
        "bucket_name": "my_created_bucket",
        "file_prefix_name": "some_folder",
        "status": "disabled"
    }

    ut = conn.cts.update_tracker(t, **update_dict)
    print("tracker is updated as:")
    print(ut)


def get_delete_tracker(conn):
    # default name, we will get the 'system' tracker
    gett = conn.cts.get_tracker()
    print("system tracker is:")
    print(gett)

    print("traces for system tracker is")
    for tr in conn.cts.traces():
        print(tr)

    print("delete tracker:")
    conn.cts.delete_tracker()
