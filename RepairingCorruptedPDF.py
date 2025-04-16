import pikepdf

def repair_pdf(input_path, output_path):
    try:
        # Attempt to open the corrupted PDF file
        with pikepdf.open(input_path) as pdf:
            # Save the repaired PDF to a new file
            pdf.save(output_path)
        print(f"Recovery successful. Data saved to '{output_path}'.")
    except pikepdf.PdfError as e:
        # Print the error message if opening the PDF fails
        print(f"An error occurred: {e}")

# Usage
repair_pdf('corrupted_file.pdf', 'repaired_file.pdf')
    
