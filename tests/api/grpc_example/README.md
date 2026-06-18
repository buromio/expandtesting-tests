# gRPC Simple Autotest Example

This example demonstrates a simple gRPC service with Python and grpcio, including an autotest.

## Files:
- `greeter.proto` - Protocol Buffers definition
- `server.py` - gRPC server implementation
- `client.py` - gRPC client
- `test_greeter.py` - Autotest using pytest
- `generate.py` - Script to generate Python stubs
- `requirements.txt` - Dependencies

## Setup:

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Generate Python stubs from proto file:
   ```bash
   python generate.py
   ```

3. Start the server:
   ```bash
   python server.py
   ```

4. Run the client (in another terminal):
   ```bash
   python client.py
   ```

5. Run autotests:
   ```bash
   pytest test_greeter.py -v
   ```

## Autotest Details:

The test file `test_greeter.py` uses pytest fixtures to:
- Start a gRPC server in a separate thread
- Create a channel and stub
- Test the `SayHello` RPC with different inputs
- Assert expected responses

## Expected Output:

When running tests:
```
test_greeter.py::test_say_hello PASSED
test_greeter.py::test_say_hello_empty_name PASSED
```