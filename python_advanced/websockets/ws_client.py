#!/usr/bin/env python3
"""Minimal WebSocket client."""

import asyncio
import os
import sys

import websockets


async def connect_and_send(uri, message):
    """Connect to a WebSocket server, send a message, and return the reply."""
    async with websockets.connect(uri) as websocket:
        await websocket.send(message)
        return await websocket.recv()


if __name__ == "__main__":
    ws_uri = os.getenv("WS_URI", "ws://localhost:8765")
    ws_message = os.getenv("WS_MESSAGE", "demo")

    if len(sys.argv) > 1:
        ws_message = sys.argv[1]

    sys.stdout.write(asyncio.run(connect_and_send(ws_uri, ws_message)))
