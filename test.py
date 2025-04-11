from PIL import Image, ImageDraw, ImageFont


def generate_mock_loan_form_image(path="sample_loan_form.jpg"):
    # Create blank white image
    img = Image.new('RGB', (800, 400), color='white')
    draw = ImageDraw.Draw(img)

    # Use system default font
    font = ImageFont.load_default()

    # Draw sample text onto image
    text = """Loan Application Form

Name: Somsri Jaidee
National ID: 1234567890123
Loan Amount: 80000 Baht
Interest Rate: 3.5%
Status: On-time
"""
    draw.multiline_text((50, 50), text, fill=(0, 0, 0), font=font, spacing=8)

    # Save image
    img.save(path)
    print(f"✅ Mock image saved at: {path}")

if __name__ == "__main__":
    generate_mock_loan_form_image()
