import pandas as pd
from sklearn.preprocessing import LabelEncoder
from imblearn.over_sampling import SMOTE
import joblib
from sklearn.model_selection import train_test_split
from joblib import dump
#
def preprocess():
    # Load the original dataset
    df = pd.read_csv("patient details.csv")

    # Custom function to fill NaN values based on gender
    def fill_values(row):
        if row['Gender'] == 'female':
            if pd.isnull(row['Menopause Age']):
                row['Menopause Age'] = 0
                row['Number of Pregnancies'] = 0
        elif row['Gender'] == 'male':
            if pd.isnull(row['Menopause Age']):
                row['Menopause Age'] = -1
                row['Number of Pregnancies'] = -1
        return row

    # Apply the custom function to each row
    df = df.apply(fill_values, axis=1)

    # Drop any remaining rows with null values
    cleaned_df = df.dropna()

    # Replace specific values in 'Obesity' column
    cleaned_df['Obesity'] = cleaned_df['Obesity'].replace(to_replace={'overweight': 'over weight', 'underweight': 'under weight', ' normalweight': 'normal weight'})

    # Map 'Diagnosis' to numerical values
    diagnosis_mapping = {'osteopenia': 0, 'normal': 1, 'osteoporosis': 2}
    cleaned_df['Diagnosis'] = cleaned_df['Diagnosis'].map(diagnosis_mapping)

    # Drop unnecessary columns
    cleaned_df = cleaned_df.drop(columns=['S.No', 'Patient Id', 'Site', 'Number of Pregnancies', 'Z-Score Value', 'Estrogen Use'])

    # Separate features and target variable
    X = cleaned_df.drop(columns=['Diagnosis'])
    y = cleaned_df['Diagnosis']

    # Identify categorical and numerical columns
    cat_cols = [col for col in X.columns if X[col].dtype == 'object']
    num_cols = [col for col in X.columns if X[col].dtype != 'object']

    # Create and fit LabelEncoders for categorical columns
    label_encoders = {}
    for col in cat_cols:
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col].astype(str))
        label_encoders[col] = le

    # Frequency encoding for Daily Eating habits
    daily_eating_freq = cleaned_df['Daily Eating habits'].value_counts(normalize=True)
    cleaned_df['Daily Eating habits'] = cleaned_df['Daily Eating habits'].map(daily_eating_freq)

    # Frequency encoding for Medical History
    medical_history_freq = cleaned_df['Medical History'].value_counts(normalize=True)
    cleaned_df['Medical History'] = cleaned_df['Medical History'].map(medical_history_freq)

    # Frequency encoding for Obesity
    obesity_freq = cleaned_df['Obesity'].value_counts(normalize=True)
    cleaned_df['Obesity'] = cleaned_df['Obesity'].map(obesity_freq)

    for col in cat_cols:
        le = LabelEncoder()
        cleaned_df[col] = le.fit_transform(cleaned_df[col].astype(str))
        label_encoders[col] = le

    # Save the encoders for later use
    joblib.dump(label_encoders, 'label_encoders.joblib')

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.35, random_state=42)

    # Apply SMOTE to the training data
    smote = SMOTE(random_state=42)
    X_train_res, y_train_res = smote.fit_resample(X_train, y_train)

    # Save the preprocessed data
    dump(X_train_res, 'X_train_res.joblib')
    dump(y_train_res, 'y_train_res.joblib')

    dump(X_train, 'X_train.joblib')
    dump(y_train, 'y_train.joblib')

    dump(X_test, 'X_test.joblib')
    dump(y_test, 'y_test.joblib')

    print("Preprocessing completed.")

if __name__ == "__main__":
    preprocess()
