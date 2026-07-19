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


1. **关于照片标注**：如果您的 Dashboard 界面包含敏感数据（如真实的公共 IP），请记得在截屏后使用图片编辑工具（如画图、Snagit）遮挡住 IP 的后两位，这在任何开源项目中都是必须的“职业规范”。
2. **README 渲染**：将此代码保存为 `README.md` 上传到 GitHub，GitHub 会自动将 `|` 符号渲染成表格，并将 `#` 后的内容处理为标题，效果会非常专业。
3. **代码安全性**：在 GitHub 上发布代码时，一定要确保 `flows.json` 里没有任何真正的 Bot Token，否则会被扫描程序自动盗取！您可以将其替换为 `YOUR_BOT_TOKEN_HERE`。
