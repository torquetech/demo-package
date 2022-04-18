# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""TODO"""

from collections import namedtuple

from torque import v1


class Provider(v1.interface.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    KeyValue = namedtuple("KeyValue", [
        "key",
        "value"
    ])

    NetworkLink = namedtuple("NetworkLink", [
        "name",
        "object"
    ])

    VolumeLink = namedtuple("VolumeLink", [
        "name",
        "mount_path",
        "object"
    ])

    SecretLink = namedtuple("SecretLink", [
        "name",
        "key",
        "object"
    ])

    def push_image(image: str):
        """TODO"""

    def create_secret(name: str,
                      entries: [KeyValue]) -> v1.interface.Future[object]:
        """TODO"""

    def create_service(name: str,
                       tcp_ports: [int],
                       udp_ports: [int]) -> v1.interface.Future[object]:
        """TODO"""

    def create_deployment(name: str,
                          image: str,
                          cmd: [str],
                          args: [str],
                          cwd: str,
                          env: [KeyValue],
                          network_links: [NetworkLink],
                          volume_links: [VolumeLink],
                          secret_links: [SecretLink],
                          replicas: int):
        """TODO"""


class Service(v1.interface.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def link() -> v1.interface.Future[object]:
        """TODO"""


class PostgresService(Service):
    # pylint: disable=E0211,E0213

    """TODO"""

    def admin() -> v1.interface.Future[object]:
        """TODO"""


class NetworkLink(v1.interface.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def add(name: str, link: v1.interface.Future[object]):
        """TODO"""


class Volume(v1.interface.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def link() -> v1.interface.Future[object]:
        """TODO"""


class VolumeLink(v1.interface.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def add(name: str, mount_path: str, link: v1.interface.Future[object]):
        """TODO"""


class SecretLink(v1.interface.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def add(name: str, key: str, link: v1.interface.Future[object]):
        """TODO"""


class Environment(v1.interface.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def add(name: str, value: str):
        """TODO"""


class PythonModules(v1.interface.Interface):
    # pylint: disable=E0211,E0213

    """TODO"""

    def path() -> str:
        """TODO"""

    def add_requirements(requirements: [str]):
        """TODO"""
