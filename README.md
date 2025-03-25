# SkyGo Drone Delivery 🚁📦

[![Python Version](https://img.shields.io/badge/Python-3.13-blue?logo=python&logoColor=white)](https://www.python.org/) [![Pytest](https://img.shields.io/badge/Pytest-8.3.5-green?logo=pytest&logoColor=white)](https://docs.pytest.org/) [![License](https://img.shields.io/badge/License-MIT-lightgrey)](LICENSE)

---
## 🌟 Overview

**SkyGo Drone Delivery** is an AI-driven project that optimizes the assignment of drones to delivery orders across a smart city grid. Our solution minimizes delivery time and maximizes drone utilization, taking into account real-world constraints such as payload, distance, and deadlines.

---

📽️ **Visual output.json Representation**  

![Image](https://github.com/user-attachments/assets/0c3a5a8a-8138-41e4-a843-cdf48c7f0872)

---

## 🎯Problem Statement

Imagine a futuristic drone delivery company operating in a 20×20 city grid:
- **Drones**: Each drone has a specific payload capacity, maximum round-trip distance, speed, and an availability status.
- **Orders**: Each order comes with a delivery location (x, y), a deadline (in minutes), and a package weight.
![Image](https://github.com/user-attachments/assets/0e02ab11-92ee-405c-9505-9a16c943ff91)

**Task:**  
Efficiently assign drones to orders such that:
- **Total travel distance is minimized.**
- **Drone usage is maximized.**
- **All operational constraints are satisfied.**

---

## Unique Aspects 🎉

- **Modular Architecture:**  
  The solution is built with clear separation into input parsing, optimization (greedy assignment), and output generation modules—making it easy to understand, test, and extend.
- **Real-World Simulation:**  
  Uses Manhattan distance to mimic grid-based travel and considers real constraints (payload, flight range, deadlines).
- **Test-Driven:**  
  Unit tests verify critical functions, demonstrating a commitment to robustness and code quality.

---

---

## 🌐 **How to Use**  

1️⃣ Clone the repository.  
2️⃣ Install dependencies using `requirements.txt`.  

🎯 **Commands**:  
```bash
git clone https://github.com/username/SkyGo_Drone_Deliver.git
cd SkyGo-Drone-Delivery
pip install -r requirements.txt

