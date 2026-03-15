from __future__ import annotations
from typing import TYPE_CHECKING
from .model import InstagramUser, InstagramStoryResponse, Post, Highlight

if TYPE_CHECKING:
    from .. import SharedAPI


class Instagram:
    api: SharedAPI

    def __init__(self, api: SharedAPI) -> None:
        self.api = api

    async def post(self, url: str) -> Post:
        """Fetch an Instagram post."""

        data = await self.api.request("GET", "/instagram/post", params={"url": url, "reserved": "true"})
        return Post(**data)

    async def user(self, username: str, reserved: bool = False) -> InstagramUser:
        """Fetch an Instagram user's profile."""

        data = await self.api.request("GET", f"/instagram/{username}", params={"reserved": str(reserved).lower()})
        return InstagramUser(**data)

    async def story(self, username: str, reserved: bool = False) -> InstagramStoryResponse:
        """Fetch an Instagram user's story."""

        data = await self.api.request("GET", f"/instagram/{username}/story", params={"reserved": str(reserved).lower()})
        return InstagramStoryResponse(**data)

    async def highlight(self, highlight_id: str, reserved: bool = False) -> Highlight:
        """Fetch an Instagram highlight."""

        data = await self.api.request("GET", f"/instagram/highlight/{highlight_id}", params={"reserved": str(reserved).lower()})
        return Highlight(**data)
