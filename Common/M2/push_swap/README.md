*This project has been created as part of the 42 curriculum by pabrogi.*

# Description

This project is called **push_swap**, and its goal is to sort a list of integers using only two stacks (A and B) and a limited set of operations (`sa`, `sb`, `pa`, `pb`, `ra`, `rb`, `rra`, `rrb`).  
The main challenge is to sort the numbers **correctly** while using **the minimum number of moves possible**, which makes the problem both algorithmic and strategic.

The program works in several steps:

1. **Input validation** – checks for errors and duplicate numbers.  
2. **Indexing** – each number gets an index corresponding to its final position in a fully sorted list. This simplifies comparisons and allows the algorithm to work independently of the actual values.  

Depending on the number of elements in the input, the program selects the sorting strategy:

- **3 numbers** → uses a simple `sort_three` algorithm.  
- **5 numbers** → uses `sort_five`, which moves the smallest elements to stack B, sorts the remaining numbers in A, then inserts elements from B in the correct position.  
- **More than 6 numbers** → uses a **greedy algorithm with cost calculation**:
  1. **Push all but three numbers to B** – first moving the smaller half of the numbers to B (index ≤ size/2), then pushing the rest except the last three.  
  2. **Sort the three numbers in A** using `sort_three`.  
  3. **Insert numbers from B back to A**:
     - For each number in B, find its **target position** in A (the first element with a higher index).  
     - Calculate the **cost** to move it to the correct position (rotations on A and B combined).  
     - Move the number with the **lowest total cost** first.  
  4. **Shift the stack** – after B is empty, rotate A so that the smallest number is on top, completing the sort.

This method ensures that the algorithm handles both small and large lists efficiently, minimizing operations while following the project rules.
AI got used during this project just to short the functions at 25 lines, multiples functions where up to 38 lines and couldn't find easy and clear way to short them 
I decided to get some help from ChatGPT

---

# How It Works

The push_swap algorithm works in several main phases:

1. **Input validation and indexing**  
   - Checks for errors and duplicate numbers.  
   - Assigns an **index** to each number corresponding to its final sorted position.  

2. **Choosing the sorting strategy**  
   - For **3 numbers** → uses `sort_three`  
   - For **5 numbers** → uses `sort_five`  
   - For **more than 6 numbers** → uses a **greedy cost-based algorithm**

3. **Pushing numbers to stack B (for large lists)**  
   - First, moves the **smaller half of numbers** (index ≤ size/2) to B  
   - Then moves the remaining numbers to B, leaving only **3 numbers in A**  
   - This reduces complexity and prepares A to be partially sorted  

4. **Sorting the remaining 3 numbers in A**  
   - Uses `sort_three` to sort the top 3 numbers in A  

5. **Reinserting numbers from B to A**  
   - For each number in B:
     - Finds its **target position** in A (the first element with a higher index)  
     - Calculates the **cost**: how many rotations of A and B are needed to insert it  
   - Moves the number with the **lowest cost** first  
   - Repeats until B is empty  

6. **Final adjustment with `shift_stack`**  
   - After B is empty, the **smallest number** may not be on top  
   - Rotates A until the smallest number is at the top, completing the sort  

---

# Instructions

1. **Compile the project**:

```bash
make