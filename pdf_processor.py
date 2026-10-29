"""
Utility for processing and extracting text from uploaded PDFs or raw paste input.
"""

import io
from typing import Tuple, Optional
import pypdf

def extract_text_from_pdf(file_bytes: bytes) -> Tuple[str, int, Optional[str]]:
    """
    Extracts text cleanly from PDF bytes.
    Returns: (extracted_text, page_count, error_message)
    """
    try:
        pdf_file = io.BytesIO(file_bytes)
        reader = pypdf.PdfReader(pdf_file)
        
        if reader.is_encrypted:
            try:
                reader.decrypt("")
            except Exception:
                return "", 0, "The PDF file is encrypted and password-protected."
                
        num_pages = len(reader.pages)
        extracted_pages = []
        
        for idx, page in enumerate(reader.pages):
            page_text = page.extract_text() or ""
            if page_text.strip():
                extracted_pages.append(f"--- [Page {idx + 1}] ---\n{page_text.strip()}")
                
        full_text = "\n\n".join(extracted_pages)
        if not full_text.strip():
            return "", num_pages, "No readable text found in PDF. It might contain only scanned images or rasterized pages."
            
        return clean_text(full_text), num_pages, None
    except Exception as e:
        return "", 0, f"Error reading PDF: {str(e)}"

def clean_text(text: str) -> str:
    """Sanitizes text by stripping excessive whitespace and formatting artifacts."""
    lines = [line.strip() for line in text.split("\n")]
    # Remove empty line runs
    cleaned = []
    prev_empty = False
    for line in lines:
        if not line:
            if not prev_empty:
                cleaned.append("")
                prev_empty = True
        else:
            cleaned.append(line)
            prev_empty = False
    return "\n".join(cleaned).strip()
