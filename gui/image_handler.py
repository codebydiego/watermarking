from tkinter import filedialog
from PIL import Image, ImageTk

class ImageHandler:
    def __init__(self, image_label):
        self.image_label = image_label
        self.image = None
        self.tk_image = None

    def load_image(self):
        """Load an image file and display it."""
        file_path = filedialog.askopenfilename()
        if file_path:
            self.image = Image.open(file_path)
            self.display_image()

    def display_image(self):
        """Display the loaded image on the label."""
        if self.image:
            self.image.thumbnail((800, 600))
            self.tk_image = ImageTk.PhotoImage(self.image)
            self.image_label.config(image=self.tk_image)
            self.image_label.image = self.tk_image  # Keep a reference

    def display_watermarked_image(self, watermarked_image):
        """Display the watermarked image on the label."""
        self.tk_watermarked_image = ImageTk.PhotoImage(watermarked_image)
        self.image_label.config(image=self.tk_watermarked_image)
        self.image_label.image = self.tk_watermarked_image  # Keep a reference