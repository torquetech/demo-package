# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""TODO"""

import os

from torque import v1

from demo import interfaces
from demo import utils


class Link(v1.link.Link):
    """TODO"""

    _PARAMETERS = {
        "defaults": {},
        "schema": {}
    }

    _CONFIGURATION = {
        "defaults": {},
        "schema": {}
    }

    @classmethod
    def validate_parameters(cls, parameters: object) -> object:
        """TODO"""

        return utils.validate_schema("parameters",
                                     cls._PARAMETERS,
                                     parameters)

    @classmethod
    def validate_configuration(cls, configuration: object) -> object:
        """TODO"""

        return utils.validate_schema("configuration",
                                     cls._CONFIGURATION,
                                     configuration)

    def on_create(self):
        """TODO"""

        if not self.source.has_interface(interfaces.Service):
            raise RuntimeError(f"{self.source.name}: incompatible component")

        if not self.destination.has_interface(interfaces.NetworkLink):
            raise RuntimeError(f"{self.destination.name}: incompatible component")

    def on_remove(self):
        """TODO"""

    def on_build(self, deployment: v1.deployment.Deployment) -> bool:
        """TODO"""

        return True

    def on_apply(self, deployment: v1.deployment.Deployment) -> bool:
        """TODO"""

        with interfaces.Service(self.source) as src:
            link = src.link()

        with interfaces.NetworkLink(self.destination) as dst:
            dst.add(link)

        return True