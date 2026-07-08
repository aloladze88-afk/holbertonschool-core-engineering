#!/usr/bin/env python3
"""Simple WebSocket broadcast server."""

import asyncio
import websockets
from websockets.exceptions import ConnectionClosed


connected_clients = set()


async def broadcast(message):
    """Send a message to all connected clients."""
    disconnected_clients = set()

    for client in connected_clients.copy():
        try:
            await client.send("B:" + message)
        except ConnectionClosed:
            disconnected_clients.add(client)

    for client in disconnected_clients:
        connected_clients.discard(client)


async def connection_handler(websocket):
    """Handle one connected client."""
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            await broadcast(message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the WebSocket broadcast server."""
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
