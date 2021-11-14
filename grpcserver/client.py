from __future__ import print_function

import logging

import grpc
import jump_pb2
import jump_pb2_grpc


def jump(request):
    logging.info(msg= "gRPC Client: Request received - %s" % request)
    
    # Obtaining Jump Step
    addr = request.jumps[0]
    logging.info(msg= "gRPC Client: Jump to %s" % addr)

    with grpc.insecure_channel(addr) as channel:
        try:
            stub = jump_pb2_grpc.JumpServiceStub(channel)
            response = stub.Jump(jump_pb2.JumpReq(message= request.message, count= request.count, jumps= request.jumps))
            return response
        except ValueError:
            logging.info("Error gRPC server negotiation: " % ValueError)
            return jump_pb2.Response(message= '/jump - Farewell from Python gRPC! | Jumps: ' + str(request.count), code= 400)
