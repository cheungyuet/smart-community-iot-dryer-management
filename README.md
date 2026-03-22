# 🚀 Smart Community IoT Dryer System (Brisbane Project)

[![Maintenance](https://img.shields.io/badge/Maintenace-Zero--Cost-green.svg)](https://netlify.com)
[![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Web-blue.svg)]()
[![Hardware](https://img.shields.io/badge/Hardware-Sonoff%20%7C%20eWeLink-orange.svg)]()

> **"Transforming unauthorized utility usage into a self-sustaining, zero-cost management ecosystem."**

This project provides an end-to-end IoT solution for a **48-unit residential community in Brisbane** to resolve long-standing issues with unauthorized utility usage and manual billing overhead.

---

## 📸 System Architecture & Interface


| Resident Portal (Mobile-First) | Admin Central Monitor (Windows) |
|---|---|
| (<img width="375" height="661" alt="image" src="https://github.com/user-attachments/assets/1dfaac28-8444-4754-910b-3e9d6177073f"/>
) | (<img width="643" height="574" alt="image" src="https://github.com/user-attachments/assets/a3f3608a-ea6c-47e0-a1cf-db7c3a2f4b8c"/>
) |
| [cite_start]*Residents register via `resident.html` [cite: 10]* | [cite_start]*Live monitoring via `dryer_central_manager3.py` [cite: 8]* |

---

## 💎 Business Value & Operational Impact
**💰 Zero OPEX Strategy:** Engineered the entire infrastructure using **Google Apps Script (GAS)** and **Netlify**, achieving a high-availability platform with **$0 monthly server costs**.

**⚡ 100% Billing Automation:** Eliminated manual auditing by automating usage logs into Google Sheets, enabling instant weekly/monthly financial forecasting.

**🔒 Security by Design:** Implemented a **6-digit Access Code Matrix** and backend **time-fence logic (06:00-21:00)** to strictly prevent system misuse and unauthorized API triggers.

---

## 🛠️ The Technical "Moat" (Engineering Excellence)

### 1. Hardware-Level Reliability (Inching Mode)
I prioritized **Hardware Certainty** over **Network Dependency**. [cite_start]By utilizing the IoT device's **Inching Mode** for the 3-hour timer, the dryer is guaranteed to cut power physically even if the local Wi-Fi or cloud connection drops mid-cycle.

### 2. Scalable Data Management
**Centralized Logging:** All transactions are handled via a RESTful API (GAS) that syncs directly with a Google Sheet "Logs" database[cite: 8, 9, 10].

**Secure Admin Access:** The Python-based dashboard uses **GCP Service Account (JSON)** for secure, server-side data retrieval, keeping management functions isolated from public access[cite: 8, 9].

---

## 📂 Project Structure
**`/admin-dashboard`**: Python (Tkinter) central monitor for property managers[cite: 8, 10].

**`/user-portal`**: Responsive HTML5/Tailwind entry point for residents[cite: 10].

**`/cloud-backend`**: Google Apps Script logic for validation and hardware triggering.

---

## ⚖️ License
Copyright (c) 2026. All Rights Reserved. (Private/Commercial Project) [cite_start][cite: 1, 2]
