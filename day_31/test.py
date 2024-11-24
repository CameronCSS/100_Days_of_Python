import chardet
import pandas as pd
import os

pwd = os.getcwd()

# Test different encodings to see what japanese characters are reading as
with open(f"{pwd}\\data\\japanese_words.csv", 'rb') as file:
    raw_data = file.read()
    result = chardet.detect(raw_data)
    print(f"Detected encoding: {result}")

# Try some additional encodings:
encodings_to_try = [
    'utf-8-sig',  # UTF-8 with BOM
    'iso-2022-jp',  # Another Japanese encoding
    'euc-jp',      # Extended Unix Code for Japanese
    'utf-16-le',   # UTF-16 Little Endian
    'utf-16-be'    # UTF-16 Big Endian
]

for encoding in encodings_to_try:
    try:
        print(f"Trying {encoding}...")
        words_df = pd.read_csv(f"{pwd}\\data\\japanese_words.csv", encoding=encoding)
        print(f"Success with {encoding}!")
        break
    except Exception as e:
        print(f"Failed with {encoding}: {str(e)}\n")
        
        
        
# Success with utf-16-le!