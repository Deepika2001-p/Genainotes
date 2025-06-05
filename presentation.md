                                        MODULE 1
A. SETS  & EXPERIMENTS

Set → A well-defined group of elements.
{Math, Science, English} subjects offered in a term.

set operations:

Union (A ∪ B)
All elements from A and B, no duplicates.
Example: A = {Math, Science}, B = {English, Science}
A ∪ B = {Math, Science, English}

Intersection (A ∩ B)
Common elements in both sets.
Example: A = {Math, English}, B = {English, Science}
 A ∩ B = {English}

Difference (A − B)
Elements in A but not in B.
Example: A = {Math, Science, English}, B = {Science}
A − B = {Math, English}

Complement (A′)
All elements not in A (based on universal set U).
Example: U = {Math, Science, English, History}, A = {Math, English}
A′ = {Science, History}


Collection → A collection is a group of items or elements.

ex: Brilliant students → not a set (subjective, not clearly defined)
Students who scored above 90%" → a set (clearly defined collection)


Random Experiment → Activity with unpredictable outcome.
ex:Conducting a surprise quiz in class

Sample Space → All possible outcomes of an experiment. 
ex:{Pass, Fail} outcomes of a quiz

Event → A subset of the sample space.
ex:A student scores more than 80%.

Basic Outcome → A single possible result.
ex:“Pass” result from the quiz

Random Variable → Number of students who passed in a class

types of Random Variables

Discrete → Countable outcomes
Ex: Number of students scoring A grade

Continuous → Any value in a range
Ex: Time taken to complete an exam

B. PROBABILILITY

Probability → Measures how likely an event is to happen.it always between 0 and 1.
ex:Chance that a student scores above 90% in math.

Conditional Probability → Probability of an event, given that another event has already happened.
ex:Probability of passing the exam given the student attended tutoring sessions.

Independent Event → One event does not affect the other.
ex: Weather and quiz results — they’re unrelated.

Dependent Event → One event does affect the other.
ex:Homework submission and test performance

Bernoulli Theorem → A single experiment with only 2 outcomes: success or failure.
ex:Student submits or doesn’t submit homework

Binomial Distribution → Probability of getting a certain number of successes in repeated Bernoulli trials.
ex:Number of students out of 10 who submitted homework

Normal Distribution → Data distributed symmetrically around the mean — follows the bell curve.
ex: Distribution of final exam scores in a large class.


C. DATA FUNCTIONS

Function → A rule that assigns exactly one output for each input.
ex:Mapping student ID → quiz score

PMF (Probability Mass Function) → Gives the probability of a specific discrete outcome.
ex:Probability of scoring exactly 2 marks in a 3-mark quiz

CDF (Cumulative Distribution Function) → gives the probability that a variable is less than or equal to a certain value.
ex:Probability a student scores up to 70 marks in a subject.

Expected Value → The average value you expect over many repetitions.
ex:Expected score in a random 3-question quiz

Mean → The average of all data values.
ex:Average marks of the class in science

Median → The middle value when data is sorted.
ex:Middle score in a ranked list of math marks.

Mode : The value that appears most frequently in a dataset.
ex: Most common mark scored in a class test.

Variance: Measures how far the scores are spread from the mean.
ex: ells how much students’ scores vary in the Science test.


Standard Deviation →  The square root of variance — shows spread of data in the same unit as original.
ex:spread of marks in the same unit as original scores.If average marks = 75 and standard deviation = 10, most students scored between 65 and 85.



 
                               MODULES 2

LINEAR EQUATIONS

Definition → An equation where variables have exponent 1, forming a straight-line graph

Standard Form → ax + b = 0 — used in exam score thresholds

Slope-Intercept Form → y = mx + c — models cost based on tutoring hours

Point-Slope Form → (y - y₁) = m(x - x₁) — tracks student improvement rate

Use → To relate time studied and marks gained

Example → Tuition cost = y = 200 + 50x (₹200 fixed + ₹50 per hour of extra help)

MATRICES

Matrix → A table of student marks in different subjects

Singleton Matrix → A matrix showing one student’s attendance on one day

Null Matrix → Student test where all answers are wrong (all zeros)

Row Matrix → A single student’s scores in multiple subjects

Column Matrix → One subject’s marks across multiple students

Horizontal Matrix → More subjects (columns) than students

Vertical Matrix → More students (rows) than subjects

Rectangular Matrix → Class with more students than subjects or vice versa

Square Matrix → Equal number of students and subjects

Diagonal Matrix → Class where only top scorers are highlighted on the diagonal

Scalar Matrix → All students scored the same in respective subjects

Identity Matrix → Each student scored full marks in only their own subject

Triangular Matrix → Progressive improvement or decline in scores across terms

Symmetric Matrix → if A rated B as 4, B rated A as 4

Example → Storing and analyzing student scores in a school database


EIGENVALUES & EIGENVECTORS

Eigenvector → A student who maintains their performance level in every test

Eigenvalue → The performance multiplier (e.g., improving by 2×)

Right Eigenvector → Student results affected by question paper design

Left Eigenvector → School-level performance factors affecting all students

Equation → Av = λv — effect of evaluation system on student performance

Example → A student always topping class — scores improve, but pattern stays the same


VECTORS & VECTOR SPACES

Vector → A student’s academic profile (marks in subjects + learning direction)

Example → Student A: 80 in Math, 90 in Science — both value (magnitude) and subject (direction)

Vector Space → Set of all possible student profiles under a grading system

Example → Every possible combination of student scores following grading rules

Additive Closure → Merging study efforts of two students → still valid profile

Commutativity → Combining efforts in group work is order-independent

Associativity → Study sessions grouped differently still result in same total effort


Linear Independence, Basis & Rank

Linear Independence → Each student’s subject choice is unique

Example → One chooses Math, one Science, one English = Independent

Basis → Minimal set of subject experts needed to cover all topics in school

Example → {Math, Science, English} form a basis to cover syllabus

Rank → Number of truly distinct subject specializations among students

Example → 3 students: one knows Math, one knows Science, third knows Math again → Rank = 2


Distance & Angle Between Vectors
Distance Between Vectors → How different two students are based on their subject scores
To find the distance between two vectors A and B, use the Euclidean distance formula.


Angle Between Vectors → Similarity in subject focus (ex :one focuses on Science, another on English — large angle)
we can find angle using dot product formula. 

Types of Angles

Acute Angle → Clock at 10:10 — class starts soon

Right Angle → Clock at 3:00 — time for sharp break

Obtuse Angle → Clock at 2:40 — end of a long session

Straight Angle → Clock at 6:00 — school day halfway done

Reflex Angle → Clock at 7:00 — time dragging late into study

Full Angle → 12:00 to 12:00 — full school day completed

    
                                MODULE 3 

CENTRALITY : It measures how important a node is in a network.

ex: how student (or) teacher important in a school.

types:

1.Degree centrality : it measures how many direct links a node has.

ex: a student who interacts with many students in a group project has high degree centrality.

2.Betweeness centrality : it measures how often a node lie on shortest paths.

ex: a mentor teacher who connects junior staff and senoir faculty.

3.closeness centrality : it measures how easily a node can reach other nodes.

ex: a school counselor connected to all students in only few steps like any annoncements or activities in school.

4.Eigenvector centrality : it measures nodes influence based on how important it connections are.

ex: a student respected by top performers in the class.


                                    SOCIAL NETWORK

A structure made up of entities and connected by relationships.

ex: nodes: students
    edges: collaborated on a project

    here entities means a student , teacher or subject.


                                    TRADITIONAL DATABASE

a database which stores data in tables(rows/columns) used for stuctured data.

ex: school management systems to track academic records.storing the data of students about course attendance grades etc...


                                    NETWORK THEORY

IT is a study of how components are connected and interact in a system using nodes and edges.

ex: nodes=classrooms   edges=hall or floor connecting them (or) wifi coverage across a school.

                                    GRAPH THEORY 

It shows how things are connected using nodes and edges.


ex:          python   mathematics
               \         /
                    ML
                    |                        each subject is a node and each edge is a relationship
                    AI
                    |
                Deep learning


                                    GRAPH DATABASE

A database that stores structured unstructured data in the form of a graph using nodes and edges just like graph theory.

ex: node1 = student
    node2 = subject
    edge = attends
a student attends subject.so the graph shows who studies what,who teaches whom..