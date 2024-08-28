"""Receives messages from publishers and forwards them to subscribers."""

import logging
import queue
import threading
from typing import Iterable
from uuid import uuid4

import grpc
from google.protobuf.timestamp_pb2 import Timestamp

from protos import pubsub_pb2, pubsub_pb2_grpc

logging.basicConfig(level=logging.DEBUG)


class BrokerService(pubsub_pb2_grpc.PubsubServiceServicer):
    def __init__(self) -> None:
        # Topic messages.
        self.subscribers: dict[str, list[queue.Queue]] = {}

    def Publish(
        self, request: pubsub_pb2.PublishRequest, context: grpc.ServicerContext
    ) -> pubsub_pb2.PublishResponse:
        logging.debug("====== PUBLISH ======")
        topic = request.topic
        message = request.message

        message_id: str = str(uuid4())
        message: pubsub_pb2.Message = pubsub_pb2.Message(
            message_id=message_id,
            topic=topic,
            message=request.message,
            timestamp=Timestamp().GetCurrentTime(),
        )

        logging.debug(
            "Publishing message: %s to subscribers: %s",
            message,
            self.subscribers,
        )

        if topic not in self.subscribers:
            logging.info("Topic %s not found. Creating new topic: %s", topic, topic)
            self.subscribers[topic] = []

        for subscriber_queue in self.subscribers[topic]:
            logging.debug("Sending to %s", subscriber_queue)
            subscriber_queue.put(message)

        return pubsub_pb2.PublishResponse(
            message_id=message_id, status_message=f"Published {topic} {message}"
        )

    def Subscribe(
        self, request: pubsub_pb2.SubscribeRequest, context: grpc.ServicerContext
    ) -> Iterable[pubsub_pb2.Message]:
        logging.debug("====== SUBSCRIBE ======")
        topic = request.topic

        subscriber_queue: queue.Queue = queue.Queue()

        if topic not in self.subscribers:
            logging.info("Topic %s not found. Creating new topic: %s", topic, topic)
            self.subscribers[topic] = []

        logging.debug("Subscribing to topic: %s", topic)
        self.subscribers[topic].append(subscriber_queue)

        logging.debug("Topics: %s", self.subscribers)

        try:
            while True:
                message = subscriber_queue.get()
                logging.debug("Sending message: %s", message)
                yield message

        except grpc.RpcError as re:
            logging.error("RPC error: %s", re)
        except KeyboardInterrupt:
            logging.info("Stopping subscription.")
        finally:
            logging.info("Popping subscriber.")
            self.subscribers[topic].remove(subscriber_queue)
