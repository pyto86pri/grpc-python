"""
Need to add this because `xxx_pb2_grpc.py` fail to import `xxx_pb2.py`
unless `xxx_pb2_grpc.py` and `xxx_pb2.py` are in the root directory.
ref. https://github.com/protocolbuffers/protobuf/issues/1491#issuecomment-547504972
"""
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent))
