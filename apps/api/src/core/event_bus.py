import asyncio
from typing import Dict, List, Callable
from dataclasses import dataclass

@dataclass
class PAIEvent:
    layer: str
    agent: str
    event_type: str
    payload: dict

class EventBus:
    """Layer 1: Kernel - Event-driven message bus for inter-agent communication"""
    def __init__(self):
        self._subscribers: Dict[str, List[Callable]] = {}
        self._queue = asyncio.Queue()
        self._running = False

    def subscribe(self, event_type: str, handler: Callable):
        if event_type not in self._subscribers:
            self._subscribers[event_type] = []
        self._subscribers[event_type].append(handler)

    async def publish(self, event: PAIEvent):
        await self._queue.put(event)

    async def start(self):
        self._running = True
        while self._running:
            event = await self._queue.get()
            handlers = self._subscribers.get(event.event_type, [])
            for handler in handlers:
                asyncio.create_task(handler(event))

    async def stop(self):
        self._running = False
