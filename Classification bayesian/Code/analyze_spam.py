import csv
import re
from collections import Counter

def get_stop_words():
    # Basic list of English stop words since nltk is not available
    return {
        'i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", 
        "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 
        'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 
        'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 
        'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 
        'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 
        'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 
        'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 
        'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 
        'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 
        'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 
        'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 
        'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 
        'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 
        've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 
        'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 
        'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 
        'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 
        'won', "won't", 'wouldn', "wouldn't", "u", "ur", "4", "2"
    }

def preprocess_text(text, stop_words):
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation using regex (keep only letters and numbers)
    # Using a simple regex to extract words
    words = re.findall(r'\b\w+\b', text)
    # Remove stop words
    return [word for word in words if word not in stop_words]

def analyze_spam(file_path):
    stop_words = get_stop_words()
    
    spam_words = Counter()
    ham_words = Counter()
    
    try:
        with open(file_path, mode='r', encoding='latin-1') as f:
            # Inspection showed v1,v2 structure, likely CSV with header
            reader = csv.reader(f)
            header = next(reader, None) # Skip header if present
            
            # Check if header looks right, otherwise might need to adjust
            # Based on `head` output: v1,v2,,,
            
            for row in reader:
                if len(row) < 2:
                    continue
                    
                label = row[0]
                message = row[1]
                
                words = preprocess_text(message, stop_words)
                
                if label.lower() == 'spam':
                    spam_words.update(words)
                else:
                    ham_words.update(words)
                    
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}")
        return
    except Exception as e:
        print(f"Error reading file: {e}")
        return

    # Calculate statistics and probabilities
    
    def print_top_words(counter, label_name):
        total_words = sum(counter.values())
        print(f"\n--- {label_name} Analysis ---")
        print(f"Total words: {total_words}")
        
        top_2 = counter.most_common(2)
        if not top_2:
            print("No words found.")
            return
            
        print("Top 2 Non-Stop Words and their Probabilities:")
        for word, count in top_2:
            prob = count / total_words
            print(f"  Word: '{word}' | Count: {count} | Probability: {prob:.6f}")

    print_top_words(spam_words, "Spam")
    print_top_words(ham_words, "Non-Spam (Ham)")

    # Save frequencies to a file as requested ("create a file that shows the frequency")
    output_file = '/home/oussama/Desktop/aed_project/word_frequencies.csv'
    try:
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(['Label', 'Word', 'Count', 'Probability'])
            
            # Spam
            total_spam = sum(spam_words.values())
            for word, count in spam_words.most_common():
                writer.writerow(['spam', word, count, count/total_spam])
                
            # Ham
            total_ham = sum(ham_words.values())
            for word, count in ham_words.most_common():
                writer.writerow(['ham', word, count, count/total_ham])
                
        print(f"\nFull frequency data saved to: {output_file}")
    except Exception as e:
        print(f"Error writing output file: {e}")

if __name__ == "__main__":
    analyze_spam('/home/oussama/Desktop/aed_project/spam.csv')
