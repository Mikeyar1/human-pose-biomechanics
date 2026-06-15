# SAM 3DB Pose Analysis Pipeline

Biomechanical analysis pipeline for human performance assessment using Meta's SAM 3D Body model. Takes a single image or video frame and produces a 3D skeleton with 127 joints, joint flexion angles, and segment orientation data.

---

## What It Does

The pipeline takes an image of a person, runs it through SAM 3DB to estimate a full 3D pose, and produces an interactive two-panel visualization that displays the joint angles and relative orientation of each joint. Example below:

<img src="./data/input/fig3.png" alt="Joint Analysis Visualization" width="900">
<br>
<img src="./data/output/fig3.png" alt="Joint Analysis Visualization" width="900">
VV
**Interactive visualization:** Download [joint_analysis.html](joint_analysis.html?raw=true) and open it in your browser to explore the 3D skeleton with hover data.

**Left panel — Joint angles:** Shows how bent each joint is using a position-based dot-product method. Color encodes flexion on a blue-to-red gradient (blue = straight, red = bent). The angle in degrees is labeled at each joint.

**Right panel — Relative orientation:** Shows the three-axis orientation of each joint relative to its parent using the model's rotation matrices. Red/Green/Blue arrows represent the X/Y/Z axes of the relative rotation. Euler angles appear on hover.

---

## Notebooks

| Notebook                | Purpose                                                                                                                                         |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| `sam3db_pipeline.ipynb` | Inference pipeline — loads the model, processes an image, and produces raw 3D pose outputs (joint positions, rotation matrices, mesh)           |
| `joint_analysis.ipynb`  | Biomechanical analysis — computes flexion angles and rotation decompositions from the pipeline outputs, generates the interactive visualization |

Run `sam3db_pipeline.ipynb` first, then `joint_analysis.ipynb`.

---

## How to Run

I developed these notebooks in **Google Colab**. Each notebook contains all the cells needed to install the model, download dependencies, and run the pipeline — just run the cells in order.

1. Open `sam3db_pipeline.ipynb` in Google Colab
2. Run all cells — this will install SAM 3DB and its dependencies, load a model checkpoint, process your image, and then save the model output as a Pickle file
3. Open `joint_analysis.ipynb` and load the Pickle file from step 2
4. Run all cells — this produces the interactive HTML visualization and saves it to your Google Drive

If you are running this in a different IDE or environment and something breaks, let me know so I can help debug it.

---

## Documentation

- `SAM3DB_research.md` — Technical reference guide covering the MHR skeleton structure, output tensors, joint index table, coordinate systems, and camera configuration
- `SAM3DB_Technical_Brief.docx` — Summary brief for technical stakeholders covering the analysis methodology and what changed from rotation-based to position-based computation