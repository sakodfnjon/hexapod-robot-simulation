# Reinforcement Learning Experiments

This folder contains early-stage reinforcement learning (RL) experiments for enabling locomotion in a hexapod robot within a simulated environment.

---

## 🔧 Overview

Reinforcement learning was explored to allow the robot to learn walking behavior through trial and error in simulation.

The robot interacts with the environment by taking actions (joint movements) and receives feedback in the form of rewards, which guide it toward improved movement over time.

---

## ⚙️ Approach

- The hexapod robot is simulated in NVIDIA Isaac Sim  
- Actions correspond to joint angle adjustments  
- Rewards are based on movement performance, such as:
  - Forward motion  
  - Stability  
  - Reduced unnecessary movement  

---

## 📊 Training Progress

Approximately **4000 training iterations** were performed.

The learning process showed gradual improvement in movement behavior, although stable and coordinated walking has not yet been fully achieved.

---

## 🎥 Reinforcement Learning Progress

The following videos show the progression of the robot's behavior before and after training:

### 🔹 Initial State (0 iterations)
[Watch initial behavior](LINK_0_ITR)
https://drive.google.com/file/d/1Rs_e3_ZTe4drIrG-UUG0RPW0uPQByN_S/view?usp=sharing

### 🔹 After Training (~4000 iterations)
[Watch learned behavior](LINK_4000_ITR)
https://drive.google.com/file/d/1E2OoZK7n6mejyiayd5wvECzDzpEBHEyy/view?usp=sharing
---

## 📌 Observations

- Initial behavior is mostly random and uncoordinated  
- After training, the robot begins to exhibit partial movement patterns  
- Stability and coordinated gait remain challenges  

---

## ⚠️ Limitations

- Gait is not yet stable  
- Reward function requires further tuning  
- More training iterations and optimization are needed  

---

## 🚀 Future Work

- Improve reward function for better stability  
- Implement structured gait patterns (e.g., tripod gait)  
- Combine reinforcement learning with kinematic control  
- Transfer learned behavior to real hardware  

---

## 🧠 Notes

This is an experimental implementation aimed at understanding how reinforcement learning can be applied to robotics problems. The focus was on learning concepts and observing behavior rather than achieving a fully optimized solution.

---
