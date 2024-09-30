import unittest
from PIL import Image
from utils.watermark import apply_text_watermark

class TestWatermark(unittest.TestCase):
    def setUp(self):
        """Create a test image before each test."""
        self.image = Image.new("RGB", (200, 200), color=(255, 255, 255))

    def test_apply_text_watermark(self):
        """Test that checks if the function can apply a text watermark."""
        watermarked_image = apply_text_watermark(self.image.copy(), "Test Watermark")
        self.assertIsInstance(watermarked_image, Image.Image)

    def test_text_watermark_position(self):
        """Verify that the watermark is drawn in the correct position."""
        text = "Test Position"
        watermarked_image = apply_text_watermark(self.image.copy(), text)
        self.assertTrue(self._is_watermark_applied(watermarked_image), "The watermark was not applied to the expected area.")

    def test_apply_text_with_default_font(self):
        """Check that the function applies the watermark with a default font if the specified font is not found."""
        watermarked_image = apply_text_watermark(self.image.copy(), "Test Default Font", font_path="non_existent_font.ttf")
        self.assertIsInstance(watermarked_image, Image.Image)

    def tearDown(self):
        """Clean up resources after each test (optional)."""
        self.image.close()

    def _is_watermark_applied(self, image):
        """Helper method to check if watermark is applied in the expected area."""
        for x in range(150, 200):
            for y in range(150, 200):
                if image.getpixel((x, y)) != (255, 255, 255):
                    return True
        return False

if __name__ == "__main__":
    unittest.main()
