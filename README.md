# 🛡️ Edge-Security-Sentinel

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status" />
  <img src="https://img.shields.io/badge/Platform-RaspberryPi-blue.svg" alt="Platform" />
  <img src="https://img.shields.io/badge/Security-IPS_Engine-red.svg" alt="Security" />
  <img src="https://img.shields.io/badge/Auth-Biometric_FaceID-purple.svg" alt="Auth" />
</p>

<p align="center">
  <b>Bridging the Complexity-Visibility Gap in Edge Network Infrastructure.</b>
</p>

---

## ⚡ Overview
**Edge-Security-Sentinel** is a high-availability, AI-driven security framework designed for Raspberry Pi. It transforms edge hardware into a hardened network perimeter, capable of autonomous threat detection and intelligent mitigation.

## 🏗️ System Architecture
The system employs a dual-bus architecture, separating the core math engine from service modules to ensure operational stability:

*   **Core Math Engine**: Utilizes heuristic Z-Score and PPS (Packets Per Second) analysis to identify volumetric DDoS threats in real-time.
*   **Security Layer (IPS)**: An automated governor that interfaces with `iptables` to perform granular threat mitigation.
*   **Biometric Access Gateway**: Implements InsightFace-powered facial recognition, acting as a "Zero-Trust" physical key for system management.
*   **Modular Dashboard**: A centralized console for visualizing throughput, traffic logs, and firewall block lists.

## 📸 Operational Visuals

| **Modular Console Dashboard** | **Telegram Real-time Alerting** |
| :---: | :---: |
| ![Dashboard](docs/dashboard.png) | ![Telegram](docs/telegram.png) |
| *Traffic analysis & IPS status* | *Remote threat notifications & C2* |

---

## 🏗️ Core Modules

The system is built on a decoupled architecture for maximum stability:

### 1. Hardware Interface (`display_lcd.py`)

<img width="600" height="400" alt="Hardware View" src="docs/Hardware.png" />

Provides physical status updates. It uses a **No-Clear-Write** methodology to update 20x4 LCD screens, preventing flickering and character garbage.

**Key Code:** 
```python
lcd.cursor_pos = (0, 0); lcd.write_string(lines[0][:20])
