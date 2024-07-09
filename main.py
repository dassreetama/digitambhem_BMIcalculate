import tkinter as tk
from gui import BMI_Calculator_GUI
from data_storage import DataStorage
from visualization import plot_bmi_trends

def main():
    # Initialize DataStorage
    db = DataStorage()
    
    # Initialize GUI
    root = tk.Tk()
    app = BMI_Calculator_GUI(root, db)
    root.mainloop()
    
    # Close database connection when GUI is closed
    db.close_connection()

if __name__ == "__main__":
    main()
