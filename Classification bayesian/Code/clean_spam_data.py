import csv
import re
import sys

def clean_text(text):
    # 1. Lowercase
    text = text.lower()
    
    # 2. Remove all non-a-z characters (replace with space to avoid merging words)
    text = re.sub(r'[^a-z\s]', ' ', text)
    
    # 3. Remove specific artifacts (gt, lt)
    # Using \b to ensure we match whole words
    text = re.sub(r'\b(gt|lt)\b', ' ', text)
    
    # 4. Remove extra spaces
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def process_spam_file(input_file, output_file):
    try:
        with open(input_file, mode='r', encoding='latin-1') as infile, \
             open(output_file, mode='w', newline='', encoding='utf-8') as outfile:
            
            reader = csv.reader(infile)
            writer = csv.writer(outfile)
            
            header = next(reader, None)
            if header:
                # Append new column name
                new_header = header + ['cleaned_text']
                writer.writerow(new_header)
            
            processed_count = 0
            for row in reader:
                if len(row) < 2:
                    continue
                
                # Assuming message is the second column (v2) based on previous inspection
                # row[0] is label, row[1] is message
                original_text = row[1] 
                cleaned = clean_text(original_text)
                
                new_row = row + [cleaned]
                writer.writerow(new_row)
                processed_count += 1
                
        print(f"Successfully processed {processed_count} messages.")
        print(f"Cleaned data saved to: {output_file}")
        
    except FileNotFoundError:
        print(f"Error: Input file not found at {input_file}")
    except Exception as e:
        print(f"Error processing file: {e}")

if __name__ == "__main__":
    input_csv = '/home/oussama/Desktop/aed_project/spam.csv'
    output_csv = '/home/oussama/Desktop/aed_project/spam_cleaned.csv'
    
    process_spam_file(input_csv, output_csv)
