#!/usr/bin/env python3
"""WebSocket server that validates incoming messages."""

import asyncio
import websockets


async def validation_handler(websocket):
    """Receive messages, validate them, and send a response."""
    async for message in websocket:
        clean_message = message.strip()

        if clean_message == "":
            await websocket.send("ERR:EMPTY")
        else:
            await websocket.send(f"OK:{clean_message}")


async def main():
    """Start the validation WebSocket server."""
    async with websockets.serve(validation_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
