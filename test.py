# user_input = {#
#     'Joint Pain:': 'yes',
#     'Gender': 'male',
#     'Age': 19,
#     'Menopause Age': 0,
#     'height  (meter)': 1.82,
#     'Weight (KG) ': 64,
#     'Smoker': 'no',
#     'Alcoholic': 'no',
#     'Diabetic': 'no',
#     'Hypothyroidism': 'no',
#     'Seizer Disorder': 'no',
#     'Occupation ': 'student',
#     'History of Fracture': 'no',
#     'Dialysis:': 'no',
#     'Family History of Osteoporosis': 'yes',
#     'Maximum Walking distance (km)': 3,
#     'Daily Eating habits': 'balanced',
#     'Medical History': 'none',
#     'T-score Value': -1.0,
#     'BMI: ': 18.9,
#     'Obesity': 'under weight'
# }
user_input = {
    'Joint Pain:': 'no',  # Osteopenia can be associated with joint pain
    'Gender': 'male',
    'Age': 54,  # Increasing the age as osteopenia is more common in older adults
    'Menopause Age': -1,  # Post-menopausal age
    'height  (meter)': 1.75,  # Adjusting height
    'Weight (KG) ': 67,  # Lower weight can be a risk factor
    'Smoker': 'no',  # Smoking is a risk factor
    'Alcoholic': 'no',  # Alcohol consumption is a risk factor
    'Diabetic': 'no',  # Diabetes can be a risk factor
    'Hypothyroidism': 'no',  # Hypothyroidism can be a risk factor
    'Seizer Disorder': 'no',  # Not specifically a risk factor for osteopenia
    'Occupation ': 'sedentary',  # Sedentary lifestyle can be a risk factor
    'History of Fracture': 'no',  # Previous fractures can indicate weaker bones
    'Dialysis:': 'no',  # Dialysis is not directly related to osteopenia
    'Family History of Osteoporosis': 'yes',  # Family history is a strong risk factor
    'Maximum Walking distance (km)': 3,  # Lower walking distance might indicate poorer bone health
    'Daily Eating habits': 'balanced',  # Poor nutrition can contribute to bone density issues
    'Medical History': 'none',  # Explicit medical history related to bone health
    'T-score Value': -1.0,  # Adjusting T-score to reflect osteopenia
    'BMI: ': 21.9,  # Lower BMI is a risk factor
    'Obesity': 'under weight'  # Underweight can be a risk factor
}
# user_input = {
#     'Joint Pain:': 'no',  # Osteopenia can be associated with joint pain
#     'Gender': 'male',
#     'Age': 20,  # Increasing the age as osteopenia is more common in older adults
#     'Menopause Age': -1,  # Post-menopausal age
#     'height  (meter)': 1.88,  # Adjusting height
#     'Weight (KG) ': 76,  # Lower weight can be a risk factor
#     'Smoker': 'no',  # Smoking is a risk factor
#     'Alcoholic': 'no',  # Alcohol consumption is a risk factor
#     'Diabetic': 'no',  # Diabetes can be a risk factor
#     'Hypothyroidism': 'no',  # Hypothyroidism can be a risk factor
#     'Seizer Disorder': 'no',  # Not specifically a risk factor for osteopenia
#     'Occupation ': 'sedentary',  # Sedentary lifestyle can be a risk factor
#     'History of Fracture': 'no',  # Previous fractures can indicate weaker bones
#     'Dialysis:': 'no',  # Dialysis is not directly related to osteopenia
#     'Family History of Osteoporosis': 'yes',  # Family history is a strong risk factor
#     'Maximum Walking distance (km)': 1,  # Lower walking distance might indicate poorer bone health
#     'Daily Eating habits': 'unbalanced',  # Poor nutrition can contribute to bone density issues
#     'Medical History': 'none',  # Explicit medical history related to bone health
#     'T-score Value': -1.0,  # Adjusting T-score to reflect osteopenia
#     'BMI: ': 21.3,  # Lower BMI is a risk factor
#     'Obesity': 'under weight'  # Underweight can be a risk factor
# }



def test():
    return user_input

if __name__ == "__main__":
    test()
