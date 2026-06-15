"""
visualization.py — 3D plotting helpers for SAM-3D Body outputs.

All functions accept a Plotly Figure and add traces to a specific
(row, col) subplot slot — making them composable in multi-panel layouts.

Usage:
    from sam3db.visualization import (
        add_skeleton,
        add_joint_angles,
        add_relative_rotation_triads,
    )
"""

import numpy as np
import plotly.graph_objects as go
from scipy.spatial.transform import Rotation

from .joints import BONES, ANGLE_TRIPLES, RELATIVE_ROT_PAIRS

# Scale for the orientation axis triads (metres)
TRIAD_SCALE: float = 0.12


def add_skeleton(
    fig: go.Figure,
    joints: np.ndarray,
    row: int = 1,
    col: int = 1,
) -> None:
    """
    Draw joint markers and anatomical bone lines onto a 3D subplot.

    Args:
        fig:    Plotly figure with at least one scatter3d subplot.
        joints: [127, 3] array of joint positions in metres.
        row:    Subplot row index (1-based).
        col:    Subplot column index (1-based).
    """
    # All joint markers
    fig.add_trace(go.Scatter3d(
        x=joints[:, 0], y=joints[:, 1], z=joints[:, 2],
        mode='markers',
        marker=dict(size=2, color='#444'),
        name='All joints',
        showlegend=False,
        hoverinfo='skip',
    ), row=row, col=col)

    # Bone lines
    for a, b in BONES:
        fig.add_trace(go.Scatter3d(
            x=[joints[a, 0], joints[b, 0]],
            y=[joints[a, 1], joints[b, 1]],
            z=[joints[a, 2], joints[b, 2]],
            mode='lines',
            line=dict(color='#444', width=2),
            showlegend=False,
            hoverinfo='skip',
        ), row=row, col=col)


def add_joint_angles(
    fig: go.Figure,
    joints: np.ndarray,
    angle_triples: dict | None = None,
    row: int = 1,
    col: int = 1,
) -> None:
    """
    Color-code limb segments by flexion angle and annotate each joint.

    Blue = straight (0°), Red = fully bent (90°+).

    Args:
        fig:           Plotly figure.
        joints:        [127, 3] joint positions in metres.
        angle_triples: Dict of {label: (upstream_idx, center_idx, downstream_idx)}.
                       Defaults to the standard ANGLE_TRIPLES from joints.py.
        row:           Subplot row (1-based).
        col:           Subplot column (1-based).
    """
    if angle_triples is None:
        angle_triples = ANGLE_TRIPLES

    for name, (up_idx, mid_idx, down_idx) in angle_triples.items():
        v1 = joints[up_idx] - joints[mid_idx]
        v2 = joints[down_idx] - joints[mid_idx]
        v1 /= np.linalg.norm(v1)
        v2 /= np.linalg.norm(v2)

        inter_angle = np.degrees(np.arccos(np.clip(np.dot(v1, v2), -1.0, 1.0)))
        flexion = 180.0 - inter_angle

        t = min(flexion / 90.0, 1.0)
        color = f'rgb({int(255 * t)}, 50, {int(255 * (1 - t))})'

        origin = joints[up_idx]
        child  = joints[down_idx]
        midpt  = (origin + child) / 2

        fig.add_trace(go.Scatter3d(
            x=[origin[0], child[0]],
            y=[origin[1], child[1]],
            z=[origin[2], child[2]],
            mode='lines',
            line=dict(color=color, width=6),
            name=f'{name} {flexion:.0f}°',
            showlegend=True,
        ), row=row, col=col)

        fig.add_trace(go.Scatter3d(
            x=[midpt[0]], y=[midpt[1]], z=[midpt[2]],
            mode='text',
            text=[f'{name}<br>{flexion:.1f}°'],
            textfont=dict(size=9, color='black'),
            showlegend=False,
        ), row=row, col=col)


def add_relative_rotation_triads(
    fig: go.Figure,
    joints: np.ndarray,
    glob_rot: np.ndarray,
    rel_rot_pairs: dict | None = None,
    scale: float = TRIAD_SCALE,
    row: int = 1,
    col: int = 1,
) -> None:
    """
    Draw XYZ orientation triads showing each joint's rotation
    relative to its parent. Hovering shows Euler angles (ZYX).

    Args:
        fig:           Plotly figure.
        joints:        [127, 3] joint positions in metres.
        glob_rot:      [127, 3, 3] global rotation matrices.
        rel_rot_pairs: Dict of {label: (parent_idx, child_idx)}.
                       Defaults to RELATIVE_ROT_PAIRS from joints.py.
        scale:         Length of each axis arrow in metres.
        row:           Subplot row (1-based).
        col:           Subplot column (1-based).
    """
    if rel_rot_pairs is None:
        rel_rot_pairs = RELATIVE_ROT_PAIRS

    axis_colors = ['red', 'green', 'blue']
    axis_labels = ['X', 'Y', 'Z (flex)']
    legend_shown = [False, False, False]

    for name, (parent_idx, child_idx) in rel_rot_pairs.items():
        R_parent = glob_rot[parent_idx]
        R_child  = glob_rot[child_idx]
        R_rel    = R_parent.T @ R_child

        angles = Rotation.from_matrix(R_rel).as_euler('ZYX', degrees=True)
        hover  = (
            f'{name}<br>'
            f'Z: {angles[0]:+.1f}°<br>'
            f'Y: {angles[1]:+.1f}°<br>'
            f'X: {angles[2]:+.1f}°'
        )

        origin = joints[child_idx]

        for ax_i in range(3):
            direction = R_parent @ R_rel[:, ax_i]
            tip = origin + direction * scale
            show = not legend_shown[ax_i]
            legend_shown[ax_i] = True

            fig.add_trace(go.Scatter3d(
                x=[origin[0], tip[0]],
                y=[origin[1], tip[1]],
                z=[origin[2], tip[2]],
                mode='lines+markers',
                line=dict(color=axis_colors[ax_i], width=5),
                marker=dict(
                    size=[1, 5],
                    color=axis_colors[ax_i],
                    symbol=['circle', 'diamond'],
                ),
                name=f'{axis_labels[ax_i]} axis' if show else None,
                legendgroup=axis_labels[ax_i],
                showlegend=show,
                hoverinfo='skip',
            ), row=row, col=col)

        # Invisible hover point that shows Euler angles on mouse-over
        fig.add_trace(go.Scatter3d(
            x=[origin[0]], y=[origin[1]], z=[origin[2]],
            mode='markers',
            marker=dict(size=8, color='rgba(0,0,0,0)'),
            hovertext=hover,
            hoverinfo='text',
            showlegend=False,
        ), row=row, col=col)
