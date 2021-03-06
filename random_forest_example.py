from sklearn import datasets
# from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.externals import joblib
import coremltools

# Load the iris dataset
iris = datasets.load_iris()

# Train a logistic regression
model = RandomForestClassifier()
model.fit(iris.data, iris.target)

# Make a prediction
print('prediction with scikit model:')
print(iris.target_names[model.predict([[1.0, 2.0, 2.0, 3.0]])])

# Dumping the model with joblib for comparison
joblib.dump(model, 'iris_random_forest.pkl')

# Export and save the CoreML model
coreml_model = coremltools.converters.sklearn.convert(model, iris.feature_names, 'iris class')
coreml_model.save('iris_random_forest.mlmodel')

# Load back the model
loaded_model =  coremltools.models.MLModel('iris_random_forest.mlmodel')

# You can check the model's specifications
print(loaded_model.get_spec())

input_data = {
    'sepal length (cm)': 1.0,
    'sepal width (cm)': 2.0,
    'petal length (cm)': 2.0,
    'petal width (cm)': 3.0
}
print('prediction with coreml model:')
print(loaded_model.predict(input_data))

