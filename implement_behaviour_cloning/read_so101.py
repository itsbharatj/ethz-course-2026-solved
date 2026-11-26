##Take an existing dataset of SO-101 (inside a mujoco simulation), have functions for sending observations in a given format

from lerobot.datasets.lerobot_dataset import LeRobotDataset

ds = LeRobotDataset(
    "rovolabs/so-arm101-pick-place",
    episodes=list(range(100)),
    root="./data/so101_pick_place",   # the dataset files go directly in here
)

## Implement a simple BC algorithm inside the MuJoCo Simulator

