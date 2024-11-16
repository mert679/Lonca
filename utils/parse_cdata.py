from bs4 import BeautifulSoup

def extract_measurements(description):
    """
    Extract measurements and fabric details from the description.
    Args:
        description (str): Product description as HTML string.
    Returns:
        dict: Extracted fabric, model measurements, and product measurements.
    """
    
    soup = BeautifulSoup(description, "html.parser")
    fabric = model_measurements = product_measurements = ""

    for li in soup.find_all("li"):
        text = li.get_text(strip=True)
        if "Kumaş Bilgisi" in text:
            fabric = text.replace("Kumaş Bilgisi:", "").strip()
        elif "Model Ölçüleri" in text:
            model_measurements = text.replace("Model Ölçüleri:", "").strip()
        elif "Ürün Ölçüleri" in text:
            product_measurements = text.replace("Ürün Ölçüleri:", "").strip()
    
    return {
        "fabric": fabric,
        "model_measurements": model_measurements,
        "product_measurements": product_measurements,
    }
