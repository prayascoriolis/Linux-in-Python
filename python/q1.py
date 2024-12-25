import pandas as pd
import os
import random

def read_n_write_csv(file_path):
    try:
        # Check if the file exists
        if os.path.exists(file_path):
            print("Reading existing CSV file:")
            # Read the existing CSV file using pandas
            df = pd.read_csv(file_path)
            print(df)
        else:
            print(f"File does not exist. A new file will be created.")
        new_data = {
            "Frame": 1,
            "Visibility": 0,
            "X": f"{random.uniform(0, 100):.2f}",
            "Y": f"{random.uniform(0, 100):.2f}"
        }
        new_df = pd.DataFrame(new_data, index=[0])
        # Append the new data to the existing file or create a new one
        if os.path.exists(file_path):
            new_df.to_csv(file_path, mode='a', index=False, header=False)
        else:
            new_df.to_csv(file_path, index=False)
        print(f"New data added to file")
    except Exception as e:
        print('ERROR: ',e)

if __name__ == "__main__":
    file_path = "./dir/black.csv"
    read_n_write_csv(file_path)