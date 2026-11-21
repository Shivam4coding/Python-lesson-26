"""
1) Add the file and topic details.
   a) Mention the file name as `03-mask-and-check.py`.
   b) Mention the topic as "Building a Bit Mask, Check if Nth Bit is Set".
   c) Introduce the program as a way to create masks and check if a bit is ON.

2) Explain bit masks.
   a) Explain that a bit mask has one 1 at a specific position.
   b) Pause the program before showing mask examples.
   c) Use a for loop to create masks for positions 0 to 3.

3) Build masks using left shift.
   a) Use `1 << k` to move 1 to position `k`.
   b) Store the result in `mask`.
   c) Print the bit position, mask value, and binary form.

4) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 42 or 13.
   c) Convert the input into an integer.

5) Ask for a prediction.
   a) Ask whether bit 2 of the number is ON.
   b) Store the user's guess.

6) Check if bit 2 is set.
   a) Pause before running the check.
   b) Use `n >> 2` to move bit 2 to the last position.
   c) Use `& 1` to check whether that bit is 1.
   d) Store the answer in `result`.

7) Display the bit check result.
   a) If `result` is true, print that bit 2 is ON.
   b) Otherwise, print that bit 2 is OFF.
   c) Print the number's binary form.
   d) Show the user's original guess.
"""

input("Press Enter to continue to the next section...")
for k in range(4):
      mask = 1 << k
      print("Bit position:", k, "Mask value:", mask, "Binary form:", bin(mask)[2:])

n = int(input("Enter a number (e.g., 4)"))
guess = input("Is bit 2 of the number ON? (yes/no): ")
input("Press Enter to check if bit 2 is set...")
result = (n >> 2) & 1
if result:
      print("Bit 2 is ON.")
else:
      print("Bit 2 is OFF.")
print("Binary form of", n, "is", bin(n)[2:])
print("Your guess was:", guess)