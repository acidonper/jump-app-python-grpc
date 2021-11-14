# Jump App Python gRPC Repository

This repository includes a microservice based on Python and gRPC that is a component develop for Jump App application. The idea of this microservice is implement an API based on gRPC that emulates the current features implemented in the original Jump App Golang microservice.

# Test Python Code

- Run the gRPC server

```$bash
export PYTHONPATH="./grpcserver"
python app.py
```

- Execute the test

```$bash
grpcurl -plaintext -d '{"count": 0, "message": "hola", "jumps": ["localhost:50052","localhost:50052"]}' localhost:50052 jump.JumpService/Jump
{
  "code": 200,
  "message": "/jump - Greetings from Python gRPC! | Jumps: 3"
}
```

# Author

Asier Cidon

asier.cidon@gmail.com

