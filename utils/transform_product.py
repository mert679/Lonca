from datetime import datetime
from utils  import parse_cdata

def transform_product(parsed_data):
    """
    Transforms the parsed XML data into a desired format.
    Args:
        parsed_data (dict): Parsed XML data.
    Returns:
        list: Transformed product data as a list of dictionaries.
    """
    try:
        products = parsed_data.get("Products", {}).get("Product", [])
        if not isinstance(products, list):
            products = [products]

        transformed_products = []
        for product in products:
            product_id = product.get("@ProductId")
            name = product.get("@Name", "").capitalize()
            images = [img["@Path"] for img in product.get("Images", {}).get("Image", [])]
            details = {d["@Name"]: d["@Value"] for d in product.get("ProductDetails", {}).get("ProductDetail", [])}
            
            # Extract measurements and other details from Description
            description = product.get("Description", "")
            measurements = parse_cdata.extract_measurements(description)

            price = float(details.get("Price", "0").replace(",", "."))
            discounted_price = float(details.get("DiscountedPrice", "0").replace(",", "."))
            is_discounted = discounted_price < price
            quantity = int(details.get("Quantity", "0"))

            transformed_products.append({
                "stock_code": product_id,
                "name": name,
                "color": [details.get("Color", "N/A")],
                "discounted_price": discounted_price,
                "is_discounted": is_discounted,
                "price": price,
                "price_unit": "USD",
                "images": images,
                "product_type": details.get("ProductType", "N/A"),
                "quantity": quantity,
                "sample_size": details.get("Size", "N/A"),
                "series": details.get("Series", ""),
                "status": "Active" if quantity > 0 else "Out of Stock",
                "fabric": measurements["fabric"],
                "model_measurements": measurements["model_measurements"],
                "product_measurements": measurements["product_measurements"],
                "createdAt": datetime.now().isoformat(),
                "updatedAt": datetime.now().isoformat(),
            })

        return transformed_products

    except Exception as e:
        print(f"Error: Failed to transform product data: {e}")
        return []

