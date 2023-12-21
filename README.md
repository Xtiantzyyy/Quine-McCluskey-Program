Quine-McCluskey Program - Python 3 Code
Simplify Boolean expressions effortlessly with the Quine-McCluskey Method using this Python program. 
Ideal for Logic Design, the code takes user inputs for variables (minterms or don't care terms) and applies the Quine-McCluskey method along with Petrick’s method to streamline Boolean expressions.

Key Functions:
comb Function
Combine two minterms, handling Boolean algebra operations, avoiding duplicates, and considering complemented terms.

combine Function
Combine expressions by iterating through elements and merging corresponding minterms, generating a list of combined expressions.

remove Function
Remove minterms present in the don't care list from the minterm list.

searchEPI Function
Identify essential prime implicants, recognizing those covering only a single minterm.

searchVariables Function
Extract and return a list of variables from a binary string.

flatten Function
Convert a nested list into a flat list, simplifying grouped minterms processing.

searchMinterms Function
Generate a list of minterms from a binary string, considering positions with a dash (-).

compare Function
Check if two binary strings representing minterms differ by only one bit.

removeTerms Function
Remove columns related to essential prime implicants from the prime implicant chart.

Input Processing:
Prompt users for variables, minterms, and don't cares, creating a sorted list called minterms.

Table Creation and Prime Implicant Search:
Initiate variables, compare minterms, and generate prime implicants iteratively.

Processing Essential Prime Implicants:
Identify, remove, and apply Petrick's method if necessary, storing results in final_result list.

Display Final Result:
Sequentially display the final result.
