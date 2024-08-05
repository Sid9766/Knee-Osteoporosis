import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
from joblib import dump, load

def train():
    # Load preprocessed data
    X_train_res = load('X_train_res.joblib')
    y_train_res = load('y_train_res.joblib')

    X_train = load('X_train.joblib')
    y_train = load('y_train.joblib')
#
    X_test = load('X_test.joblib')
    y_test = load('y_test.joblib')

    # Initialize and train the random forest model
    rf_model = RandomForestClassifier(
        n_estimators=5000,
        max_features='sqrt',
        max_depth=10,
        min_samples_split=65,
        min_samples_leaf=60,
        bootstrap=True,
        random_state=24
    )
    rf_model.fit(X_train_res, y_train_res)

    # Calculate and print training accuracy
    train_accuracy = rf_model.score(X_train_res, y_train_res)
    print(f"Training Accuracy: {train_accuracy:.4f}")

    # Calculate and print test accuracy
    test_accuracy = rf_model.score(X_test, y_test)
    print(f"Test Accuracy: {test_accuracy:.4f}")

    # Evaluate model performance
    y_pred = rf_model.predict(X_test)
    print(classification_report(y_test, y_pred))

    # Save the trained model
    model_filename = "random_forest_model_smote_final.joblib"
    dump(rf_model, model_filename)

    print("Training completed and model saved.")

if __name__ == "__main__":
    train()
