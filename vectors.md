Linear equation : It is an algebraic equation where each term has an exponent of one and when the equation is graphed it always results a straight line.
Linear equation can be expressed in 3 standard forms
1.standard form  ax + b = 0
2.slope intercept form y= mx + c
3.point slope form (y-y1)=m(x-x1)
why we use linear equations : to predict the relationships like time and speed and where there is a constant rate of change between two variables.

where we use linear equations :  phone recharge plan 
a phone plan has fixed monthly fees plus minute charge.so we can write this in equation y=45+0.5x 
here y is total cost 
x is minutes we used
45 is fixed charge 
0.5 is charge per minute 

MATRICES

what is matrix : matrix is an rectangular array of numbers  arranged in rows and columns. where each matrix is identified by its position.
                  [A]m*n where m = represents number of rows 
                               n =  represents number of columns

Types of matrixs are:
1. singleton : a matrix that has only one element 
2. null : a matrix whose all elements are zero.
3. row matrix : a matrix that contain only one row.
4. column matrix : a matrix that contain only one column.
5. horizontal matrix : a matrix that contain number rows is lower than number of columns.
6. vertical matrix : a matrix that contain number of rows is higher than number of columns
7. Rectangular : a matrix that does not have equal number of rows and columns
8. square : a matrix which has equal number of rows and columns
9. Diagonal : a matrix which has all the elements zero except the diagonal elements.
10. scalar : a matrix which follow another matrix rule diagonal matrix whose all diagonal elements are non zero.
11. identity : a matrix where all the diagonal elements are 1 and other are zero.
12. Triangular : A square matrix in which the non-zero elements form a triangular below and above the diagonal 
                 1.upper triangle : A square matrix where elements below the diagonal are zero and the elements from the diagonal and above are non-zero 
                 2.lower triangle : A square matrix where elements above the diagonal are zero and the elements from the diagonal and below are non-zero 
13.symmetric matrix : A symmetric matrix is a square matrix that is equal to its transpose.

example : Image processing



EIGEN VALUES AND EIGEN VECTORS

When a matrix is applied on a vector, it usually changes the vector’s direction and size.
But sometimes, a special vector only gets stretched or shrunk, not turned — it stays in the same direction.

That special vector is called an "eigenvector"
The amount it’s stretched/shrunk is called the "eigenvalue"

Types of Eigenvector :The eigenvectors calculated for the square matrix are of two types
                      1.Right Eigenvector : The eigenvector which is multiplied by the given square matrix from the right-hand side
                      2.Left Eigenvector : The eigenvector which is multiplied by the given square matrix from the left-hand side


EIGEN VALUES : It is a scalar factor and eigenvalue tells how much the eigenvector is stretched.
The equation for eigenvalue is given by
Av = lambda v
A is the matrix
v is eigenvector
lambda is eigenvalue.

example : Imagine you're holding a stick pointing east.
          You stretch it to double its length, but still pointing east.
          The stick’s direction didn’t change - it's an eigenvector
          It got 2 times longer - 2 is the eigenvalue



VECTORS: vectors were introduced for quantities that have both a magnitude and direction.
         A vector is something that has: Magnitude (how much)
                                         Direction (which way)
example : The wind blows at 20 km/h east.
          This is a vector — it tells speed and direction.

VECTOR SPACES: A vector space is a collection of vectors where:
               You can add any two vectors in the space
               You can multiply a vector by a number (called a scalar)
               The result is still in the same space

example: Imagine you’re building with LEGO blocks:
         You can add blocks in different directions (vectors).
         You can double the size (scalar multiplication).
         As long as you follow the building rules (like straight lines), your new shape is still in your LEGO world — (your vector space).



Additive Closure : If you add any two vectors in the space, the result is also in the space.
Additive Commutativity : The order of vector addition is does not matter u+v = v+u
Additive Associativity : Grouping of vectors in addition doesn't affect the result. (u+v)+w = u+(v+w)

LINEAR INDEPENDANCE: No vector in the set can be made by adding or multiplying by the other vectors. 

Linearly Independent	Vectors are truly different
Linearly Dependent	One vector is a mix of others


example : Paint Mixing
You have Red, Blue, and Green paints.
You can mix them in different amounts to make other colors.
Each color brings something unique → linearly independent
But if you had:
Red
Red again
A mix of 0.5 Red + 0.5 Red
All are just scaled or mixed versions of Red → dependent


BASIS : A basis is a minimum set of independent vectors that can be used to build any vector in a space.

example : Imagine a piano keyboard.
Each key makes a different sound. But in music, you don't need all the keys to play any song — you just need the basic notes of a scale (like C, D, E, F, G, A, B).
These 7 notes form a basis for music in the C major scale.
You can combine them (play them faster, slower, together) to make any song in that scale.



RANK : The rank of a matrix or set of vectors is the number of independent vectors in it.

example : Suppose we have 3 students: A knows coding
                                      B knows designing
                                      C also knows coding (same as A)
Rank = 2 → only 2 independent skill sets (coding & design)
(C’s skill is not new)
So:
Independent skills = rank
Same skills = do not increase rank

Distance between two vectors : To find the distance between two vectors A and B, use the Euclidean distance formula.

angle between two vectors : we can find angle using dot product formula. 
                           
                 
ANGLES AND TYPES 

An angle is formed when two lines meet at a common endpoint.

Acute Angle-Less than 90°-sharp, small angle
Right Angle-Exactly 90°-Forms a perfect L shape
Obtuse Angle-Greater than 90° and less than 180°-A wide angle
Straight Angle-Exactly 180°-Forms a straight line
Reflex Angle-Greater than 180° and less than 360°-A bent-backward angle
Full Angle-Exactly 360°-A full circle or full rotation  

example : clock 
          when we move clock time little bit it would be acute angle
                                      
