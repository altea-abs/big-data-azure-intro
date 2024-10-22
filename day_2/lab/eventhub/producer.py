"""
pip install azure-eventhub
pip install aiohttp

https://learn.microsoft.com/en-us/azure/event-hubs/event-hubs-python-get-started-send?tabs=passwordless%2Croles-azure-portal
"""

import asyncio
import json
from datetime import datetime

import numpy as np

from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
from azure.identity.aio import DefaultAzureCredential

EVENT_HUB_FULLY_QUALIFIED_NAMESPACE = "test-eh-course.servicebus.windows.net"
EVENT_HUB_NAME = "test"

credential = DefaultAzureCredential()

def gen_record():
    return json.dumps({
        'id': '1',
        'timestamp': datetime.now().strftime("%Y%m%d%H%M%S"),
        'value': np.random.normal(20, 5, 1).item()
    })

async def run():
    # Create a producer client to send messages to the event hub.
    # Specify a credential that has correct role assigned to access
    # event hubs namespace and the event hub name.
    producer = EventHubProducerClient(
        fully_qualified_namespace=EVENT_HUB_FULLY_QUALIFIED_NAMESPACE,
        eventhub_name=EVENT_HUB_NAME,
        credential=credential,
    )
    async with producer:
        # Create a batch.
        event_data_batch = await producer.create_batch()

        # Add events to the batch.
        event_data_batch.add(EventData(gen_record()))
        event_data_batch.add(EventData(gen_record()))
        event_data_batch.add(EventData(gen_record()))

        # Send the batch of events to the event hub.
        await producer.send_batch(event_data_batch)

        # Close credential when no longer needed.
        await credential.close()

asyncio.run(run())