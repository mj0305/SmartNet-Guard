# 🛡️ Edge-Security-Sentinel

<p align="center">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status" />
</p>

<p align="center">
  <b>Bridging the Complexity-Visibility Gap in Edge Network Infrastructure.</b>
</p>


## 📌 Project Overview
A robust, host-based edge security sentinel designed to bridge the complexity-visibility gap in modern network administration. Engineered specifically for resource-constrained edge environments like the Raspberry Pi, this system provides real-time packet telemetry, automated volumetric threat mitigation, and a "Zero-Trust" biometric access gateway without the overhead of enterprise-grade security suites.


This project focuses on L3-L4 anomaly detection and interactive remote management, serving as a transparent analytical and defensive tool for organizational network perimeters.## 📂 Project Structure

```bash
SmartNet-Guard/
│
├── data/                   # Log exports and historical threat captures
├── docs/                   # Architecture diagrams and UI screenshots
│   ├── Hardware.png
│   ├── Network_Sniffer.png
│   ├── CoreMathEngine.png
│   ├── dashboard.png
│   └── telegram.jpg
│
├── flows.json              # Core Node-RED workspace (Math Engine & Dashboard)
├── edge_probe_v2.py        # Scapy-based network telemetry sniffer
├── face_auth.py            # Hardware camera trigger and local auth client
├── local_face_api.py       # FastAPI microservice for InsightFace embedding extraction
├── display_lcd.py          # I2C LCD hardware feedback controller
│
├── requirements.txt        # Python dependency list
├── .gitignore              # Ignored files (e.g., __pycache__, tokens, admin.jpg)
└── README.md               # Core project documentation
```

## ✨ Key Features
Dual-Bus Architecture: Decouples the computational Math Engine from the UI and Alerting services, ensuring high-availability monitoring without interface latency.
Automated Threat Interception (IPS): Dynamically interfaces with Linux iptables to block malicious IP addresses instantly upon threshold breaches.
AI Biometric Gateway: Utilizes NPU-accelerated InsightFace models to require physical administrative verification before activating probe sensors.
Interactive C2 Alerting: Integrates a Telegram Bot for real-time threat push notifications and remote command execution.
Hardware Telemetry Feedback: Provides physical status awareness through I2C LCD screens and GPIO-driven LED/Buzzer alerts.

## 🏗️Architecture 
The framework is designed using a decentralized, modular pattern separated into distinct operational planes:

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

<img width="600" height="400" alt="image" src="docs/Hardware.png" />
Provides physical status updates. It uses a **No-Clear-Write** methodology to update 20x4 LCD screens, preventing flickering and character garbage.

Key Code: 
```bash
`lcd.cursor_pos = (0, 0); lcd.write_string(lines[0][:20])`
```

### 2. Network Sniffer (`edge_probe_v2.py`)

<img width="600" height="400" alt="image" src="docs/Network_Sniffer.png" />
A Scapy-based sentinel that monitors `wlan0`. It aggregates packets and computes telemetry data locally before pushing it to the Math Engine.

Key Code: 
```bash
`sniff(iface=TARGET_INTERFACE, prn=packet_callback, store=0)`
```

### 3. Math Core Engine (Node-RED)

<img width="600" height="400" alt="image" src="docs/CoreMathEngine.png" />
The central intelligence. It calculates **Z-Score anomalies** to detect DDoS volumetric floods.

To identify DDoS flooding or anomalous bandwidth consumption, the Math Core Engine dynamically computes the Packets Per Second (PPS). Any traffic rate generating a Z-Score where |Z|>3.0 triggers the IPS Governor to inject immediate drop rules.


**Logic Definition**:
```bash
$$ Z = \frac{\text{currentPPS} - \mu}{\sigma} $$
```

### 4. Biometric Enrollment & Verification (`face_auth.py` & `local_face_api.py`)

<img width="600" height="400" alt="image" src="docs/BiometricEnrollment-Verification2.png" />
The system enforces strict biometric access control to prevent unauthorized tampering, utilizing the **InsightFace (antelopev2)** model to perform 1:1 cosine similarity matching.
*   **Key Code**: `sim = np.dot(emb1, emb2) / (norm1 * norm2)`

**A. Enrollment (Registration)**
To register the administrator, capture a reference image and save it to the system. Ensure the image is well-lit and clearly shows your face as it will serve as the unique authentication template. 
```bash
sudo rpicam-still -t 3000 --width 640 --height 480 -o /home/mj/admin.jpg
```

### 🛠️ Integrated Features
Telegram Integration (node-red-contrib-telegrambot)

![Telegram](docs/telegram.png)

Allows remote administration. It broadcasts DDoS alerts and accepts control commands like /on, /off, /reset, and /status via an interactive inline keyboard.

### Dashboard & Metrics (node-red-dashboard)
Provides a real-time digital twin of the network, synchronized across Threat Logs, All Traffic Logs, and Active Firewall Blocks tables, ensuring full network visibility.

### IPS & Dynamic Governor
Automatically injects iptables rules when a threat reaches a critical state. It features a heuristic hit-map system to distinguish between transient warnings and persistent attacks.

### 🔧 Deployment
Requirements: Raspberry Pi, Node-RED, InsightFace dependencies.
Setup AI Backend: Enable the background facial recognition microservice.

```Bash
nohup python3 /home/mj/local_face_api.py > api.log 2>&1 &
```
Flow Deployment: Import the provided flows.json and configure your chatId in the Telegram function nodes.

### 📸 Operational Visuals & Deployment
Dashboard & Metrics (node-red-dashboard)
Provides a real-time digital twin of the network, synchronized across Threat Logs, All Traffic Logs, and Active Firewall Blocks tables, ensuring full network visibility.
Telegram Integration (node-red-contrib-telegrambot)

Allows remote administration. It broadcasts DDoS alerts and accepts control commands like /on, /off, /reset, and /status via an interactive inline keyboard.

### 🚀 Installation & Setup
Prerequisites
	Hardware: Raspberry Pi (3B+ or higher recommended) with an active Camera Module.
	Operating System: Raspberry Pi OS with 8GB Swap memory enabled to prevent OOM termination.
	Node-RED Dependencies: dashboard, telegrambot, influxdb, pi-gpio, ui-table.

### Quick Start
Clone the repository:
```Bash
git clone [https://github.com/yourusername/SmartNet-Guard.git](https://github.com/yourusername/SmartNet-Guard.git)
cd SmartNet-Guard
```
	
### Start AI Backend: Ensure the recognition API is running as a background service:
```Bash
sudo python3 /home/mj/local_face_api.py > api.log 2>&1 &
```
### Register Administrator (Enrollment): Capture a reference image and save it to the system.
```Bash
sudo rpicam-still -t 3000 --width 640 --height 480 -o /home/mj/admin.jpg
```
### Flows: Import the provided flows.json and configure your chatId in the Telegram function nodes.
Verification (Access Check):

```Bash
sudo python3 /home/mj/face_auth.py
```
AUTHORIZED:mj: Access granted; probe and control services are enabled.
DENIED:UNKNOWN_FACE_SCORE_xx: Verification rejected due to low confidence.

## 🛡️ Scope & Limitations
### Traffic Capacity: Optimized for edge constraints. Extreme volumetric attacks exceeding the Raspberry Pi's NIC hardware limits may result in packet drop before analysis.
### Authentication Constraints: The facial recognition gateway requires adequate ambient lighting. Infrared (IR) capture is not supported in the base hardware configuration.
### Network Topology: Designed specifically as an edge-node sentinel rather than a centralized, distributed core network analyzer.

## 👨‍💻 Author
###Tan Minjun
###Bachelor of Information Technology (Honours) Communications and Networking, UTAR.
Networking Professional specializing in edge security and network visibility solutions.


