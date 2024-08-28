# gRPC Messenger

gRPC messaging system between microservices.

## Getting started

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
