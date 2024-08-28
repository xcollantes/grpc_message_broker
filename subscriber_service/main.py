"""Subscriber example.

This would be in a service to receive messages from broker service.
Service will stay open since the proto specifies a `stream` response.
"""

import logging
import os
from typing import Any

import grpc
from dotenv import load_dotenv

from proto_files import pubsub_pb2, pubsub_pb2_grpc

load_dotenv()

logging.basicConfig(level=logging.DEBUG)


def main() -> None:
    with grpc.insecure_channel(os.environ["PUBSUB_SERVICE_URI"]) as channel:
        stub: pubsub_pb2_grpc.PubsubServiceStub = pubsub_pb2_grpc.PubsubServiceStub(
            channel=channel
        )

        response_stream: Any = stub.Subscribe(
            pubsub_pb2.SubscribeRequest(topic="example_topic")
        )

        try:
            for msg in response_stream:
                logging.info("MSG: %s", msg)
        except grpc.RpcError as e:
            logging.error("RPC error: %s", e)
        except KeyboardInterrupt:
            logging.info("Stopping subscription.")
        finally:
            logging.info("Popping subscriber.")


if __name__ == "__main__":
    main()
