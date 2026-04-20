https://drive.google.com/file/d/1hJKEDaNLk0jpT74t_edVvrhgmM4Ln3m6/view?usp=sharing
# Hexapod Manual Control (Isaac Sim)

## 🚀 Overview

This project lets you **manually control a hexapod robot** in Isaac Sim using a simple text file (`motions.txt`).
Edit the file → save → the robot updates instantly.

---

## 📁 Files

```text
hexapod_motion_player.py   # Main script
motions.txt                # Joint values
```

---

## ▶️ Run

```bash
cd C:\isaac-sim
python hexapod_motion_player.py
```

---

## 🦿 Robot Setup

* 6 legs
* 3 joints per leg (hip, mid, lower)
* Total: **18 joints**

---

## 🧠 motions.txt Format

* Exactly **18 values**
* Space-separated
* One line = one pose

### Example:

```text
0.0 0.5 0.3   0.0 0.5 0.3   0.0 0.5 0.3   0.0 0.5 0.3   0.0 0.5 0.3   0.0 0.5 0.3
```

---

## 🎮 Controls

* **hip** → forward/back
* **mid** → up/down
* **lower** → foot angle

---

## 🔁 How it works

* Script continuously reads `motions.txt`
* Applies values every frame
* Edit → Save → robot updates instantly

---

## ⚠️ Common Issues

* Not saving file → no update
* Wrong number of values → ignored
* Robot not visible → press **F** to focus

---

## 📌 Summary

A simple way to control and test a hexapod robot in real time without RL.
