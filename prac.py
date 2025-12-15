import math

# prac.py - simple square root calculator

def sqrt_of_number(x):
    if x < 0:
        raise ValueError("Cannot compute square root of a negative number")
    return math.sqrt(x)

def main():
    try:
        n = float(input("Enter a non-negative number: ").strip())
        print(f"Square root: {sqrt_of_number(n)}")
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
    
    