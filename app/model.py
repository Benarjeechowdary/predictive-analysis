import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, f1_score
import pickle

# Path to save the trained model
MODEL_PATH = "app/data/model.pkl"

def train_model(data):
    X = data.drop(columns=["Downtime"])
    y = data["Downtime"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    model = DecisionTreeClassifier(    
    random_state=42,    # For reproducibility
    )
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    metrics = {
        "accuracy": accuracy_score(y_test, y_pred),
        "f1_score": f1_score(y_test, y_pred,)
    }
    
    with open(MODEL_PATH, "wb") as f:
        pickle.dump(model, f)

    return metrics

def make_prediction(input_data):
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
    
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)
    confidence = max(model.predict_proba(df)[0])
    
    return {"Downtime": "Yes" if prediction[0] == 1 else "No", "Confidence": confidence}
