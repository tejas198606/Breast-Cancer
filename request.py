import requests


url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'mean radius':2,'mean texture':9,'mean perimeter':6,'mean area':2,'mean smoothness':9,
                            'mean compactness':6,'mean concavity':9,'mean concave points':9,'mean symmetry':9,
                            'mean fractal dimension':9,'radius error':9,'texture error':9,'perimeter error':9,
                          'area error':9,'smoothness error':2,'compactness error':9,'concave points error':6,'concavity error':2,
                            'symmetry error':9, 'fractal dimension error':6,'worst radius':9,'mean concave points':9,'worst texture':9,
                            'worst perimeter':9,'worst area':9,'worst smoothness':9,'worst compactness':9,
                          'worst concavity':9,'worst concave points':9,'worst symmetry':9,'worst fractal dimension':9})

print(r.json())