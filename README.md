# 🚀 Smart Community IoT Dryer System (Brisbane Project)

[![Maintenance](https://img.shields.io/badge/Maintenace-Zero--Cost-green.svg)](https://netlify.com)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Web-blue.svg)]()
[![Hardware](https://img.shields.io/badge/Hardware-Sonoff%20%7C%20eWeLink-orange.svg)]()

> **"Turning unauthorized utility usage into an automated, data-driven management tool."**

[cite_start]This end-to-end IoT solution was designed for a **48-unit residential community in Brisbane** to solve the pain points of "utility theft" (unauthorized usage) and the lack of cost-tracking transparency in shared laundry facilities. 

---

## 📸 System Preview
| User Portal (Mobile) | Admin Dashboard (Windows) |
|---|---|
| [Insert your resident.html screenshot here] | [Insert your Python app screenshot here] |
| *Residents register their usage via smartphone.* | *Management monitors live status & overrides power.* |

---

## 🎯 Business Value & Impact
* **💰 Zero Operational Expenditure (OPEX):** Engineered a high-availability infrastructure using **Serverless (GAS)** and **Netlify** to achieve **Zero-cost maintenance**. [cite_start]No server rental fees, ever. [cite: 61, 72]
* [cite_start]**⏰ 100% Automation in Finance:** Transformed a manual 2-hour monthly cost-tracking task into an instant, "Zero-second" automated data generation process. [cite: 67, 74]
* [cite_start]**🔒 Eliminated Misuse:** Prevented unauthorized API calls and system misuse through a custom 6-digit access code matrix and strict time-fence logic (06:00 - 21:00). [cite: 63, 64]

---

## 🛠️ The Technical "Moat" (Why it works better)

### 1. Hardware-Level Reliability (Inching Mode)
Unlike fragile cloud-based software timers, I utilized **Inching Mode** technology on the IoT hardware level.
* **The Result:** Even if the internet drops, the dryer **will accurately cut power after 3 hours**. [cite_start]Hardware certainty > Network dependency. [cite: 65, 66, 73]

### 2. High-Performance Admin Dashboard (Python)
A Windows-based management tool built with Python to provide real-time visibility.
* [cite_start]**Features:** Real-time monitoring, manual remote power overrides, and direct secure integration with Google Sheets API via GCP Service Account. [cite: 58, 69]

### 3. Lightweight User Portal (Web)
[cite_start]A mobile-first entry point built with **Tailwind CSS** and **Vanilla JS** for maximum compatibility across all resident smartphones. [cite: 56]

---

## 🏗️ System Architecture

1.  **User Entry:** Resident registers via `resident.html`.
2.  [cite_start]**Validation:** Google Apps Script checks credentials and current time. [cite: 63, 64]
3.  [cite_start]**Logging:** Valid entries are written to a secure Google Sheet. [cite: 67]
4.  [cite_start]**Hardware Trigger:** IFTTT Webhooks trigger the Sonoff physical switches. [cite: 59]
5.  [cite_start]**Admin Monitor:** Management views live activity and controls power via the Python Dashboard. [cite: 69]

---

## 📂 Project Structure
```text
├── /admin-dashboard     # Python (Tkinter) Windows management tool
├── /user-portal          # Responsive Web interface (deployed on Netlify)
├── /cloud-backend       # Google Apps Script (Logic & API)
└── README.md

⚖️ License
Copyright (c) 2026. All Rights Reserved. (Private/Commercial Project)
