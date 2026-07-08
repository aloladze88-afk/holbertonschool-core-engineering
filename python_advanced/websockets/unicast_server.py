#!/usr/bin/env python3
"""WebSocket unicast server."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def connection_handler(websocket):
    """Handle one client and reply only to that client."""
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await websocket.send("U:" + message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket server."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
