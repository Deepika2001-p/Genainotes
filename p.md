variable : Variables are containers for storing data values.

Datatypes in python :
1.int : x = int(20)
2.str : x = str("Hello World")
3.float: x = float(20.5)
4.complex: x = complex(1j)
5.list: x = list(("apple", "banana", "cherry"))
6.tuple: x = tuple(("apple", "banana", "cherry"))
7.range: x = range(6)
8.Dictionary: x = dict(name="John", age=36)
9.Boolean: x = bool(5)
10.set: x = set(("apple", "banana", "cherry")).

There are four collection data types in the Python programming language:

List is a collection which is ordered and changeable. Allows duplicate members.
Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
Dictionary is a collection which is ordered** and changeable. No duplicate members.

Operators of python : Operators are used to perform operations on variables and values.

1.Arithmetic : 
Operator	Name	       Example	
+	        Addition	    x + y	
-	        Subtraction	    x - y	
*	       Multiplication	x * y	
/	        Division	    x / y	
%	         Modulus	    x % y	
**	       Exponentiation	x ** y	
//	       Floor division	x // y	

2.Assignment Operators : are used to assign values to variables
3.Comparison Operators : Comparison operators are used to compare two values.
Operator	Name	              Example	
==	       Equal	              x == y	
!=	      Not equal	              x != y	
>	    Greater than	          x > y	
<	     Less than	               x < y	
>=	Greater than or equal to	   x >= y	
<=	Less than or equal to	       x <= y

4.Logical Operators : Logical operators are used to combine conditional statements.
Operator	          Description	                                          Example	            
and 	Returns True if both statements are true	                    x < 5 and  x < 10	
or	    Returns True if one of the statements is true	                x < 5 or x < 4	
not	    Reverse the result, returns False if the result is true	        not(x < 5 and x < 10)	

5.Identity Operators:Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.
Operator	                      Description	                              Example	
is 	           Returns True if both variables are the same object	          x is y	
is not	       Returns True if both variables are not the same object	      x is not y

6.Membership Operators:re used to test if a sequence is presented in an object.
Operator	                                     Description	                                Example	
in 	          Returns True if a sequence with the specified value is present in the object	    x in y	
not in	      Returns True if a sequence with the specified value is not present in the object	x not iny

7.Bitwise Operators: are used to compare (binary) numbers.
Operator	Name	                 Description	                               Example	
& 	        AND	                 Sets each bit to 1 if both bits are 1	            x & y	
|	        OR	                 Sets each bit to 1 if one of two bits is 1	        x | y	
^	        XOR	               Sets each bit to 1 if only one of two bits is 1	    x ^ y	
~	        NOT	                     Inverts all the bits	                         ~x	
<<	Zero fill left shift	Shift left by pushing zeros in from the right 
                              and let the leftmost bits fall off	                x << 2	
>>	Signed right shift	   Shift right by pushing copies of the leftmost 
                         bit in from the left, and let the rightmost bits fall off	x >> 2