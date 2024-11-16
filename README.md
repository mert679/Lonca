# Product Insertion to MongoDB

## Features
1. XML File Parsing: Reads product data from an XML file.
2. Data Transformation: Transforms the parsed XML data into a structure suitable for insertion into MongoDB.
3. MongoDB Connection: Connects to MongoDB using credentials stored in a configuration file.
4. Duplicate Check: Ensures no duplicate products with the same stock_code is inserted into the database.
5. Error Handling: Stops the insertion process and raises an error if duplicate products are found.


## Table of Contents

- [Cloning the Project](#cloning-the-project)
- [Installing Dependencies](#installing-dependencies)
- [Adjusting Configuration File](#adjusting-configuration-file)
- [How the Program Works](#how-the-program-works)
- [Modules and Functions](#modules-and-functions)
- [Running the Program](#running-the-program)

## Cloning the Project

To get started, you need to clone the repository. Follow these steps:

1. Open your terminal or command prompt.
2. Clone the project by running the following command:

   ```bash
   git clone https://github.com/mert679/Lonca.git
   ```

## Installing Dependencies
 Create and activate a virtual environment and then install dependency
 
  ```bash
     python -m venv venv
     source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
     pip install -r requirements.txt   #Install dependency.
  ```

## Adjusting configuration file
1. create and open the config.json file.
2. create the following fields with your MongoDB connection details:
   
  ```bash
    {
      "username": "your-mongodb-username",
      "password": "your-mongodb-password",
      "database": "your-database-name",
      "collection": "your-collection-name"
  }
  ```
username: Your MongoDB username.
password: Your MongoDB password.
database: The name of the database you want to use.
collection: The name of the collection within the database where the product data will be stored.
save config.json file.



## How the Program Works

The program works in the following steps:

### 1. Database Connection
The program connects to MongoDB using the credentials specified in the `config.json` file.

### 2. XML Parsing
The program reads the product data from an XML file (`lonca-sample.xml`), parsing it into a Python dictionary.

### 3. Transformation
The XML data is transformed into a consistent format suitable for insertion into the MongoDB collection. During transformation:
- The `stock_code` is checked to ensure no duplicate records are inserted.
- The program capitalizes product names, calculates prices, and determines whether a product is discounted.

### 4. Insertion
The program inserts the transformed product data into the MongoDB collection. If the  `stock_code` already exists, the program will not insert a duplicate record.



## Modules and Functions

### 1. `connection.py`
This module is responsible for connecting to MongoDB.

- **Function**: `get_mongo_connection(config_file="config.json")`
  - **Arguments**: Path to the configuration file (default is `config.json`).
  - **Returns**: MongoDB database and collection objects.
  - **Usage**: Establishes a connection to MongoDB and returns the database and collection objects for further operations.


### 2. `parce_cdata.py`
This module is responsible for parsing the cdata.

- **Function**: `extract_measurements(description)`
  - **Arguments**: description (str): Product description as HTML string.
  - **Returns**: Extracted fabric, model measurements, and product measurements.
  - **Usage**: Reads the html string and parses it into a Python dictionary for further processing.


### 3. `read_xml.py`
This module is responsible for parsing the XML file and extracting product data.

- **Function**: `read_xml_file(file_path)`
  - **Arguments**: The path to the XML file.
  - **Returns**: Parsed XML data as a Python dictionary.
  - **Usage**: Reads the XML file and parses it into a Python dictionary for further processing.

### 4. `transform_product.py`
This module is responsible for transforming the parsed data into the format required for MongoDB.

- **Function**: `transform_product(parsed_data)`
  - **Arguments**: A single product entry from the parsed XML data.
  - **Returns**: A dictionary representing the transformed product data ready for insertion into MongoDB.
  - **Usage**: Processes a product, ensuring that product names are capitalized, prices are calculated, and duplicate checks are performed.

### 5. `lonca.py`
The entry point of the program. It ties everything together.

- **Function**: `main()`
  - **Usage**: Loads the configuration, establishes a connection to MongoDB, reads and parses the XML file, transforms the data, and inserts the transformed data into MongoDB.

## Running the Program

Once the dependencies are installed and the configuration file is adjusted, you can run the program as follows:

1. Ensure your MongoDB instance is running and accessible.
2. Run the program using the following command:

  ```bash
    python lonca.py
  ```

