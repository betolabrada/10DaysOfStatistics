import numpy as np
from sklearn.linear_model import LinearRegression


x = np.array([95, 85, 80, 70, 60]).reshape((-1, 1))
y = np.array([85, 95, 70, 65, 70])

model = LinearRegression().fit(x, y)

print(model.predict(80))