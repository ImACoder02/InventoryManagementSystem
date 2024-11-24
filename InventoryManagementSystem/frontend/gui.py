import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from backend.db import Database


class InventoryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Inventory Management System")
        self.root.geometry("1920x1080")  # Set the width to 1440 and height to 1024
        self.root.resizable(True, True)  # Optional: Disable 
        self.root.configure(bg="#808080")
        self.db = Database()

        # Header Frame
        self.header_frame = tk.Frame(self.root, bg="#213A58", height=80)
        self.header_frame.pack(side="top", fill="x")  # Position at the top, full width
        self.header_frame.pack_propagate(False)  # Prevent resizing based on contents

        # Add a label inside the header frame
        header_label = tk.Label(
            self.header_frame, 
            text="INVENTORY MANAGEMENT SYSTEM", 
            bg="#213A58", 
            fg="white", 
            font=("Arial", 23, "bold")
        )
        header_label.pack(pady=20)


        # Input Frame
        self.header_input_frame = tk.Frame(self.root, bg="white", width=1480, height=650)
        self.header_input_frame.place(relx=0.5, rely=0.5, y=40, anchor="center")
        self.header_input_frame.pack_propagate(False)

        # UI Components
        self.product_name_label = tk.Label(self.header_input_frame, bg="white", font=("Arial", 15), text="Product Name")
        self.product_name_label.place(x=40, y=50, anchor="nw")
        self.product_name_entry = tk.Entry(self.header_input_frame, font=("Arial", 15), bg="#D9D9D9", width=27)
        self.product_name_entry.place(x=500, y=53, anchor="nw")

        self.category_label = tk.Label(self.header_input_frame, bg="white", font=("Arial", 15), text="Category")
        self.category_label.place(x=55, y=110, anchor="nw")
        self.category_entry = tk.Entry(self.header_input_frame, font=("Arial", 15), bg="#D9D9D9", width=27)
        self.category_entry.place(x=500, y=113, anchor="nw")

        self.price_label = tk.Label(self.header_input_frame, bg="white", font=("Arial", 15), text="Price")
        self.price_label.place(x=70, y=170, anchor="nw")
        self.price_entry = tk.Entry(self.header_input_frame, font=("Arial", 15), bg="#D9D9D9", width=27)
        self.price_entry.place(x=500, y=173, anchor="nw")

        self.stock_quantity_label = tk.Label(self.header_input_frame, bg="white", font=("Arial", 15), text="Stock Quantity")
        self.stock_quantity_label.place(x=40, y=230, anchor="nw")
        self.stock_quantity_entry = tk.Entry(self.header_input_frame, font=("Arial", 15), bg="#D9D9D9", width=27)
        self.stock_quantity_entry.place(x=500, y=233, anchor="nw")

        # Buttons and Listbox
        self.listbox_frame = tk.Frame(self.header_input_frame, bg="#D9D9D9", width=1400, height=325)
        self.listbox_frame.place(relx=0.5, rely=0.5, y=130, anchor="center")
        self.listbox_frame.pack_propagate(False)

        self.button_frame = tk.Frame(self.listbox_frame, bg="#D9D9D9")
        self.button_frame.pack(side="top", pady=10)

        self.add_button = tk.Button(self.button_frame, text="Add Product", command=self.add_product)
        self.add_button.grid(row=0, column=0, padx=10)

        self.update_button = tk.Button(self.button_frame, text="Update Product", command=self.update_product)
        self.update_button.grid(row=0, column=1, padx=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=0, column=2, padx=10)

        self.view_button = tk.Button(self.button_frame, text="View Inventory", command=self.view_inventory)
        self.view_button.grid(row=0, column=3, padx=10)

        self.product_listbox = tk.Listbox(self.listbox_frame, font=("Arial", 12), bg="white", height=14, width=150)
        self.product_listbox.place(relx=0.5, rely=0.5, y=10, anchor="center")



        # Listbox to display products
        self.product_listbox = tk.Listbox(self.listbox_frame, font=("Arial", 12), bg="white", height=14, width=150)
        self.product_listbox.place(relx=0.5, rely=0.5, y=10, anchor="center")  


        


    
        """
        # UI Components
        self.product_name_label = tk.Label(root, text="Product Name:")
        self.product_name_label.grid(row=0, column=0)
        self.product_name_entry = tk.Entry(root)self.product_name_entry = tk.Entry(root)
        self.product_name_entry.grid(row=0, column=1)

        self.category_label = tk.Label(root, text="Category:")
        self.category_label.grid(row=1, column=0)
        self.category_entry = tk.Entry(root)
        self.category_entry.grid(row=1, column=1)

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.grid(row=2, column=0)
        self.price_entry = tk.Entry(root)
        self.price_entry.grid(row=2, column=1)

        self.stock_quantity_label = tk.Label(root, text="Stock Quantity:")
        self.stock_quantity_label.grid(row=3, column=0)
        self.stock_quantity_entry = tk.Entry(root)
        self.stock_quantity_entry.grid(row=3, column=1)
        
        # Buttons
        self.add_button = tk.Button(root, text="Add Product", command=self.add_product)
        self.add_button.grid(row=4, column=0)

        self.update_button = tk.Button(root, text="Update Product", command=self.update_product)
        self.update_button.grid(row=4, column=1)

        self.delete_button = tk.Button(root, text="Delete Product", command=self.delete_product)
        self.delete_button.grid(row=5, column=0)

        self.view_button = tk.Button(root, text="View Inventory", command=self.view_inventory)
        self.view_button.grid(row=5, column=1)

        # Listbox to display products
        self.product_listbox = tk.Listbox(root, height=10, width=50)
        self.product_listbox.grid(row=6, column=0, columnspan=2)
        """
    
    
    def add_product(self):
        product_name = self.product_name_entry.get()
        category = self.category_entry.get()
        try:
            price = float(self.price_entry.get())
            stock_quantity = int(self.stock_quantity_entry.get())
            product_id = self.db.add_product(product_name, category, price, stock_quantity)
            messagebox.showinfo("Success", "Product added successfully!")
            self.view_inventory()  # Refresh the inventory list after adding the product
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")

    def update_product(self):
        try:
            selected_item = self.product_listbox.curselection()
            if selected_item:
                # Extract the product ID from the selected item
                product_text = self.product_listbox.get(selected_item)
                product_id = int(product_text.split(",")[0].split(":")[1].strip())  # Parse ID from text
                
                # Get updated product details from the entries
                product_name = self.product_name_entry.get()
                category = self.category_entry.get()
                price = float(self.price_entry.get())
                stock_quantity = int(self.stock_quantity_entry.get())
                
                # Call the database update method
                self.db.update_product(product_id, product_name, category, price, stock_quantity)
                messagebox.showinfo("Success", "Product updated successfully!")
                
                # Refresh the Listbox to reflect changes
                self.view_inventory()
            else:
                messagebox.showerror("No Selection", "Please select a product to update.")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid price and quantity.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during update: {e}")


    def delete_product(self):
        try:
            selected_item = self.product_listbox.curselection()
            if selected_item:
                # Extract the product ID from the selected item
                product_text = self.product_listbox.get(selected_item)
                product_id = int(product_text.split(",")[0].split(":")[1].strip())  # Parse ID from text
                
                # Call the database delete method
                self.db.delete_product(product_id)
                messagebox.showinfo("Success", "Product deleted successfully!")
                
                # Refresh the Listbox to reflect changes
                self.view_inventory()
            else:
                messagebox.showerror("No Selection", "Please select a product to delete.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during deletion: {e}")


    def view_inventory(self):
        inventory = self.db.fetch_products()
        self.product_listbox.delete(0, tk.END)  # Clear previous list
        for product in inventory:
            self.product_listbox.insert(tk.END, f"ID: {product[0]}, Name: {product[1]}, Category: {product[2]}, Price: ${product[3]:.2f}, Stock: {product[4]}")
    
if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()
