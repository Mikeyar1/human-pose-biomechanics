# SAM3D Body  — Technical Reference Guide

**Model:** SAM 3D Body (3DB), Meta
**Body model used:** Momentum Human Rig (MHR)  

---
## MHR Joints Index Reference

**How the joint indices were obtained:**
The MHR joint list and indices are not published anywhere in the official documentation, the research paper, or the GitHub README. To recover them, I inspected the SAM3D Body estimator object at runtime. Exploring the estimator object, I found a skeleton definition at `estimator.model.head_pose.mhr.character_torch.skeleton` which exposes the joints names ordered by its index, also confirmed by the fact that the list contains exactly 127 entrie, matching the number of joints in the MHR skeleton. 

**Full Joints Table**

| Index | Joint Name | Body Region |
|---|---|---|
| 0 | body_world | World anchor — global origin, not a physical joint |
| 1 | root | Pelvis — reference point for all motion |
| 2 | l_upleg | Left thigh |
| 3 | l_lowleg | Left shin |
| 4 | l_foot | Left foot |
| 5 | l_talocrural | Left ankle — true ankle hinge |
| 6 | l_subtalar | Left subtalar — controls inversion/eversion |
| 7 | l_transversetarsal | Left midfoot |
| 8 | l_ball | Left toe |
| 9 | l_lowleg_twist1_proc | Left shin twist 1 |
| 10 | l_lowleg_twist2_proc | Left shin twist 2 |
| 11 | l_lowleg_twist3_proc | Left shin twist 3 |
| 12 | l_lowleg_twist4_proc | Left shin twist 4 |
| 13 | l_upleg_twist0_proc | Left thigh twist 0 |
| 14 | l_upleg_twist1_proc | Left thigh twist 1 |
| 15 | l_upleg_twist2_proc | Left thigh twist 2 |
| 16 | l_upleg_twist3_proc | Left thigh twist 3 |
| 17 | l_upleg_twist4_proc | Left thigh twist 4 |
| 18 | r_upleg | Right thigh |
| 19 | r_lowleg | Right shin |
| 20 | r_foot | Right foot |
| 21 | r_talocrural | Right ankle — true ankle hinge |
| 22 | r_subtalar | Right subtalar — controls inversion/eversion |
| 23 | r_transversetarsal | Right midfoot |
| 24 | r_ball | Right toe |
| 25 | r_lowleg_twist1_proc | Right shin twist 1 |
| 26 | r_lowleg_twist2_proc | Right shin twist 2 |
| 27 | r_lowleg_twist3_proc | Right shin twist 3 |
| 28 | r_lowleg_twist4_proc | Right shin twist 4 |
| 29 | r_upleg_twist0_proc | Right thigh twist 0 |
| 30 | r_upleg_twist1_proc | Right thigh twist 1 |
| 31 | r_upleg_twist2_proc | Right thigh twist 2 |
| 32 | r_upleg_twist3_proc | Right thigh twist 3 |
| 33 | r_upleg_twist4_proc | Right thigh twist 4 |
| 34 | c_spine0 | Lumbar spine — L5/L4 level |
| 35 | c_spine1 | Mid spine — L3/L2 level |
| 36 | c_spine2 | Thoracic spine — T12/T10 level |
| 37 | c_spine3 | Upper thoracic — T8/T6 level |
| 38 | r_clavicle | Right clavicle |
| 39 | r_uparm | Right upper arm |
| 40 | r_lowarm | Right forearm |
| 41 | r_wrist_twist | Right wrist twist |
| 42 | r_wrist | Right wrist |
| 43 | r_pinky0 | Right pinky MCP |
| 44 | r_pinky1 | Right pinky PIP |
| 45 | r_pinky2 | Right pinky DIP |
| 46 | r_pinky3 | Right pinky tip |
| 47 | r_pinky_null | Right pinky null |
| 48 | r_ring1 | Right ring MCP |
| 49 | r_ring2 | Right ring PIP |
| 50 | r_ring3 | Right ring DIP |
| 51 | r_ring_null | Right ring null |
| 52 | r_middle1 | Right middle MCP |
| 53 | r_middle2 | Right middle PIP |
| 54 | r_middle3 | Right middle DIP |
| 55 | r_middle_null | Right middle null |
| 56 | r_index1 | Right index MCP |
| 57 | r_index2 | Right index PIP |
| 58 | r_index3 | Right index DIP |
| 59 | r_index_null | Right index null |
| 60 | r_thumb0 | Right thumb CMC |
| 61 | r_thumb1 | Right thumb MCP |
| 62 | r_thumb2 | Right thumb IP |
| 63 | r_thumb3 | Right thumb tip |
| 64 | r_thumb_null | Right thumb null |
| 65 | r_lowarm_twist1_proc | Right forearm twist 1 |
| 66 | r_lowarm_twist2_proc | Right forearm twist 2 |
| 67 | r_lowarm_twist3_proc | Right forearm twist 3 |
| 68 | r_lowarm_twist4_proc | Right forearm twist 4 |
| 69 | r_uparm_twist0_proc | Right upper arm twist 0 |
| 70 | r_uparm_twist1_proc | Right upper arm twist 1 |
| 71 | r_uparm_twist2_proc | Right upper arm twist 2 |
| 72 | r_uparm_twist3_proc | Right upper arm twist 3 |
| 73 | r_uparm_twist4_proc | Right upper arm twist 4 |
| 74 | l_clavicle | Left clavicle |
| 75 | l_uparm | Left upper arm |
| 76 | l_lowarm | Left forearm |
| 77 | l_wrist_twist | Left wrist twist |
| 78 | l_wrist | Left wrist |
| 79 | l_pinky0 | Left pinky MCP |
| 80 | l_pinky1 | Left pinky PIP |
| 81 | l_pinky2 | Left pinky DIP |
| 82 | l_pinky3 | Left pinky tip |
| 83 | l_pinky_null | Left pinky null |
| 84 | l_ring1 | Left ring MCP |
| 85 | l_ring2 | Left ring PIP |
| 86 | l_ring3 | Left ring DIP |
| 87 | l_ring_null | Left ring null |
| 88 | l_middle1 | Left middle MCP |
| 89 | l_middle2 | Left middle PIP |
| 90 | l_middle3 | Left middle DIP |
| 91 | l_middle_null | Left middle null |
| 92 | l_index1 | Left index MCP |
| 93 | l_index2 | Left index PIP |
| 94 | l_index3 | Left index DIP |
| 95 | l_index_null | Left index null |
| 96 | l_thumb0 | Left thumb CMC |
| 97 | l_thumb1 | Left thumb MCP |
| 98 | l_thumb2 | Left thumb IP |
| 99 | l_thumb3 | Left thumb tip |
| 100 | l_thumb_null | Left thumb null |
| 101 | l_lowarm_twist1_proc | Left forearm twist 1 |
| 102 | l_lowarm_twist2_proc | Left forearm twist 2 |
| 103 | l_lowarm_twist3_proc | Left forearm twist 3 |
| 104 | l_lowarm_twist4_proc | Left forearm twist 4 |
| 105 | l_uparm_twist0_proc | Left upper arm twist 0 |
| 106 | l_uparm_twist1_proc | Left upper arm twist 1 |
| 107 | l_uparm_twist2_proc | Left upper arm twist 2 |
| 108 | l_uparm_twist3_proc | Left upper arm twist 3 |
| 109 | l_uparm_twist4_proc | Left upper arm twist 4 |
| 110 | c_neck | Neck |
| 111 | c_neck_twist1_proc | Neck twist 1 |
| 112 | c_neck_twist0_proc | Neck twist 0 |
| 113 | c_head | Head |
| 114 | c_jaw | Jaw |
| 115 | c_teeth | Teeth |
| 116 | c_jaw_null | Jaw null |
| 117 | c_tongue0 | Tongue base |
| 118 | c_tongue1 | Tongue mid 1 |
| 119 | c_tongue2 | Tongue mid 2 |
| 120 | c_tongue3 | Tongue mid 3 |
| 121 | c_tongue4 | Tongue tip |
| 122 | r_eye | Right eye |
| 123 | r_eye_null | Right eye null |
| 124 | l_eye | Left eye |
| 125 | l_eye_null | Left eye null |
| 126 | c_head_null | Head null |

*Additional validation*

If the index-to-name mapping is correct, the Euclidean distance between any
parent-child pair must fall within the anatomically expected range for that
bone segment. Code snippet to reproduce this check:

```python

joints = outputs[0]['pred_joint_coords']  # 3d position of all 127 joints. Shape: [127, 3]

# Expected ranges in meters — based on average adult human anatomy
bone_checks = [
    (2,   3,  "l_upleg  -> l_lowleg  (femur)",    0.35, 0.50), # (2,3) are the indeces of l_upleg and l_lowleg in the 127 joints array which composes the femur bone for skeleton drawing in the visualization. (0.35,0.50) are the expected ranges in meters for the femur bone.
    (3,   5,  "l_lowleg -> l_talocrural (tibia)",  0.30, 0.50),
    (5,   8,  "l_talocrural -> l_ball (foot)",     0.10, 0.25),
    (76,  78, "l_lowarm -> l_wrist   (forearm)",   0.20, 0.35),
    (1,   34, "root     -> c_spine0  (lumbar)",    0.05, 0.20),
    (110, 113,"c_neck   -> c_head    (neck)",      0.08, 0.20),
]

print(f"{'Bone':<30} {'Distance':>10}  {'Expected':>10}  Result")
print("-" * 50)
for parent_index, child_index, name, low, high in bone_checks:
    distance = float(np.linalg.norm(joints[parent_index] - joints[child_index]))
    result = "PASS" if low <= distance <= high else "FAIL"
    print(f"{name:<40} {distance:>8.4f} m  {low}–{high} m  {result}")
```
## Outputs returned by the model image processor

`outputs.process_one_image` is the main function that takes a single image and runs the entire pipeline from raw pixels to 3D skeleton. Below are the essential parameters that it returns.

## Output Parameters

| Parameter | Shape | Type | Description |
|---|---|---|---|
| `bbox` | `[4]` | float32 | Bounding box of detected person in image pixels — `[x1, y1, x2, y2]` |
| `focal_length` | scalar | float32 | Estimated camera focal length in pixels — one component of the intrinsics matrix |
| `pred_keypoints_3d` | `[~70, 3]` | float32 | 3D positions of evaluation-format keypoints in camera space (meters) — excludes spinal joints |
| `pred_keypoints_2d` | `[~70, 2]` | float32 | 2D projection of the 3D keypoints onto the image plane (pixels) |
| `pred_vertices` | `[18439, 3]` | float32 | Full body mesh surface points in camera space (meters) — 18,439 vertices at default LOD 1 |
| `pred_cam_t` | `[3]` | float32 | Camera translation vector `[tx, ty, tz]` placing the person in 3D camera space (meters) |
| `pred_pose_raw` | `[204]` | float32 | Full MHR parameter vector — 136 pose parameters and 68 skeleton scaling parameters |
| `global_rot` | `[3]` or `[3,3]` | float32 | Root joint (pelvis) orientation in camera space — the overall body rotation |
| `body_pose_params` | subset of `[204]` | float32 | MHR parameters controlling body joint articulations — spine, limbs, excluding hands |
| `hand_pose_params` | subset of `[204]` | float32 | MHR parameters controlling finger articulation for both hands — from the hand decoder |
| `scale_params` | `[68]` | float32 | Skeleton transformation parameters — encodes bone lengths and skeletal proportions, constant per subject |
| `shape_params` | `[45]` | float32 | Body surface shape coefficients — 20 body + 20 head + 5 hand PCA components |
| `expr_params` | `[72]` | float32 | Facial expression blendshape weights following FACS — range −1 to +1 |
| `mask` | `[H, W]` or None | uint8 | Person segmentation mask — binary, white = person. None if use_mask=False |
| `pred_joint_coords` | `[127, 3]` | float32 | 3D position of all 127 MHR skeleton joints in camera space (meters) — includes full spinal chain |
| `pred_global_rots` | `[127, 3, 3]` | float32 | Global orientation of each joint as a 3×3 rotation matrix — columns are local X, Y, Z axes in camera space |
| `mhr_model_params` | bundled | mixed | Full MHR forward pass inputs — identity coefficients, model parameters, and expression coefficients |
| `lhand_bbox` | `[4]` | float32 | Left hand bounding box in image pixels — `[x1, y1, x2, y2]` |
| `rhand_bbox` | `[4]` | float32 | Right hand bounding box in image pixels — `[x1, y1, x2, y2]` |

## Visualizing the vectors of Key joints

## Coordinate Systems and Camera Configuration

### Current configuration
By default, SAM3D Body operates entirely in **camera space**. The camera is the origin `[0,0,0]` of the coordinate system, which axes defined as:

- **X** — pointing right
- **Y** — pointing down
- **Z** — pointing into the scene (away from the camera)

All outputs are expressed in this coordinate system: 

- `pred_joint_coords` — joint positions in meters from the camera origin
- `pred_global_rots` — joint orientations expressed relative to the camera axes
- `pred_vertices` — mesh surface points in meters from the camera origin

Without a calibrated camera, the model estimates the focal lengrh from the image content using MoGE2 model. This isestimate is generally reliable but introduces uncertaintiy in the depth axis `z`. However, it does not affect the joint angles.

### Camera intrinsics — improving metric accuracy

Camera intrinsics describe the internal optical properties of the camera — 
focal length and principal point — encoded in the 3×3 matrix **K**.

Passing a calibrated K matrix replaces the MoGe2 focal length estimate and 
improves the metric accuracy of all positional outputs. This is particularly 
important for the depth estimate and for `pred_cam_t`, which places 
the person in 3D space relative to the camera.

### Camera extrinsics — transforming to world coordinates

Camera extrinsics describe where the camera is positioned and oriented in 
the physical world — a rotation matrix **R_ext** and translation vector 
**t_ext** produced by the camera calibration.

Applying the extrinsic transform moves all outputs from camera space into 
the lab's world coordinate system, setting the origin where the calibration reference was placed.

```python
# R_ext: [3, 3] rotation matrix from calibration
# t_ext: [3] translation vector from calibration

# Transform joint positions to world space
joints_world = (R_ext @ pred_joint_coords.T).T + t_ext

# Transform joint orientations to world space
glob_rot_world = np.array([R_ext @ R for R in pred_global_rots])
```

After this transformation, joint positions are in meters from the lab 
origin and joint orientations are expressed relative to the lab's axes — 
so **forward** means forward in the room, not forward relative to the camera

---

### Different uses

| Research question | Intrinsics | Extrinsics |
|---|---|---|
| Joint angles (knee flexion, elbow bend) | Not required | Not required |
| Segment orientation relative to body | Not required | Not required |
| Expert vs novice posture comparison | Not required | Not required |
| Metric bone length verification | Recommended | Not required |
| Absolute joint position in meters | Required | Not required |
| Which direction person faces in room | Not required | Required |
| Align pose with force plate data | Required | Required |
| Multi-camera fusion in shared frame | Required | Required |
| Correlate with EEG electrode positions | Required | Required |
