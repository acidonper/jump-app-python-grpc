from concurrent import futures
import logging
from six import print_
from grpc_reflection.v1alpha import reflection

import grpc
import client
import jump_pb2
import jump_pb2_grpc

class Jump(jump_pb2_grpc.JumpServiceServicer):

    def Jump(self, request, context):
        logging.info(msg= "gRPC Server: Request received - %s" % request)

        # Add a new count
        request.count = request.count + 1
        logging.info("gRPC Server: Steps count %d" % request.count)

        # Evaluate jumps to send response or perform a jump 
        if len(request.jumps) == 0 or request.jumps[0] == "":
            logging.info("gRPC Server: Send response 200")
            return jump_pb2.Response(message= '/jump - Greetings from Python gRPC! | Jumps: ' + str(request.count), code= 200)
        else:
            try:
                responseJump = client.jump(request)
            except ValueError:
                logging.info("Error local calling grpcclient from grpcserver -" % ValueError)
                return jump_pb2.Response(message= '/jump - Farewell from Python gRPC! Error Jumping | Jumps: ' + str(request.count), code= 500)
            logging.info("gRPC Server: Response received %s", responseJump)
            return responseJump


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    jump_pb2_grpc.add_JumpServiceServicer_to_server(Jump(), server)

    # Activate Reflection
    SERVICE_NAMES = (
        jump_pb2.DESCRIPTOR.services_by_name['JumpService'].full_name,
        reflection.SERVICE_NAME,
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.add_insecure_port('[::]:50052')
    server.start()
    logging.info(msg= "gRPC Server: listening port 50052")
    server.wait_for_termination()

def main():
    logging.basicConfig(level= logging.INFO)
    serve()

if __name__ == '__main__':
    main()