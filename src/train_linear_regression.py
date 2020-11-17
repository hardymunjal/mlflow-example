import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np
import mlflow

from sklearn.linear_model import LinearRegression
from get_path import path_to_model_data

mlflow.set_tracking_uri("file:///"+str(path_to_model_data))
mlflow.set_registry_uri("file:///"+str(path_to_model_data))

print("Tracking URI: ", mlflow.get_tracking_uri())
print("Registry URI: ", mlflow.get_registry_uri())

mlflow.set_experiment("Dummy_Data_LR")
mlflow.start_run()

run = mlflow.active_run()

print("Current Run id: ",run.info.run_id)

mlflow.autolog(log_input_examples=True)
rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = 2 * x - 5 + rng.randn(50)
plt.scatter(x, y)
plt.savefig("./output_images/ScatterPlot.png")
mlflow.log_artifact("./output_images/ScatterPlot.png")

model = LinearRegression(fit_intercept=True)

model.fit(x[:, np.newaxis], y)

xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.savefig("./output_images/LinearRegressionModel.png")
mlflow.log_artifact("./output_images/LinearRegressionModel.png")
mlflow.end_run()