FEATURE SELECTION:
Feature selection is about choosing only the most important features (columns) in our dataset and removing irrelevant ones.
This step helps the model:
 Focus on useful information
 Run faster and more efficiently
 Avoid unnecessary complexity and overfitting

Supervised Feature Selection: Spam Email Detection
Here, we know the target label (e.g., spam or not spam), so we use that information to find the most relevant features.
Example:
•	In a spam detection model, words like free, offer, and click might be highly predictive, while email header IDs are irrelevant.
Common Methods:
•	Filter Methods: Select features with strong correlation to the target.
•	Wrapper Methods: Add or remove features step-by-step and evaluate model performance.
•	Embedded Methods: Let the model select features automatically (e.g., Lasso Regression).
For example, if we are predicting house prices, we’ll keep features like square footage, number of bedrooms, and location, but remove features like owner’s name, which are irrelevant.

Unsupervised Feature Selection: Here, we do not have any target variable. Instead, we focus on preserving the data’s structure or variance.
Example: customer segmentation - No labels, we group customers based on patterns.
Some techniques are:
•	Variance threshold, where we remove features with very little change.
•	Laplacian score, which uses graph-based methods to rank features.”
Example:
Think about customer segmentation. We might keep features like purchase frequency, which vary across customers, and drop features that are almost the same for everyone.


FEATURE ENGINEERING:
feature engineering helps us make the dataset smarter so the model can learn better.
Feature engineering is the process of creating, transforming, or combining variables to help the model understand patterns better.
Supervised Feature Engineering: Loan Default Prediction
In supervised feature engineering, we use the target labels to create new features that help the model understand patterns better.
For example, in a loan default prediction model, we start with a dataset containing age, income, loan amount, and payment history. But raw data isn’t always enough.
We can create smarter features like:
•	Debt-to-Income Ratio: Loan amount ÷ income. Higher ratios suggest higher risk.
•	Number of Late Payments (last 6 months): Captures recent payment behavior.
•	Credit Utilization: Measures how much of available credit is being used; high usage signals financial stress.
These engineered features make the model more powerful and improve prediction accuracy.

Unsupervised Feature Engineering: Image Compression with PCA
In unsupervised it does not contain any target labels. Instead, it creates features to capture general patterns or structures in the data.
Example: Text clustering: Transform raw text into TF-IDF vectors. convert text into a numeric vector that reflects the importance of words in the documents.
PCA, or Principal Component Analysis, compresses an image by reducing its dimensions. For example, a 100×100 image has 10,000 pixel values, which means 10,000 dimensions. PCA identifies the directions where the pixel values vary the most, called principal components, and keeps only the top ones that capture most of the important information. This way, instead of storing all 10,000 values, we can represent the image using just 50 or 100 components. The compressed image looks almost the same to the human eye, but it takes up much less storage and is faster to process.
