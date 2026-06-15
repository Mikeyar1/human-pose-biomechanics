"""
sam3db — SAM-3D Body biomechanics analysis package.
"""
from .pipeline import load_model, run_inference
from .joints import JOINT, BONES, ANGLE_TRIPLES, RELATIVE_ROT_PAIRS
from .visualization import add_skeleton, add_joint_angles, add_relative_rotation_triads
