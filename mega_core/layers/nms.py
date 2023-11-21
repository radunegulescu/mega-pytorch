# Copyright (c) Facebook, Inc. and its affiliates. All Rights Reserved.
# from ._utils import _C
from mega_core import _C

# from apex import amp

# Only valid with fp32 inputs - give AMP the hint
# nms = amp.float_function(_C.nms)

# Define the nms function directly without using Apex's amp
def nms(*args, **kwargs):
    # You might need to inspect the _C.nms function arguments and return values
    return _C.nms(*args, **kwargs)

# Assign the function pointer to the nms variable
nms = nms

# nms.__doc__ = """
# This function performs Non-maximum suppresion"""
