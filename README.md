# SmartNet-Guard
A modular edge network security monitoring system featuring real-time traffic analysis, DDoS threat interception (IPS), and AI-based biometric authentication (Face ID) for system access control.

# 🛡️ Edge-Security-Sentinel

## 🚀 Overview

**Edge-Security-Sentinel** is a modular edge network security framework developed to eliminate the "Complexity-Visibility Gap" in edge infrastructure[cite: 3]. It integrates real-time packet analysis with AI-driven authentication to provide autonomous, proactive threat mitigation at the network perimeter[cite: 3, 5, 7].



## 📸 System Visuals

*(在 GitHub 上上传截图到 `/docs` 文件夹，并替换下方链接)*

| **Modular Console Dashboard** | **Telegram Real-time Alerting** |
| --- | --- |
|  |  |
| *Visualizing throughput & IPS status* | *Remote threat notifications & C2* |


## 🏗️ Core Architecture

The system is built on a decoupled architecture for maximum stability[cite: 6, 7]:

### 1. Hardware Interface (`display_lcd.py`)

Provides physical status updates. It uses a **No-Clear-Write** methodology to update 20x4 LCD screens, preventing flickering and character garbage[cite: 4].

* **Key Code**: `lcd.cursor_pos = (0, 0); lcd.write_string(lines[0][:20])`

### 2. Network Sniffer (`edge_probe_v2.py`)

A Scapy-based sentinel that monitors `wlan0`. It aggregates packets and computes telemetry data locally before pushing it to the Math Engine[cite: 5].

* **Key Code**: `sniff(iface=TARGET_INTERFACE, prn=packet_callback, store=0)`

### 3. Math Core Engine (Node-RED)

The central intelligence. It calculates **Z-Score anomalies** to detect DDoS volumetric floods.

* **Logic**: `zScore = (currentPPS - mean) / stdDev`[cite: 7].

### 4. Biometric Auth (`face_auth.py` & `local_face_api.py`)

Uses the **InsightFace (antelopev2)** model to perform 1:1 cosine similarity matching[cite: 1, 2].

* **Key Code**: `sim = np.dot(emb1, emb2) / (norm1 * norm2)`[cite: 2].



## 🛠️ Modules & Features

### Telegram Integration (`node-red-contrib-telegrambot`)

Allows remote administration. It broadcasts DDoS alerts and accepts control commands like `/on`, `/off`, `/reset`, and `/status` via an interactive inline keyboard[cite: 7].

### Dashboard & Metrics (`node-red-dashboard`)

Provides a real-time digital twin of the network, synchronized across `Threat Logs`, `All Traffic Logs`, and `Active Firewall Blocks` tables, ensuring full network visibility[cite: 7].

### IPS & Dynamic Governor

Automatically injects `iptables` rules when a threat reaches a critical state. It features a heuristic hit-map system to distinguish between transient warnings and persistent attacks[cite: 7].



## 🔧 Deployment

1. **Requirements**: Raspberry Pi, Node-RED, InsightFace dependencies[cite: 2, 7].
2. **Setup**:
```bash
# Enable background AI service
nohup python3 /home/mj/local_face_api.py > api.log 2>&1 &

```


3. **Flows**: Import the provided `flows.json` and configure your `chatId` in the Telegram function nodes[cite: 7].


## 🎓 Academic Context

This project originates from research into **Network Tool Analysis** and the **Complexity-Visibility Gap**, aiming to provide affordable, high-end security tools for constrained edge devices[cite: 3].
