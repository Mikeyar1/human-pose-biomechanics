"""
pipeline.py — Model loading and inference.

Wraps the SAM-3D Body estimator and visualizer setup so notebooks stay light.

Usage:
    from sam3db.pipeline import load_model, run_inference

    estimator, visualizer = load_model()
    outputs = run_inference(estimator, "path/to/image.png")
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

# Load .env from the project root (two levels up from this file)
load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def _ensure_sam3dbody_on_path() -> Path:
    """
    Adds the sam-3d-body/notebook directory to sys.path so that the
    upstream `utils` module (setup_sam_3d_body, setup_visualizer, etc.)
    can be imported.

    Raises FileNotFoundError if sam-3d-body hasn't been cloned yet.
    """
    root = Path(__file__).resolve().parents[1]
    notebook_dir = root / "notebooks"

    if not notebook_dir.exists():
        raise FileNotFoundError(
            "sam-3d-body not found. Run the setup cell in the notebook first:\n"
            "  !git clone https://github.com/facebookresearch/sam-3d-body.git"
        )

    if str(notebook_dir) not in sys.path:
        sys.path.insert(0, str(notebook_dir))

    return notebook_dir


def load_model(hf_repo_id: str = "facebook/sam-3d-body-dinov3"):
    """
    Authenticates with Hugging Face (using HF_TOKEN from .env),
    then loads the SAM-3D Body estimator and Pyrender visualizer.

    Args:
        hf_repo_id: Hugging Face repo to download the checkpoint from.

    Returns:
        estimator: SAM3DBodyEstimator instance.
        visualizer: Pyrender visualizer instance.
    """
    token = os.getenv("HF_TOKEN")
    if not token:
        raise EnvironmentError(
            "HF_TOKEN not set. Add it to your .env file:\n  HF_TOKEN=hf_your_token_here"
        )

    from huggingface_hub import login
    login(token=token, add_to_git_credential=False)

    _ensure_sam3dbody_on_path()

    from utils import setup_sam_3d_body, setup_visualizer  # upstream module
    estimator = setup_sam_3d_body(hf_repo_id=hf_repo_id)
    visualizer = setup_visualizer()

    return estimator, visualizer


def run_inference(estimator, image_path: str) -> list[dict]:
    """
    Runs SAM-3D Body on a single image.

    Args:
        estimator: Loaded estimator returned by load_model().
        image_path: Absolute or relative path to the input image.

    Returns:
        List of per-person output dicts. Each dict contains keys like:
          - pred_joint_coords : np.ndarray [127, 3]  (metres)
          - pred_global_rots  : np.ndarray [127, 3, 3]
          - pred_vertices     : np.ndarray [N, 3]
          - pred_keypoints_2d : np.ndarray [127, 2]
          etc.
    """
    image_path = str(Path(image_path).resolve())
    outputs = estimator.process_one_image(image_path)
    print(f"[pipeline] Detected {len(outputs)} person(s) in '{Path(image_path).name}'")
    return outputs
