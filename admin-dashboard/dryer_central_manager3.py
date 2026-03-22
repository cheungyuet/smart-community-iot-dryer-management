import tkinter as tk
from tkinter import ttk, messagebox
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import requests
from datetime import datetime

# --- Configuration ---
SHEET_NAME = "Logs"
IFTTT_KEY = "您的_IFTTT_KEY"  # Replace with your actual IFTTT Key
JSON_FILE = "credentials.json" # Google API credentials filename

class DryerManager:
    def __init__(self, root):
        self.root = root
        self.root.title("BNE Dryer Management System")
        self.root.geometry("650x550")
        self.root.configure(bg="#f3f4f6")
        
        # Title
        title = tk.Label(
            root, 
            text="BNE Dryer Real-time Monitor", 
            font=("Segoe UI", 18, "bold"),
            bg="#f3f4f6",
            fg="#1f2937"
        )
        title.pack(pady=20)

        # Status Display Frame
        self.status_frame = tk.Frame(root, bg="#f3f4f6")
        self.status_frame.pack(pady=10)
        
        self.dryer_labels = {}
        # Define grid for 8 dryers (D01-D08)
        for i in range(1, 9):
            d_id = f"D0{i}"
            btn = tk.Button(
                self.status_frame, 
                text=f"{d_id}\nInitializing", 
                font=("Segoe UI", 10, "bold"),
                width=12, 
                height=3, 
                fg="white",
                bg="#9ca3af", 
                relief="flat",
                command=lambda id=d_id: self.force_trigger(id)
            )
            btn.grid(row=(i-1)//4, column=(i-1)%4, padx=8, pady=8)
            self.dryer_labels[d_id] = btn

        # Log Display Area
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))
        
        self.tree = ttk.Treeview(
            root, 
            columns=("Time", "Block", "Unit", "Dryer"), 
            show="headings", 
            height=8
        )
        self.tree.heading("Time", text="Timestamp")
        self.tree.heading("Block", text="Block")
        self.tree.heading("Unit", text="Unit No.")
        self.tree.heading("Dryer", text="Dryer ID")
        
        self.tree.column("Time", width=180, anchor="center")
        self.tree.column("Block", width=100, anchor="center")
        self.tree.column("Unit", width=100, anchor="center")
        self.tree.column("Dryer", width=100, anchor="center")
        self.tree.pack(pady=20, padx=20, fill=tk.X)

        # Button Area
        btn_refresh = tk.Button(
            root, 
            text="REFRESH DATA", 
            font=("Segoe UI", 10, "bold"),
            command=self.refresh_data, 
            bg="#2563eb", 
            fg="white",
            padx=20,
            pady=5,
            relief="flat"
        )
        btn_refresh.pack(pady=10)

        # Initial data load
        self.refresh_data()

    def refresh_data(self):
        try:
            # Connect to Google Sheets
            scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/drive']
            creds = ServiceAccountCredentials.from_json_keyfile_name(JSON_FILE, scope)
            client = gspread.authorize(creds)
            sheet = client.open(SHEET_NAME).worksheet("Logs")
            
            # Read last 10 records
            records = sheet.get_all_values()
            # Skip header, get last 10
            recent_logs = records[-10:] if len(records) > 10 else records[1:]
            
            # Update Treeview
            for item in self.tree.get_children():
                self.tree.delete(item)
            for row in reversed(recent_logs):
                # Ensure row has enough columns to prevent index errors
                if len(row) >= 4:
                    self.tree.insert("", tk.END, values=(row[0], row[1], row[2], row[3]))

            # Update Dryer Status UI
            # Logic: If Dryer ID appears in recent logs, consider it "Active"
            active_dryers = [row[3] for row in recent_logs]
            for d_id, btn in self.dryer_labels.items():
                if d_id in active_dryers:
                    btn.config(bg="#ef4444", text=f"{d_id}\nIN USE") # Red for busy
                else:
                    btn.config(bg="#10b981", text=f"{d_id}\nAVAILABLE") # Green for idle

        except Exception as e:
            messagebox.showerror("Connection Error", f"Failed to fetch data: {e}")

    def force_trigger(self, dryer_id):
        confirm = messagebox.askyesno(
            "Manual Override", 
            f"Do you want to manually trigger Power ON for {dryer_id}?"
        )
        if confirm:
            url = f"https://maker.ifttt.com/trigger/dryer_{dryer_id.lower()}_on/with/key/{IFTTT_KEY}"
            try:
                response = requests.post(url)
                if response.status_code == 200:
                    messagebox.showinfo("Success", f"Command sent to {dryer_id} successfully.")
                else:
                    messagebox.showwarning("Warning", f"Command sent, but server returned: {response.status_code}")
                self.refresh_data()
            except Exception as e:
                messagebox.showerror("Trigger Failed", f"Network error: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    # Apply a modern look if available
    try:
        root.tk.call('tk_setPalette', '#f3f4f6')
    except:
        pass
    app = DryerManager(root)
    root.mainloop()