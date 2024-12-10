import streamlit as st
from fpdf import FPDF, HTMLMixin
import markdown2  # Converts Markdown to HTML
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import io

mermaid_js = "https://cdn.jsdelivr.net/npm/mermaid@latest/dist/mermaid.min.js"
 
class PDF(FPDF, HTMLMixin):
    pass


def render_mermaid_html(mermaid_code):
    """Generate HTML content to render Mermaid diagram."""
    html_content = f"""
        <html>
        <head>
            <script src="{mermaid_js}"></script>
        </head>
        <body>
            <div class="mermaid">{mermaid_code}</div>
            <script>
                mermaid.initialize({{ startOnLoad: true }});
            </script>
        </body>
        </html>
    """
    return html_content
 
 
def capture_mermaid_as_image(html_content):
    """Capture Mermaid diagram as an image using Selenium and headless Chromium."""
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--window-size=800x600")
 
    with webdriver.Chrome(options=chrome_options) as driver:
        driver.get("data:text/html;charset=utf-8," + html_content)
        driver.implicitly_wait(3)
        screenshot = driver.get_screenshot_as_png()
 
    return io.BytesIO(screenshot)
 
@st.cache_data 
def generate_combined_pdf(document_html, mermaid_image_buffer):
    """Generate a combined PDF with the technical spec and Mermaid diagram."""
    pdf = PDF()
    pdf.add_page()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
 
    # Add the technical specification content
    pdf.write_html(document_html)
 
    # Add a new page for the Mermaid diagram
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, "Mermaid Diagram", ln=True, align="C")
    pdf.image(mermaid_image_buffer, x=10, y=30, w=180)
 
    # Output PDF to memory
    pdf_buffer = io.BytesIO()
    pdf.output(pdf_buffer)
    pdf_buffer.seek(0)
    return pdf_buffer



def generate_pdf(html_content):
    """Generate a PDF from the LLM's response."""
    pdf = PDF()
    pdf.add_page()
    pdf.set_left_margin(10)
    pdf.set_right_margin(10)
 
    # Convert HTML to PDF using fpdf2
    pdf.write_html(html_content)
    with open("Document.pdf", "wb") as f:
        pdf.output(f)
 
 
def pdf_convertion_with_mermaid(document,mermaid_code):
    document_html = markdown2.markdown(document)
    
    html_content = render_mermaid_html(mermaid_code)
    # Capture the Mermaid diagram as an image
    mermaid_image_buffer = capture_mermaid_as_image(html_content)
 
    # Generate combined PDF when the button is clicked
    if st.button("Generate PDF"):
        # Generate the combined PDF
        pdf_buffer = generate_combined_pdf(document_html, mermaid_image_buffer)
 
        # Provide a download button for the combined PDF
        st.download_button(
            label="Download Document",
            data=pdf_buffer,
            file_name="Document.pdf",
            mime="application/pdf"
        )
        
        
        
        
def pdf_convertion(document):
    document_html = markdown2.markdown(document)
 
    # Display the content in Streamlit
    # st.markdown(document, unsafe_allow_html=True)
    # Generate PDF when the button is clicked
    
    if st.button("Generate PDF"):
        generate_pdf(document_html)  # Generate the PDF
       
        # Allow the user to download the PDF
        with open("Document.pdf", "rb") as f:
            pdf_file = f.read()
        st.download_button(
            label="Download Document",
            data=pdf_file,
            file_name="Document.pdf",
            mime="application/pdf"
        )
        

    
def main():
    st.title("Document Generator")
    document="Hi this is Gowtham."

    # Convert Markdown to HTML
    document_html = markdown2.markdown(document)
 
    # Display the content in Streamlit
    st.markdown(document, unsafe_allow_html=True)
 
    # Generate PDF when the button is clicked
    if st.button("Generate PDF"):
        generate_pdf(document_html)  # Generate the PDF
       
        # Allow the user to download the PDF
        with open("document.pdf", "rb") as f:
            pdf_file = f.read()
            
        st.download_button(
            label="Download Document",
            data=pdf_file,
            file_name="document.pdf",
            mime="application/pdf"
        )
 
if __name__ == "__main__":
    main()