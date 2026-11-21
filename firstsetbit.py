"""
1) Add the file and topic details.
   a) Mention the file name as `02-first-set-bit.py`.
   b) Mention the topic as "The First Set Bit".
   c) Introduce the program as a way to find the rightmost 1 in a binary number.

2) Explain the first set bit.
   a) Explain that the first set bit is the rightmost 1.
   b) Pause the program before showing examples.
   c) Show the binary form of 5.
   d) Show the binary form of 8.
   e) Mention the first 1 position for both examples.

3) Ask for a number.
   a) Ask the user to enter a number.
   b) Suggest example values like 8 or 14.
   c) Convert the input into an integer.

4) Prepare to scan the bits.
   a) Store the user's number in `temp`.
   b) Create `pos` to track the current bit position.
   c) Start `pos` from 0.

5) Use a while loop.
   a) Repeat while `temp` is greater than 0.
   b) Print the current binary form of `temp`.
   c) Use `temp & 1` to check the last bit.

6) Find the first set bit.
   a) If the last bit is 1, stop the loop using `break`.
   b) If the last bit is 0, increase `pos` by 1.
   c) Use `temp >>= 1` to shift the bits right.

7) Display the result.
   a) Print the original number.
   b) Print the position of the first set bit.
   c) Show how right shift helps drop bits one by one.
"""

input("Press Enter to coninue to the next section...")
print("Demonstrating the first set bit:")
print("Binary form of 5:", bin(5)[2:])

n = 8
input("Press Enter to see the binary form of 8:")
temp = n
pos = 0
while temp > 0:
      print("Current binary form of", temp, "is", bin(temp)[2:])
      if temp & 1:
         break
      pos += 1
      temp >>= 1
print("The first set of bit in", n, "is at position:", pos)

