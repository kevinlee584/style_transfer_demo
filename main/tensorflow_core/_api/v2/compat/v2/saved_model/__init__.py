# This file is MACHINE GENERATED! Do not edit.
# Generated by: tensorflow/python/tools/api/generator/create_python_api.py script.
"""Public API for tf.saved_model namespace.
"""

from __future__ import print_function as _print_function

import sys as _sys

from tensorflow.python.saved_model.constants import ASSETS_DIRECTORY
from tensorflow.python.saved_model.constants import ASSETS_KEY
from tensorflow.python.saved_model.constants import SAVED_MODEL_FILENAME_PB
from tensorflow.python.saved_model.constants import SAVED_MODEL_FILENAME_PBTXT
from tensorflow.python.saved_model.constants import SAVED_MODEL_SCHEMA_VERSION
from tensorflow.python.saved_model.constants import VARIABLES_DIRECTORY
from tensorflow.python.saved_model.constants import VARIABLES_FILENAME
from tensorflow.python.saved_model.load import load
from tensorflow.python.saved_model.loader_impl import contains_saved_model
from tensorflow.python.saved_model.save import save
from tensorflow.python.saved_model.save_options import SaveOptions
from tensorflow.python.saved_model.signature_constants import CLASSIFY_INPUTS
from tensorflow.python.saved_model.signature_constants import CLASSIFY_METHOD_NAME
from tensorflow.python.saved_model.signature_constants import CLASSIFY_OUTPUT_CLASSES
from tensorflow.python.saved_model.signature_constants import CLASSIFY_OUTPUT_SCORES
from tensorflow.python.saved_model.signature_constants import DEFAULT_SERVING_SIGNATURE_DEF_KEY
from tensorflow.python.saved_model.signature_constants import PREDICT_INPUTS
from tensorflow.python.saved_model.signature_constants import PREDICT_METHOD_NAME
from tensorflow.python.saved_model.signature_constants import PREDICT_OUTPUTS
from tensorflow.python.saved_model.signature_constants import REGRESS_INPUTS
from tensorflow.python.saved_model.signature_constants import REGRESS_METHOD_NAME
from tensorflow.python.saved_model.signature_constants import REGRESS_OUTPUTS
from tensorflow.python.saved_model.tag_constants import GPU
from tensorflow.python.saved_model.tag_constants import SERVING
from tensorflow.python.saved_model.tag_constants import TPU
from tensorflow.python.saved_model.tag_constants import TRAINING
from tensorflow.python.training.tracking.tracking import Asset

del _print_function