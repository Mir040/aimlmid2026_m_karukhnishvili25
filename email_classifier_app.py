import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score

def run_application():
    # --- 1. Data Loading and Processing ---
    # Load the dataset (Ensure the file is in the same directory)
    df = pd.read_csv('m_karukhnishvili25_43871.csv')
    
    X = df[['words', 'links', 'capital_words', 'spam_word_count']]
    y = df['is_spam']

    # Split: 70% Training, 30% Testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    # --- 2. Model Creation and Training ---
    model = LogisticRegression()
    model.fit(X_train, y_train)

    # --- 3. Validation ---
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)

    print("--- Model Performance ---")
    print(f"Accuracy: {acc:.4f}")
    print(f"Confusion Matrix:\n{cm}")
    print(f"Coefficients: {dict(zip(X.columns, model.coef_[0]))}")
    print(f"Intercept: {model.intercept_[0]}")

    # --- 4. Visualizations ---
    # Visualization A: Confusion Matrix Heatmap
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Legit', 'Spam'], yticklabels=['Legit', 'Spam'])
    plt.title('Confusion Matrix Heatmap')
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.show()

    # Visualization B: Feature Importance (Coefficients)
    plt.figure(figsize=(8, 5))
    plt.bar(X.columns, model.coef_[0], color='teal')
    plt.title('Feature Importance (Logistic Regression Coefficients)')
    plt.ylabel('Coefficient Value')
    plt.show()

    # --- 5. Email Text Parser & Checker ---
    def check_email(text):
        words_list = text.split()
        word_count = len(words_list)
        # Regex to count links
        links = len(re.findall(r'http[s]?://\S+', text))
        # Count words that are entirely uppercase
        capitals = sum(1 for w in words_list if w.isupper() and len(w) > 1)
        
        # Simple list of keywords based on common spam patterns
        triggers = ['prize', 'winner', 'free', 'urgent', 'cash', 'money', 'offer', 'congratulations']
        spam_word_count = sum(1 for w in words_list if w.lower() in triggers)
        
        features = [[word_count, links, capitals, spam_word_count]]
        pred = model.predict(features)
        
        print(f"\nExtracted Features: Words: {word_count}, Links: {links}, Capitals: {capitals}, Spam Words: {spam_word_count}")
        return "SPAM" if pred[0] == 1 else "LEGITIMATE"

    # Testing the manual input
    print("\n--- Manual Email Check ---")
    user_email = input("Paste email text to check: ")
    print(f"Classification Result: {check_email(user_email)}")

if __name__ == "__main__":
    run_application()