1. Introduction to Data Types : Data Types tell us what kind of data we have.

Numerical Data: Numbers you can measure or count (e.g., age, height, salary).
                Continuous: Can take any value (e.g., temperature 23.5°C).
                Discrete: Countable numbers (e.g., number of students).

Categorical Data: Data divided into categories (e.g., gender, color).
                  Nominal: No order (e.g., red, blue, green).
                  Ordinal: Ordered categories (e.g., small, medium, large).

2. Numerical Parameters to Represent Data
These are ways to summarize and describe data using numbers:

a. Mean: The average of data points.

Add all values and divide by the number of values.

Example: For [2, 4, 6], mean = (2+4+6)/3 = 4.

b. Mode: The most frequent value in the data.

Example: In [2, 3, 3, 5], mode = 3 (because 3 appears most).

c. Median: The middle value when data is sorted.

If even number of values, average the two middle ones.

Example: For [1, 3, 5], median = 3; For [1, 4, 6, 8], median = (4+6)/2 = 5.

d. Sensitivity: In classification, sensitivity measures the model’s ability to correctly identify true positives.

Formula:

Sensitivity = True Positives / True Positives + False Negatives

​Example: If a test identifies 90 sick people correctly out of 100, sensitivity = 90%.

e. Information Gain: A measure used in decision trees to decide which feature best splits the data.

It shows how much uncertainty is reduced by knowing the value of a feature.

Higher information gain means better feature for splitting.

f. Entropy: A measure of uncertainty or disorder in the data.

In classification, entropy quantifies how mixed the classes are.
Formula:

Entropy= −∑𝑝𝑖log2(𝑝𝑖)
where 
𝑝𝑖 = is the proportion of class 
If entropy = 0, data is pure (all one class). If entropy is high, data is mixed.

3. Statistical Parameters to Represent Data
These parameters help describe the distribution and spread of the data:

Variance: Measures how much data values vary from the mean.

Standard Deviation: Square root of variance; shows average distance from the mean.

Range: Difference between max and min values.

Percentiles/Quartiles: Divide data into parts or seggmants (e.g., median is the 50th percentile).
                       25th percentile (Q1), 50th percentile (median), 75th percentile (Q3)

PROBABILITY 

Probability is a branch of mathematics that measures how likely an event is to happen.
It is expressed as a number between 0 and 1:
0 means the event cannot happen
1 means the event will definitely happen
For example, the probability of tossing a fair coin and getting heads is 0.5 (50%).

Why Do We Need Probability?
Real-life events are uncertain; probability helps measure and manage that uncertainty
Provides a scientific method for making predictions
Helps quantify risks and benefits
Supports fair games and experiments

Bayesian Inference : A statistical method that updates the probability of an event or hypothesis based on new data

Follows Bayes’ Theorem: Posterior = Prior × Likelihood / Evidence

​
Density Concepts: In continuous data, probabilities are described using a probability density function (PDF)
The PDF shows how probability is spread over a range of values
Probabilities are calculated as the area under the curve between two values
The total area under the entire curve is always 1
Example: a PDF describing the probability of people’s heights

Normal Distribution

Also called the Gaussian distribution or bell curve
Symmetrical shape centered around the mean
Mean = median = mode
Defined by two parameters: mean (average) and standard deviation (spread)
About 68% of data falls within 1 standard deviation of the mean, 95% within 2, and 99.7% within 3
Appears in many natural and social phenomena (e.g., test scores, heights, measurement errors)

STATISTICAL INFERENCE

Point Estimation: Using sample data to estimate a single (point) value of a population parameter.
Example: Using the sample mean to estimate the true average height of all students.
If a sample of 10 students has an average height of 160 cm, that 160 cm is a point estimate of the population mean.

Confidence Margin (Confidence Interval) : When you estimate something (like an average), you usually don’t get the exact true value, just an approximate.

A confidence interval gives you a range where you think the true value really is.
The confidence level (like 95%) tells you how sure you are that the true value is inside that range.
The margin of error is how far off your estimate could be from the true value.

Simple example:
If you estimate that the average test score is 80, and the margin of error is 5, then the confidence interval is from 75 to 85.
This means: I am 95% confident that the true average score is somewhere between 75 and 85.

Hypothesis Testing: Hypothesis testing is a way to check if what you believe about data is likely true or not.
                    You start with a claim (called a hypothesis), then use data to check if there’s enough proof.

There are two types of claims:

Null hypothesis (H0): This is the starting assumption. Example: “The new medicine is no better than the old one.”

Alternative hypothesis (H1): This is what you want to prove. Example: “The new medicine is better.”

Goal: Use sample data to see if we can reject H0 (the default assumption).

Levels of Hypothesis Testing (Significance Level)
The significance level (called alpha, α) tells you how much risk you’re okay with when it comes to making a mistake.

Most common levels: 0.05 (5% risk)
                    0.01 (1% risk)

What it means:
If alpha = 0.05 → You accept a 5% chance you might wrongly reject the null hypothesis (H0), even if it is actually true.

A smaller alpha (like 0.01) means you want to be extra careful before rejecting H0.

Types of Errors in Hypothesis Testing
Type I Error (False positive)

You say something is true (reject H0) when actually H0 was right.

Example: You think the medicine works, but it really doesn’t.

Type II Error (False negative)

You say nothing is happening (fail to reject H0), when actually H0 is wrong.

Example: You think the medicine doesn’t work, but it actually does.

Summary in one sentence:
Hypothesis testing helps decide if data gives enough evidence for a claim. You set a risk level (alpha), and you try to avoid errors where you either wrongly believe something works (Type I) or wrongly believe it doesn’t (Type II).

4.DATA CLUSTERING





