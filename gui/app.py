import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image, ImageTk, ImageDraw, ImageFont
from gui.image_handler import ImageHandler
from utils.watermark import apply_text_watermark

class WatermarkApp:
    def __init__(self, master):
        """Initialize the main application window."""
        self.master = master
        master.title("Watermark Application")
        self.master.attributes('-fullscreen', True)  # Hacer la ventana a pantalla completa

        # Frame for buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(side=tk.TOP, fill=tk.X)

        # Frame for centering buttons
        self.center_frame = tk.Frame(self.button_frame)
        self.center_frame.pack(side=tk.TOP)

        # Load Image Button
        self.load_button = tk.Button(self.center_frame, text="Load Image", command=self.load_image)
        self.load_button.pack(side=tk.LEFT, padx=5, pady=5)

        # TextBox for watermark text
        self.watermark_text = tk.Text(master, height=1, width=30)
        self.watermark_text.pack(side=tk.TOP, padx=10, pady=10)
        self.watermark_text.insert(tk.END, "Sample Watermark")

        # Apply Watermark Button
        self.watermark_button = tk.Button(self.center_frame, text="Apply Watermark", command=self.apply_watermark)
        self.watermark_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Save Image Button
        self.save_button = tk.Button(self.center_frame, text="Save Image", command=self.save_image)
        self.save_button.pack(side=tk.LEFT, padx=5, pady=5)

        # Label for displaying image
        self.image_label = tk.Label(master)
        self.image_label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        self.image_handler = ImageHandler(self.image_label)
        self.watermarked_image = None

    def load_image(self):
        self.image_handler.load_image()

    def apply_watermark(self):
        """Apply a watermark to the loaded image."""
        if self.image_handler.image:
            watermark_text = self.watermark_text.get("1.0", tk.END).strip()
            self.watermarked_image = apply_text_watermark(self.image_handler.image.copy(), watermark_text)
            self.image_handler.display_watermarked_image(self.watermarked_image)

    def save_image(self):
        """Save the watermarked image to a file."""
        if self.watermarked_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png")
            if file_path:
                self.watermarked_image.save(file_path)
                messagebox.showinfo("Image Saved", "The image has been saved successfully.")
