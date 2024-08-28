# gRPC Messenger

gRPC messaging system between microservices.

_Why gRPC?_

- gRPC is ~6x faster than REST API ([gRPC vs REST speed
  comparison](https://blog.shiftasia.com/grpc-vs-rest-speed-comparation))
- gRPC serializes using Protocol Buffers which send data as binary; REST usually
  uses JSON or XML which use text based data.
- gRPC supports bidirectional streaming; REST uses request-response.
- gRPC communicates using HTTP 2 which is faster reduces network delay through
  the use of multiplexing.

[What is gRPC](https://grpc.io/docs/what-is-grpc/introduction)

## Getting started

- Messages are not saved
- Topics are created by either publishing or subscribing
- Subscribers will not receive messages sent to a topic prior to subscribing

### broker_service

Service broker which receives messages from publishers and distributes messages
to subscribers.

### publisher_service

Example for placing code in a service pushing messages to subscribers.

### subscribe_service

Example for listening for messages.

## Contributing to this repo

### Generate protobuf files

Run this when editing the `.proto` files.

```bash
# Delete __pycache__ directory if it exists.
rm -r protos/__pycache__

# Delete existing protobuf files if they exist.
rm -r protos/*_pb2*

# Generate new protobuf files.
python3 -m grpc_tools.protoc -I. --python_out=. --grpc_python_out=. protos/*
```
