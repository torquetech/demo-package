# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at https://mozilla.org/MPL/2.0/.

"""TODO"""

import os
import jinja2

from torque import v1

from demo import components
from demo import network
from demo import utils


class Link(network.Link):
    """TODO"""

    # pylint: disable=W0212
    _CONFIGURATION = v1.utils.merge_dicts(network.Link._CONFIGURATION, {
        "defaults": {
            "database": "postgres"
        },
        "schema": {
            "database": str
        }
    }, allow_overwrites=False)

    @classmethod
    def on_requirements(cls) -> dict:
        """TODO"""

        return super().on_requirements() | {
            "pg": {
                "interface": components.PostgresService,
                "bind_to": "source",
                "required": True
            },
            "mod": {
                "interface": components.PythonModules,
                "bind_to": "destination",
                "required": True
            },
            "sec": {
                "interface": components.SecretLink,
                "bind_to": "destination",
                "required": True
            },
            "env": {
                "interface": components.Environment,
                "bind_to": "destination",
                "required": True
            }
        }

    def on_create(self):
        """TODO"""

        super().on_create()

        template_path = f"{utils.module_path()}/templates/psycopg.py.template"
        template = jinja2.Template(utils.load_file(template_path))

        target_path = f"{self.binds.mod.path()}/{self.source}.py"

        if os.path.exists(v1.utils.resolve_path(target_path)):
            raise RuntimeError(f"{target_path}: file already exists")

        with open(v1.utils.resolve_path(target_path), "w", encoding="utf8") as file:
            file.write(template.render(COMPONENT=self.source.upper()))
            file.write("\n")

        self.binds.mod.add_requirements(["psycopg"])

    def on_apply(self, deployment: v1.deployment.Deployment):
        """TODO"""

        super().on_apply(deployment)

        source = self.source.upper()
        secret = self.binds.pg.admin()

        self.binds.env.add(f"{source}_PSYCOPG_DB", self.configuration["database"])
        self.binds.sec.add(f"{source}_PSYCOPG_USER", "user", secret)
        self.binds.sec.add(f"{source}_PSYCOPG_PASSWORD", "password", secret)
