"""
class Computation:
    def initialize(self, ctx):
        pass

    def process_record(self, ctx, record):
        pass

    def process_timer(self, ctx, time):
        pass

    def metadata(self):
        pass

class Metadata:
    def __init__(self, name=None, istreams=None, ostreams=None):
        self.name = name
        self.istreams = istreams
        self.ostreams = ostreams

class ComputationContext:
    def produce_record(self, stream, key, value):
        pass

    def set_timer(self, time):
        pass

    def set_state(self, key, value):
        pass

    def get_state(self, key):
        pass

"""
import rbonut
import logging
import sys
import time

def milliseconds_now():
    return int(round(time.time() * 1000))

class TestConsumer:
    def initialize(self, ctx):
        logging.info("computation initialized!!")
        ctx.set_timer(milliseconds_now() + 1000)
        logging.info("Set the timer callback for 1 second")

    def process_record(self, ctx, record):
        logging.info("Got something! do something here!")

    def process_timer(self, ctx, timer):
        logging.info("W00t - ending the computation")

    def metadata(self):
        return rbonut.Metadata(
                name='example-globally-unique-name-py',
                istreams=['words'],
                ostreams=[]
                )

logging.basicConfig(filename='computation.log',level=logging.DEBUG)
rbonut.serve_computation(TestConsumer())
