import pandas as pd
from joblib import load
from sklearn.preprocessing import LabelEncoder
#
# Import functions from other scripts
from preprocess import preprocess
from train import train
from test import test

def predict():
    # Run preprocessing
    preprocess()
    
    # Run training
    train()
    
    # Get user input from test
    user_input = test()
    
    # Load the saved random forest model and label encoders
    model = load('random_forest_model_smote_final.joblib')
    label_encoders = load('label_encoders.joblib')

    # Convert the user input to a DataFrame
    user_df = pd.DataFrame([user_input])

    # Handle missing values if any
    user_df['Menopause Age'] = user_df['Menopause Age'].fillna(0)

    # Encode categorical variables using the loaded label encoders
    for col in user_df.columns:
        if user_df[col].dtype == object:
            le = label_encoders.get(col, None)
            if le:
                user_df[col] = user_df[col].map(lambda s: le.transform([s])[0] if s in le.classes_ else -1)
            else:
                # Handle new categories not seen during training
                user_df[col] = -1  # Or use a default value that makes sense in your context

    # Make predictions using the loaded model
    prediction = model.predict(user_df)

    # Output the prediction
    if prediction[0] == 0:
        print("Diagnosis: Osteopenia")
    elif prediction[0] == 1:
        print("Diagnosis: Normal")
    else:
        print("Diagnosis: Osteoporosis")

if __name__ == "__main__":
    predict()
