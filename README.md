# 🚀 Smart Community IoT Dryer System (Brisbane Project)

[![Maintenance](https://img.shields.io/badge/Maintenace-Zero--Cost-green.svg)](https://netlify.com)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Web-blue.svg)]()
[![Hardware](https://img.shields.io/badge/Hardware-Sonoff%20%7C%20eWeLink-orange.svg)]()

> **"Transforming unauthorized utility usage into a self-sustaining, zero-cost management ecosystem."**

[cite_start]This project provides an end-to-end IoT solution for a **48-unit residential community in Brisbane** to resolve long-standing issues with unauthorized utility usage and manual billing overhead.

---

## 📸 System Architecture & Interface


| Resident Portal (Mobile-First) | Admin Central Monitor (Windows) |
|---|---|
| ![Mobile View](https://via.placeholder.com/300x500?text=Resident+Portal+Screenshot) | ![Admin View](https://via.placeholder.com/500x300?text=Python+Admin+Dashboard+Screenshot) |
| [cite_start]*Residents register via `resident.html` [cite: 10]* | [cite_start]*Live monitoring via `dryer_central_manager3.py` [cite: 8]* |

---

## 💎 Business Value & Operational Impact
* [cite_start]**💰 Zero OPEX Strategy:** Engineered the entire infrastructure using **Google Apps Script (GAS)** and **Netlify**, achieving a high-availability platform with **$0 monthly server costs**.
* [cite_start]**⚡ 100% Billing Automation:** Eliminated manual auditing by automating usage logs into Google Sheets, enabling instant weekly/monthly financial forecasting.
* [cite_start]**🔒 Security by Design:** Implemented a **6-digit Access Code Matrix** and backend **time-fence logic (06:00-21:00)** to strictly prevent system misuse and unauthorized API triggers.

---

## 🛠️ The Technical "Moat" (Engineering Excellence)

### 1. Hardware-Level Reliability (Inching Mode)
I prioritized **Hardware Certainty** over **Network Dependency**. [cite_start]By utilizing the IoT device's **Inching Mode** for the 3-hour timer, the dryer is guaranteed to cut power physically even if the local Wi-Fi or cloud connection drops mid-cycle.

### 2. Scalable Data Management
* [cite_start]**Centralized Logging:** All transactions are handled via a RESTful API (GAS) that syncs directly with a Google Sheet "Logs" database[cite: 8, 9, 10].
* [cite_start]**Secure Admin Access:** The Python-based dashboard uses **GCP Service Account (JSON)** for secure, server-side data retrieval, keeping management functions isolated from public access[cite: 8, 9].

---

## 📂 Project Structure
* [cite_start]**`/admin-dashboard`**: Python (Tkinter) central monitor for property managers[cite: 8, 10].
* [cite_start]**`/user-portal`**: Responsive HTML5/Tailwind entry point for residents[cite: 10].
* [cite_start]**`/cloud-backend`**: Google Apps Script logic for validation and hardware triggering.

---

## ⚖️ License
Copyright (c) 2026. All Rights Reserved. (Private/Commercial Project) [cite_start][cite: 1, 2]
