"""Publisher client.

This would be in a service to send messages to broker service.
"""

import logging
import os
from dotenv import load_dotenv
import grpc

from proto_files import pubsub_pb2, pubsub_pb2_grpc

logging.basicConfig(level=logging.DEBUG)


load_dotenv()


def main() -> None:
    with grpc.insecure_channel(os.environ["PUBSUB_SERVICE_URI"]) as channel:
        stub: pubsub_pb2_grpc.PubsubServiceStub = pubsub_pb2_grpc.PubsubServiceStub(
            channel=channel
        )

        response_stream = stub.Publish(
            pubsub_pb2.PublishRequest(
                topic="example_topic",
                message="hello this is from the publisher client.",
            )
        )

        logging.debug("Publisher stub stream response %s", response_stream)
        logging.debug(response_stream.message_id)
        logging.debug(response_stream.status_message)


if __name__ == "__main__":
    main()
