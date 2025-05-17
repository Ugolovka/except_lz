from processing import DataProcessor

if __name__ == "__main__":
    input_file = 'var9.csv'
    processor = DataProcessor(input_file)    
    processor.read_dataframe()

    