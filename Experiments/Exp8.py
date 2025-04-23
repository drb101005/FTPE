import re
import sys

def handle_file():
    filename = input("Enter filename (default: words.txt): ") or "words.txt"
    if '.' not in filename:
        filename += ".txt"
    
    try:
        # Write sample content
        with open(filename, "w") as f:
            f.write("This file contains words of various lengths like cat dog apple banana")
        
        # Get length filters
        lengths = list(map(int, input("Enter lengths to find (comma-separated): ").split(',')))
        
        # Read and filter words
        with open(filename) as f:
            words = re.findall(r'\w+', f.read())
            for l in lengths:
                matches = [w for w in words if len(w) == l]
                print(f"{l}-letter words:", matches)
                
    except PermissionError:
        print("Error: Cannot access file")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    handle_file()
    input("Press Enter to exit...")