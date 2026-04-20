from isaacsim import SimulationApp
import numpy as np
import time

# ======================
# START ISAAC SIM
# ======================
simulation_app = SimulationApp({"headless": False})

import omni.usd
import omni.kit.app
from isaacsim.core.api import SimulationContext
from isaacsim.core.prims import SingleArticulation

# ======================
# CONFIG
# ======================
USD_PATH = "C:/Users/Abhay/Desktop/hexx/hexa2sim_v3_standing.usd"
ROBOT_PATH = "/hexa2sim"
MOTION_FILE = "C:/Users/Abhay/Desktop/hexx/motions.txt"

app = omni.kit.app.get_app()

# ======================
# LOAD STAGE
# ======================
omni.usd.get_context().open_stage(USD_PATH)

for _ in range(50):
    app.update()

# ======================
# START SIMULATION
# ======================
sim = SimulationContext.instance() or SimulationContext()
sim.play()

for _ in range(50):
    app.update()

# ======================
# LOAD ROBOT
# ======================
robot = SingleArticulation(prim_path=ROBOT_PATH)
robot.initialize()

print("✅ Robot initialized")
print("Joints:", robot.dof_names)

# ======================
# LOAD MOTION FILE
# ======================
def load_motion():
    poses = []
    try:
        with open(MOTION_FILE, "r") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#"):
                    vals = [float(x) for x in line.split()]
                    if len(vals) == 18:
                        poses.append(vals)
    except Exception as e:
        print("Error loading file:", e)

    return poses

# ======================
# REORDER FUNCTION
# ======================
def reorder(vals):
    vals = np.array(vals)
    hips = vals[0::3]
    mids = vals[1::3]
    lowers = vals[2::3]
    return np.concatenate([hips, mids, lowers])

# ======================
# LIVE UPDATE LOOP
# ======================
last_pose = None

print("🚀 Live control started. Edit motions.txt and save.")

while simulation_app.is_running():

    app.update()

    poses = load_motion()

    if len(poses) == 0:
        continue

    current = poses[0]  # only first pose used

    # update only if changed
    if last_pose is None or current != last_pose:
        ordered = reorder(current)

        robot.set_joint_positions(ordered)

        print("Updated pose:", current[:3])
        last_pose = current

    time.sleep(0.1)

# ======================
# CLEANUP
# ======================
simulation_app.close()