# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""TODO"""

from abc import abstractmethod

from torque import v1

from demo import types


class Service(v1.component.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def link() -> v1.utils.Future[object]:
        """TODO"""


class PostgresService(Service):
    # pylint: disable=E0211,E0213

    """TODO"""

    def admin() -> v1.utils.Future[object]:
        """TODO"""

    def pg_data() -> str:
        """TODO"""


class NetworkLink(v1.component.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def add(name: str, link: v1.utils.Future[object]):
        """TODO"""


class Volume(v1.component.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def link() -> v1.utils.Future[object]:
        """TODO"""


class VolumeLink(v1.component.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def add(name: str, mount_path: str, link: v1.utils.Future[object]):
        """TODO"""


class SecretLink(v1.component.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def add(name: str, key: str, link: v1.utils.Future[object]):
        """TODO"""


class Environment(v1.component.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def add(name: str, value: str):
        """TODO"""


class PythonModules(v1.component.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def path() -> str:
        """TODO"""

    def add_requirements(requirements: [str]):
        """TODO"""


class Images(v1.provider.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    @abstractmethod
    def push(self, image: str):
        """TODO"""


class Secrets(v1.provider.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    @abstractmethod
    def create(self, name: str, entries: [types.KeyValue]) -> v1.utils.Future[object]:
        """TODO"""


class Services(v1.provider.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    @abstractmethod
    def create(self, name: str, type: str, port: int, target_port: int) -> v1.utils.Future[object]:
        """TODO"""


class Deployments(v1.provider.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    @abstractmethod
    def create(self,
               name: str,
               image: str,
               cmd: [str],
               args: [str],
               cwd: str,
               env: [types.KeyValue],
               network_links: [types.NetworkLink],
               volume_links: [types.VolumeLink],
               secret_links: [types.SecretLink],
               replicas: int):
        """TODO"""


class ConfigMaps(v1.provider.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    @abstractmethod
    def create(self, name: str, configuration: object) -> v1.utils.Future[object]:
        """TODO"""


class EBSVolumes(v1.provider.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    @abstractmethod
    def create(self, name: str, volume_id: str) -> v1.utils.Future[object]:
        """TODO"""


class EBSProvider(v1.provider.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    @abstractmethod
    def create(self, name: str, size: int) -> v1.utils.Future[object]:
        """TODO"""
