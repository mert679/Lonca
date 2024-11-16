from utils.connection import get_mongo_connection
from utils.read_xml import read_xml_file
from utils.transform_product import transform_product

def main():
    """
    Main function to orchestrate the XML parsing, transformation, and MongoDB insertion.
    """
    
    parsed_data = read_xml_file()

    # Transform parsed data
    transformed_products = transform_product(parsed_data)
  
    # Connect to MongoDB
    db, collection = get_mongo_connection()

    # Insert transformed data into MongoDB
    for product in transformed_products:
        # Check if a product with the same stock_code and product_id already exists in the collection
        if not collection.find_one({"stock_code": product["stock_code"]}):
            collection.insert_one(product)
            print(f"Inserted product with stock code: {product['stock_code']}")
        else:
            print(f"Product with stock code {product['stock_code']} already exists.")

if __name__ == "__main__":
    main()



