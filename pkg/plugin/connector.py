# For connect to plugin runtime.
from __future__ import annotations

import asyncio
import os
import sys

from ..core import app
from . import handler
from ..utils import platform
from langbot_plugin.runtime.io.controllers.stdio import client as stdio_client_controller
from langbot_plugin.runtime.io.connections import stdio as stdio_connection
from langbot_plugin.runtime.io.controllers.ws import client as ws_client_controller


class PluginRuntimeConnector:
    """Plugin runtime connector"""

    ap: app.Application

    handler: handler.RuntimeConnectionHandler

    handler_task: asyncio.Task

    stdio_client_controller: stdio_client_controller.StdioClientController

    def __init__(self, ap: app.Application):
        self.ap = ap

    async def initialize(self):
        async def new_connection_callback(connection: stdio_connection.StdioConnection):
            self.ap.logger.info('Connected to plugin runtime.')
            self.handler = handler.RuntimeConnectionHandler(connection)
            self.handler_task = asyncio.create_task(self.handler.run())

        if platform.get_platform() == 'docker':  # use websocket
            ws_url = self.ap.instance_config.data['plugin']['runtime_ws_url']
            ctrl = ws_client_controller.WebSocketClientController(
                ws_url=ws_url,
            )
            await ctrl.run(new_connection_callback)
        else:  # stdio
            # cmd: lbp rt -s
            python_path = sys.executable
            env = os.environ.copy()
            ctrl = stdio_client_controller.StdioClientController(
                command=python_path,
                args=['-m', 'langbot_plugin.cli.__init__', 'rt', '-s'],
                env=env,
            )
            await ctrl.run(new_connection_callback)

    async def run(self):
        pass

    async def initialize_plugins(self):
        pass
