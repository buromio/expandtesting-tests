import grpc
import pytest
import greeter_pb2
import greeter_pb2_grpc
from server import Greeter
from concurrent import futures


@pytest.fixture(scope="module")
def grpc_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    greeter_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    import time
    time.sleep(0.5)  # Wait for server to start
    yield server
    server.stop(0)


@pytest.fixture(scope="module")
def grpc_channel(grpc_server):
    channel = grpc.insecure_channel("localhost:50051")
    yield channel
    channel.close()


@pytest.fixture(scope="module")
def grpc_stub(grpc_channel):
    return greeter_pb2_grpc.GreeterStub(grpc_channel)


def test_say_hello(grpc_stub):
    response = grpc_stub.SayHello(greeter_pb2.HelloRequest(name="Test"))
    assert response.message == "Hello, Test!"


def test_say_hello_empty_name(grpc_stub):
    response = grpc_stub.SayHello(greeter_pb2.HelloRequest(name=""))
    assert response.message == "Hello, !"