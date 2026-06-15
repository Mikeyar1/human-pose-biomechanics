"""
joints.py — SAM-3D Body joint registry and biomechanics constants.

All joint names, indices, skeleton bones, angle triples, and relative
rotation pairs live here as module-level constants. Notebooks and
analysis scripts import from here rather than re-defining inline.

Usage:
    from sam3db.joints import JOINT, BONES, ANGLE_TRIPLES, RELATIVE_ROT_PAIRS
"""

# ──────────────────────────────────────────────────────────────
# Joint name → index lookup
# Full 127-joint hierarchy from SAM-3D Body (SMPL-X based)
# ──────────────────────────────────────────────────────────────

JOINT_NAMES: list[str] = [
    'body_world', 'root', 'l_upleg', 'l_lowleg', 'l_foot',
    'l_talocrural', 'l_subtalar', 'l_transversetarsal', 'l_ball',
    'l_lowleg_twist1_proc', 'l_lowleg_twist2_proc', 'l_lowleg_twist3_proc',
    'l_lowleg_twist4_proc', 'l_upleg_twist0_proc', 'l_upleg_twist1_proc',
    'l_upleg_twist2_proc', 'l_upleg_twist3_proc', 'l_upleg_twist4_proc',
    'r_upleg', 'r_lowleg', 'r_foot', 'r_talocrural', 'r_subtalar',
    'r_transversetarsal', 'r_ball', 'r_lowleg_twist1_proc',
    'r_lowleg_twist2_proc', 'r_lowleg_twist3_proc', 'r_lowleg_twist4_proc',
    'r_upleg_twist0_proc', 'r_upleg_twist1_proc', 'r_upleg_twist2_proc',
    'r_upleg_twist3_proc', 'r_upleg_twist4_proc', 'c_spine0', 'c_spine1',
    'c_spine2', 'c_spine3', 'r_clavicle', 'r_uparm', 'r_lowarm',
    'r_wrist_twist', 'r_wrist', 'r_pinky0', 'r_pinky1', 'r_pinky2',
    'r_pinky3', 'r_pinky_null', 'r_ring1', 'r_ring2', 'r_ring3',
    'r_ring_null', 'r_middle1', 'r_middle2', 'r_middle3', 'r_middle_null',
    'r_index1', 'r_index2', 'r_index3', 'r_index_null', 'r_thumb0',
    'r_thumb1', 'r_thumb2', 'r_thumb3', 'r_thumb_null',
    'r_lowarm_twist1_proc', 'r_lowarm_twist2_proc', 'r_lowarm_twist3_proc',
    'r_lowarm_twist4_proc', 'r_uparm_twist0_proc', 'r_uparm_twist1_proc',
    'r_uparm_twist2_proc', 'r_uparm_twist3_proc', 'r_uparm_twist4_proc',
    'l_clavicle', 'l_uparm', 'l_lowarm', 'l_wrist_twist', 'l_wrist',
    'l_pinky0', 'l_pinky1', 'l_pinky2', 'l_pinky3', 'l_pinky_null',
    'l_ring1', 'l_ring2', 'l_ring3', 'l_ring_null', 'l_middle1',
    'l_middle2', 'l_middle3', 'l_middle_null', 'l_index1', 'l_index2',
    'l_index3', 'l_index_null', 'l_thumb0', 'l_thumb1', 'l_thumb2',
    'l_thumb3', 'l_thumb_null', 'l_lowarm_twist1_proc',
    'l_lowarm_twist2_proc', 'l_lowarm_twist3_proc', 'l_lowarm_twist4_proc',
    'l_uparm_twist0_proc', 'l_uparm_twist1_proc', 'l_uparm_twist2_proc',
    'l_uparm_twist3_proc', 'l_uparm_twist4_proc', 'c_neck',
    'c_neck_twist1_proc', 'c_neck_twist0_proc', 'c_head', 'c_jaw',
    'c_teeth', 'c_jaw_null', 'c_tongue0', 'c_tongue1', 'c_tongue2',
    'c_tongue3', 'c_tongue4', 'r_eye', 'r_eye_null', 'l_eye',
    'l_eye_null', 'c_head_null',
]

# dict: joint_name → index  (e.g. JOINT['c_head'] == 113)
JOINT: dict[str, int] = {name: i for i, name in enumerate(JOINT_NAMES)}

# ──────────────────────────────────────────────────────────────
# Skeleton bones — (parent_idx, child_idx) pairs for rendering
# ──────────────────────────────────────────────────────────────

BONES: list[tuple[int, int]] = [
    # Left leg
    (1, 2),    # pelvis → left hip
    (2, 3),    # left hip → left knee
    (3, 5),    # left knee → left ankle

    # Right leg
    (1, 18),   # pelvis → right hip
    (18, 19),  # right hip → right knee
    (19, 21),  # right knee → right ankle

    # Spine
    (1, 34),   # pelvis → lumbar
    (34, 35),  # lumbar → mid spine
    (35, 36),  # mid spine → thoracic
    (36, 37),  # thoracic → upper spine

    # Right arm
    (37, 38),  # upper spine → right clavicle
    (38, 39),  # right clavicle → right shoulder
    (39, 40),  # right shoulder → right elbow
    (40, 42),  # right elbow → right wrist

    # Left arm
    (37, 74),  # upper spine → left clavicle
    (74, 75),  # left clavicle → left shoulder
    (75, 76),  # left shoulder → left elbow
    (76, 78),  # left elbow → left wrist

    # Neck and head
    (37, 110), # upper spine → neck
    (110, 113), # neck → head
]

# ──────────────────────────────────────────────────────────────
# Angle triples — (upstream, joint_center, downstream)
# The angle is computed at joint_center between the two limb vectors.
# ──────────────────────────────────────────────────────────────

ANGLE_TRIPLES: dict[str, tuple[int, int, int]] = {
    'L knee':     (JOINT['l_upleg'],    JOINT['l_lowleg'],  JOINT['l_talocrural']),
    'R knee':     (JOINT['r_upleg'],    JOINT['r_lowleg'],  JOINT['r_talocrural']),
    'L elbow':    (JOINT['l_uparm'],    JOINT['l_lowarm'],  JOINT['l_wrist']),
    'R elbow':    (JOINT['r_uparm'],    JOINT['r_lowarm'],  JOINT['r_wrist']),
    'L hip':      (JOINT['c_spine0'],   JOINT['l_upleg'],   JOINT['l_lowleg']),
    'R hip':      (JOINT['c_spine0'],   JOINT['r_upleg'],   JOINT['r_lowleg']),
    'L shoulder': (JOINT['l_clavicle'], JOINT['l_uparm'],   JOINT['l_lowarm']),
    'R shoulder': (JOINT['r_clavicle'], JOINT['r_uparm'],   JOINT['r_lowarm']),
    'Trunk':      (JOINT['root'],       JOINT['c_spine1'],  JOINT['c_spine3']),
    'Neck':       (JOINT['c_spine3'],   JOINT['c_neck'],    JOINT['c_head']),
}

# ──────────────────────────────────────────────────────────────
# Relative rotation pairs — (parent_idx, child_idx)
# Used to compute the child's rotation relative to its parent
# and visualise it as XYZ axis triads.
# ──────────────────────────────────────────────────────────────

RELATIVE_ROT_PAIRS: dict[str, tuple[int, int]] = {
    'L knee':     (JOINT['l_upleg'],    JOINT['l_lowleg']),
    'R knee':     (JOINT['r_upleg'],    JOINT['r_lowleg']),
    'L elbow':    (JOINT['l_uparm'],    JOINT['l_lowarm']),
    'R elbow':    (JOINT['r_uparm'],    JOINT['r_lowarm']),
    'L hip':      (JOINT['c_spine0'],   JOINT['l_upleg']),
    'R hip':      (JOINT['c_spine0'],   JOINT['r_upleg']),
    'L shoulder': (JOINT['l_clavicle'], JOINT['l_uparm']),
    'R shoulder': (JOINT['r_clavicle'], JOINT['r_uparm']),
    'Trunk':      (JOINT['root'],       JOINT['c_spine1']),
    'Neck':       (JOINT['c_spine3'],   JOINT['c_neck']),
}
