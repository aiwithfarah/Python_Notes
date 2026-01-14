# Now, let's secure your code. This is a small but crucial check that distinguishes "scripts" from "modules."
# The Task:
# Define a function system_check() that prints "All systems go".
# Add the Execution Guard (if __name__ ...).
# Call the function inside the guard block.
# (This ensures that if someone imports your file, the check doesn't run automatically).

def system_check():

    print("All Systems Go!")


if __name__ == "__main__":
    system_check()
