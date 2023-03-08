import PyPDF2

file_name = "Slides_fifth_block_D_ensemble_learning"

# Open the PDF file
pdf_file = open('D:\\Download\\' + file_name + '.pdf', 'rb')

# Create a PDF reader object
pdf_reader = PyPDF2.PdfReader(pdf_file)

# Get the number of pages in the PDF file
num_pages = len(pdf_reader.pages)

# Open a new text file for writing
text_file = open('C:\\Users\\andre\\Desktop\\extracted\\' + file_name + '.txt', 'w')

# Loop through each page in the PDF file
for page in range(num_pages):
    # Get the text from the current page
    page_text = pdf_reader.pages[page].extract_text()

    # remove non-unicode characters
    page_text = page_text.encode('ascii', 'ignore').decode('ascii')
    try:
        n_imgs = len(pdf_reader.pages[page].images)
    except:
        n_imgs = 0
    # if not (page>=100 and page<152):
    #     continue

    page_text = "Page " + str(page) + " with " + str(n_imgs) + ' images \n' + page_text.strip() + '\n\n'
    text_file.write(page_text)
        
    
# Close the PDF file and the output file
pdf_file.close()
text_file.close()
