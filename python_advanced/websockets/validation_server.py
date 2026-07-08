#!/usr/bin/env python3
"""WebSocket server that validates incoming messages."""

import asyncio

import websockets
from websockets.exceptions import ConnectionClosed


async def connection_handler(websocket):
    """Receive messages, validate them, and send a response."""
    try:
        async for message in websocket:
            clean_message = message.strip()

            if clean_message == "":
                await websocket.send("ERR:EMPTY")
            else:
                await websocket.send("OK:" + clean_message)
    except ConnectionClosed:
        pass


async def main():
    """Start the validation WebSocket server."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
