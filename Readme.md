# Email Spam Classification Analysis

## Task Description
The goal of this task is to develop a Python console application for email classification using a **Logistic Regression** model. The application processes email features—such as word count, links, and specific keywords—to categorize messages as either **Spam** or **Legitimate**.

---

## Data Collection
The dataset was retrieved from the provided source: [m_karukhnishvili25_43871_csv](http://max.ge/aiml_midterm/m_karukhnishvili25_43871_csv). 

---

## Method
The following steps were performed:
1.  **Data Loading**: Loaded into a Pandas DataFrame.
2.  **Splitting**: 70% Training / 30% Testing.
3.  **Model Training**: Scikit-Learn LogisticRegression.
4.  **Validation**: Evaluated using Accuracy and a Confusion Matrix.

---

## Result
The Logistic Regression model achieved high predictive performance.

### 1. Model Coefficients
| Feature | Coefficient |
| :--- | :---: |
| **Intercept** | -10.5631 |
| **words** | 0.0084 |
| **links** | 0.9554 |
| **capital_words** | 0.4872 |
| **spam_word_count** | 0.8931 |

### 2. Validation Metrics
* **Accuracy Score**: **94.93%**

---

## Visualizations



## Manual Classification Examples

### Composed Spam Email
**Text**: "URGENT! You are the lucky WINNER of a FREE cash PRIZE. Claim your money now at http://win-now-free.com."
**Explanation**: Contains a URL, multiple all-caps words, and trigger words to force a Spam classification.

### Composed Legitimate Email
**Text**: "Hi team, just a reminder that our meeting has been moved to 3 PM today. Thanks, David."
**Explanation**: Uses neutral language and zero links, correctly identified as Legitimate.
