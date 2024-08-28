# gRPC Messenger

gRPC messaging system between microservices.

## Developer

### RPC generate

```bash
rm -r protos/__pycache__
python3 -m grpc_tools.protoc -I. --python_out=generated/ --grpc_python_out=generated/ protos/*
```
