#!/usr/bin/python3
"""Simple WebSocket echo server."""

import asyncio
import websockets


async def connection_handler(websocket):
    """Receive messages from one client and echo them back."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the WebSocket server."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
