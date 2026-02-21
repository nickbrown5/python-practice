import sys

def main():
    if len(sys.argv) < 2:
        print("Please pass at least one argument.")
        return
    
    for arg in sys.argv[1:]:
        print(f"Argument: {arg}")

if __name__ == "__main__":
    main()
