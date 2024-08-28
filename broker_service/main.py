"""Broker service server."""

import logging
import os
from concurrent import futures

import grpc
from dotenv import load_dotenv

from broker_service.broker_service import BrokerService
from protos import pubsub_pb2_grpc

load_dotenv()


logging.basicConfig(level=logging.DEBUG)


def main() -> None:
    max_workers_env: str = os.environ.get("MAX_WORKERS", None)
    max_workers: int = int(max_workers_env) if max_workers_env else None

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=max_workers))
    pubsub_pb2_grpc.add_PubsubServiceServicer_to_server(BrokerService(), server)
    server.add_insecure_port(f"[::]:{os.environ['PUBSUB_SERVICE_PORT']}")
    logging.info(
        f"Starting broker service on port: {os.environ['PUBSUB_SERVICE_PORT']}"
    )
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    main()
