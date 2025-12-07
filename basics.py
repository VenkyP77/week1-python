# basics.py

# 1. Basic Types
age: int = 48
price: float = 39.99
name: str = "Venky"
is_active: bool = True

# 2. Collection Types
# List: Mutabable (Can be changed)
skills = ["Python", "Django", "JavaScript"]  # type: list[str]
skills.append("React")
skills.insert(1, "VS Code")

# Tuple: Immutable (Cannot be changed)
coordinates = (10.0, 20.0)  # type: tuple[float, float]

# Dictionary: Key-Value pairs (like JSON)'
user = {"username": "VenkyP77", "Role": "Developer", "age": 48}  #

print(
    f"User {user['username']} is a {user['Role']} aged {user['age']} has skills: {skills}"
)

# 3. Control Flow

# Loop through a list
skills.append("Linux")
print("\n--- Skill Check ---")
for skill in skills:
    if skill == "Linux":
        print(f"{skill} is essential for servers!")
    else:
        print(f"{skill} is a great tool.")

# While loop
count = 3
while count > 0:
    print(count)
    count -= 1
print("Liftoff! 🚀")


# 4. getmax number from a list
def get_max(numbers: list[int]) -> int:
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num


# 5A. reverse a string
def reverse_string(s: str) -> str:
    reversed_s = ""
    for char in s:
        reversed_s = char + reversed_s
    return reversed_s


# 5B. reverse a string using slicing
def reverse_string_slicing(s: str) -> str:
    return s[::-1]


# 6. Check prime number
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# Test the functions
print(f"Max of [10, 5, 20]: {get_max([10, 5, 20])}")
print(f"Reverse 'Python': {reverse_string('Python')}")
print(f"Is 29 prime? {is_prime(29)}")
print(f"Reverse 'Naughty' using slicing: {reverse_string_slicing('Naughty')}")


def process_file(input_file: str, output_file: str):
    try:
        # 'with' automatically closes the file even if errors occur
        with open(input_file, "r") as f:
            content = f.read()

        # Process: Convert to uppercase
        processed_content = content.upper()

        with open(output_file, "w") as f:
            f.write(processed_content)

        print(f"Success! Processed data saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")


# Run the file processor
process_file("data.txt", "data_upper.txt")
