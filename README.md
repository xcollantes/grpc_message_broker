# gRPC Messenger

gRPC messaging system between microservices.

## Developer

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
