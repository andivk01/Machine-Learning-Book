# script to extract all the images from the pdf of slides

import fitz
from PIL import Image

# Open the PDF file
pdf_file = "test.pdf"
out_dir = "out"
doc = fitz.open(pdf_file)

# Iterate through each page in the document
for page_num in range(doc.page_count):
    print("Doing page", page_num)
    page = doc[page_num]

    # Get a list of all the image elements on the page
    images = page.get_images()

    # Iterate through each image element and extract the image
    for image in images:
        xref = image[0]
        pix = fitz.Pixmap(doc, xref)
        try:
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            img.save(f"{out_dir}/p{page_num}_img{xref}.png")
        except:
            print(f"Could not save image {xref} on page {page_num}")