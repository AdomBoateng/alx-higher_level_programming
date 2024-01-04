#!/usr/bin/python3
def main():
    import sys

# Get the arguments list
    arguments = sys.argv

# Print the number of arguments
    if len(arguments) == 1:
        print("Argument:", end="")
    else:
        print("Arguments:", len(arguments), end="")

# Print the arguments (if any)
    if len(arguments) > 1:
        print("s:", end="")
    for i, argument in enumerate(arguments[1:]):
        print(f"\n{i + 1}: {argument}")

# Add a newline at the end
    print()

if __name__ == "__main__":
    main()
