import xmltodict
def read_xml_file(file="lonca-sample.xml" ):
    """
    Reads XML data from a file.
    
    Args:
        file_path (str): Path to the XML file.
        
    Returns:
        dict: Parsed XML data.
    """
    lonca_sample = file

    try:
        # Open file with UTF-8 encoding
        with open(lonca_sample, 'r', encoding='utf-8') as sample:
            xml_data = sample.read()
    except FileNotFoundError:
        print(f"File {lonca_sample} not found. Please provide a valid file path.")
        exit()
    except UnicodeDecodeError as e:
        print(f"Error decoding file {lonca_sample}: {e}")
        exit()

    try:
        # Parse XML data
        parsed_data = xmltodict.parse(xml_data)
    
    except Exception as e:
        print(f"Error parsing XML data: {e}")
        exit()
    return parsed_data

