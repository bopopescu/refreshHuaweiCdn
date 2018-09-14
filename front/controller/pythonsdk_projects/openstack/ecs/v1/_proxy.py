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
from openstack import proxy2
from openstack.ecs.v1 import server as _server
from openstack.ecs.v1 import server_ext as _server_ext


class Proxy(proxy2.BaseProxy):
    def create_server(self, **data):
        """
        post method to create ecs server
        :param data: data to create ecs server see more info from support website
        :return: :class:`~openstack.ecs.v1.server.Servers`
        """
        return self._create(_server.Servers, **data)

    def resize_server(self, server_id, **data):
        """
        post method to modify ecs server size
        :param server_id: ecs server id
        :param data: data to create ecs server see more info from support website
        :return: class:`~openstack.ecs.v1._server.ResizeServer`
        """
        return self._create(_server.ResizeServer, server_id=server_id, **data)

    def create_server_ext(self, **data):
        """
        post method to create ecs server
        :param data: data to create ecs server see more info from support website
        :return: :class:`~openstack.ecs.v1.server_ext.Servers`
        """
        return self._create(_server_ext.Servers, **data)

    def resize_server_ext(self, server_id, **data):
        """
        post method to modify ecs server size
        :param server_id: ecs server id
        :param data: data to create ecs server see more info from support website
        :return: class:`~openstack.ecs.v1.server_ext.ResizeServer`
        """
        return self._create(_server_ext.ResizeServer, server_id=server_id, **data)

    def start_server(self, **data):
        """
        post method to do server action ,such as batch start stop and restart server
        :param data: data to do action see more info from support website
        :return: :class:`~openstack.ecs.v1.server.ServerAction`
        """
        return self._create(_server.ServerAction, **data)

    def stop_server(self, **data):
        """
        post method to do server action ,such as batch start stop and restart server
        :param data: data to do action see more info from support website
        :return: :class:`~openstack.ecs.v1.server.ServerAction`
        """
        return self._create(_server.ServerAction, **data)

    def reboot_server(self, **data):
        """
        post method to do server action ,such as batch start stop and restart server
        :param data: data to do action see more info from support website
        :return: :class:`~openstack.ecs.v1.server.ServerAction`
        """
        return self._create(_server.ServerAction, **data)

    def delete_server(self, **data):
        """
        post method to batch delete server
        :param data: data to do delete server such as server id list
        :return: :class:`~openstack.ecs.v1.server.ServerAction`
        """
        return self._create(_server.DeleteServer, **data)
