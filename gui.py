import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from data_storage import DataStorage
from visualization import plot_bmi_trends
from datetime import datetime
from PIL import Image, ImageTk

class BMI_Calculator_GUI:
    def __init__(self, root, db):
        self.root = root
        self.root.title("BMI Calculator")
        self.db = db
        
        # Center window on screen
        self.center_window()
        
        # Variables to store user input
        self.weight_var = tk.DoubleVar()
        self.height_var = tk.DoubleVar()
        
        # Labels and Entries
        ttk.Label(self.root, text="Weight (kg):").grid(row=0, column=0, padx=10, pady=10)
        self.weight_entry = ttk.Entry(self.root, textvariable=self.weight_var)
        self.weight_entry.grid(row=0, column=1, padx=10, pady=10)
        
        ttk.Label(self.root, text="Height (m):").grid(row=1, column=0, padx=10, pady=10)
        self.height_entry = ttk.Entry(self.root, textvariable=self.height_var)
        self.height_entry.grid(row=1, column=1, padx=10, pady=10)
        
        # Calculate Button
        self.calculate_button = ttk.Button(self.root, text="Calculate BMI", command=self.calculate_bmi)
        self.calculate_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        # Result Label
        self.result_label = ttk.Label(self.root, text="")
        self.result_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        
        # Cartoon Image
        self.cartoon_image_label = tk.Label(self.root)
        self.cartoon_image_label.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # View History Button
        self.view_history_button = ttk.Button(self.root, text="View History", command=self.view_history)
        self.view_history_button.grid(row=5, column=0, columnspan=2, padx=10, pady=10)
        
        # Load initial cartoon image
        self.load_cartoon_image("default")

    def center_window(self):
        # Calculate window position to center it on the screen
        window_width = 400
        window_height = 400
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        
        # Set window geometry and update to ensure it stays centered
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        self.root.update_idletasks()

    def calculate_bmi(self):
        try:
            weight = self.weight_var.get()
            height = self.height_var.get()
            
            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Weight and height must be positive numbers.")
                return
            
            bmi = weight / (height ** 2)
            bmi_category = self.get_bmi_category(bmi)
            
            self.result_label.config(text=f"BMI: {bmi:.2f} ({bmi_category})")
            
            # Show cartoon image based on BMI category
            self.load_cartoon_image(bmi_category.lower())
            
            # Save data to storage
            self.db.insert_record(weight, height, bmi)
            
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
        
    def calculate_bmi(self):
        try:
            weight = self.weight_var.get()
            height = self.height_var.get()
            
            if weight <= 0 or height <= 0:
                messagebox.showerror("Error", "Weight and height must be positive numbers.")
                return
            
            bmi = weight / (height ** 2)
            bmi_category = self.get_bmi_category(bmi)
            
            self.result_label.config(text=f"BMI: {bmi:.2f} ({bmi_category})")
            
            # Show cartoon image based on BMI category
            self.load_cartoon_image(bmi_category.lower())
            
            # Save data to storage
            self.db.insert_record(weight, height, bmi)
            
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please enter numeric values.")
    
    def get_bmi_category(self, bmi):
        if bmi < 18.5:
            return "Underweight"
        elif 18.5 <= bmi < 25:
            return "Normal weight"
        elif 25 <= bmi < 30:
            return "Overweight"
        else:
            return "Obese"
    
    def view_history(self):
        records = self.db.get_all_records()
        plot_bmi_trends(records)
    
    def load_cartoon_image(self, category):
        try:
            # Define image paths based on BMI categories
            image_paths = {
                "underweight": "images/underweight.png",
                "normal weight": "images/normal.png",
                "overweight": "images/overweight.png",
                "obese": "images/obese.png",
                "default": "images/default.png"
            }
            
            # Load and display the image
            image_path = image_paths.get(category, image_paths["default"])
            image = Image.open(image_path)
            image = image.resize((200, 200), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(image)
            
            self.cartoon_image_label.configure(image=photo)
            self.cartoon_image_label.image = photo  # keep a reference
            
        except FileNotFoundError:
            messagebox.showerror("Error", "Image file not found.")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to load image: {str(e)}")

