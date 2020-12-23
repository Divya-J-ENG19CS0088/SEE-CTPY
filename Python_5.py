‘’’
This function takes two arguments,
Data1 and data2, which contain
Key-value pairs. All key-value
Pairs within data1 are unique.
Similarly, all key-value pairs
Within data2 are unique. However,
There may be key-value pairs (k, v1)
In data1 and (k, v2) in data2 with a
Common key k. In this case, v1 and
V2 may be the same, or v1 and v2 may
Be different.
This function should modify only
Data1 and return a (possibly empty)
Dictionary as follows:
For every key-value pair (k, v2) in
Data2, if no key-value pair with key
K exists in data1, then the pair
(k, v2) should be added to data1.
Otherwise, there is a unique pair
(k, v1) already in data1. If v1 and
V2 are different, the pair (k, v1)
Should be removed from data1 and the
Key-value pair (k, [v1, v2]) should
Be added to the (initially empty)
Dictionary to be returned.
In this implementation, data1 is a
Dictionary and data2 is a list where
Each key-value pair in data2 is alsoA list [key, value] of length 2.
‘’’
Def uniqueUpdate(data1, data2):
 # Initially empty dictionary
 dupKeys = {}
 # Examine every (k, v2) pair in data2
 For k, v2 in data2.items():
 # Search for a key-value pair
 # with key = k in data1
 # (no such pair found yet)
 kFound = False
 for [k1, v1] in data1:
 if k1 == k:
 # Found pair with key = k
 kFound = True
 if v1 != v2:
 # Remove (k, v1) from data1
 Data1.remove([k,v1])
 # Add (k, [v1, v2])
 # to dictionary
 dupKeys[k] = [v1,v2]
 
 # After the loop, check if
 # k was not found
 If not kFound:# Add (k, v2) to data1
 Data1.append([k, v2])
 # After processing all (k, v2) in
 # data2, return the dictionary
 Return dupKeys
‘’’
Visualize this function on an example:
https://tinyurl.com/dsaprac20
‘’’
## DO NOT MODIFY BELOW THIS LINE! ##
‘’’
This part of the code reads input in
The following format:
Line 1: A positive integer n1
Representing the number of key value
Pairs in data1
Lines 2 to n1+1: Two integers k v
Per line representing the key and
Value (these n1 key value pairs are
Added to data1)
Line n1+2: A positive integer n2
Representing the number of key value
Pairs in data2
Lines n1+3 to n1+n2+2: Two integers
K and v per line representing the
Key and value (these n2 key valuePairs are added to data2)
This also prints the output in the
Following format after calling the
uniqueUpdate function:
data1
data2 (should remain the same)
dup (the dictionary returned)
‘’’
Import sys
If __name__ == ‘__main__’:
 Data1 = []
 N1 = int(input())
 For _ in range(n1):
 K, v = map(int, input().split())
 For [k1, v1] in data1:
 If k1 == k:
 Sys.exit(“Illegal: data1”)
 Data1.append([k, v])
 Data2 = {}
 N2 = int(input())
 For _ in range(n2):
 K, v = map(int, input().split())
 If k in data2:
 Sys.exit(“Illegal: data2”) 
 Data2[k] = v
 Dup = uniqueUpdate(data1, data2)
 Print(data1)
 Print(data2)
 Print(dup)
