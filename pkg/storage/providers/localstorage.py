from __future__ import annotations

import os
import aiofiles

from ...core import app

from .. import provider


LOCAL_STORAGE_PATH = os.path.join('data', 'storage')


class LocalStorageProvider(provider.StorageProvider):
    def __init__(self, ap: app.Application):
        super().__init__(ap)
        if not os.path.exists(LOCAL_STORAGE_PATH):
            os.makedirs(LOCAL_STORAGE_PATH)

    async def save(
        self,
        key: str,
        value: bytes,
    ):
        async with aiofiles.open(os.path.join(LOCAL_STORAGE_PATH, f'{key}'), 'wb') as f:
            await f.write(value)

    async def load(
        self,
        key: str,
    ) -> bytes:
        async with aiofiles.open(os.path.join(LOCAL_STORAGE_PATH, f'{key}'), 'rb') as f:
            return await f.read()

    async def exists(
        self,
        key: str,
    ) -> bool:
        return os.path.exists(os.path.join(LOCAL_STORAGE_PATH, f'{key}'))

    async def delete(
        self,
        key: str,
    ):
        os.remove(os.path.join(LOCAL_STORAGE_PATH, f'{key}'))
