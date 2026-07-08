#!/usr/bin/env python3
"""ASGI application with HTTP and WebSocket routes."""

from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.websockets import WebSocketDisconnect


async def homepage(request):
    """Return a simple HTML homepage."""
    return HTMLResponse("<h1>WebSocket App</h1>")


async def websocket_endpoint(websocket):
    """Accept WebSocket messages and echo them back."""
    await websocket.accept()

    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except WebSocketDisconnect:
        pass


app = Starlette(
    routes=[
        Route("/", homepage),
        WebSocketRoute("/ws", websocket_endpoint),
    ]
)
