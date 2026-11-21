"""
1) Add the file and topic details.
   a) Mention the file name as `01-set-and-power.py`.
   b) Mention the topic as "Set Bits and Zero Bits, Power of 2 Check".
   c) Introduce the program as a way to understand bit setting, bit clearing, and powers of 2.

2) Demonstrate setting a bit.
   a) Pause the program before showing the example.
   b) Print the binary form of 5.
   c) Use the OR operator `|` to turn a bit ON.
   d) Show the result of `5 | 2` in decimal and binary.

3) Demonstrate zeroing a bit.
   a) Pause the program before showing the example.
   b) Print the binary form of 7.
   c) Use the AND operator `&` to turn a bit OFF.
   d) Show the result of `7 & 5` in decimal and binary.

4) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 4 or 6.
   c) Convert the input into an integer.

5) Ask for a power of 2 prediction.
   a) Ask the user if the number is a power of 2.
   b) Store the user's guess.

6) Check if the number is a power of 2.
   a) Pause before running the check.
   b) Check that the number is greater than 0.
   c) Use `(n & (n - 1)) == 0` to test if only one bit is ON.
   d) Print that the number is a power of 2 if the condition is true.

7) Show the final result.
   a) Print the number.
   b) Print its binary form using `bin(n)[2:]`.
   c) Print whether it is a power of 2 or not.
   d) Show the user's original guess.
"""

input("Press Enter to continue to the next section...")
print("Demonstrating setting a bit:")
print("Binary form of 5:", bin(5)[2:])

input("Press Enter to set the 2nd bit (turn ON):")
print("5 | 2 =", 5 | 2, "in decimal and", bin(5 | 2)[2:], "in binary.")
print("\nDemonstrating zeroing a bit:")

n = 7
print("Binary form of 7:", bin(n)[2:])
input("Press Enter to clear the 2nd bit (turn OFF):")

if n & 2:
      print("7 & 5 =", n & 5, "in decimal and", bin(n & 5)[2:], "in binary.")

else:
      print("The 2nd bit is already OFF.")
