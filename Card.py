from PIL import Image
from qrcode import QRCode


class Card:
    @staticmethod
    def create_card(ship_id: str):
        # make qr image
        qr = QRCode(version=1, box_size=3.5, border=2)
        qr.add_data(ship_id)
        qr.make_image(fit=True)
        qr_image = qr.make_image(fill_color="black", back_color="white")
        # Open the two images
        card_template = Image.open("assets/card_template.png")
        # Define the location to overlay qr image onto the card
        x_offset = 467
        y_offset = 153
        # Resize the qr image
        new_width = 627
        new_height = 627
        qr_image_resized = qr_image.resize((new_width, new_height))
        # Create a new image the same size as the card
        result_image = card_template.copy()
        # Paste resized qr image onto the result image at the defined location
        result_image.paste(qr_image_resized, (x_offset, y_offset))
        # Save the result as PDF
        result_image.save(f"cards/{ship_id}.pdf", "PDF")
