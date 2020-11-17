# MLflow Example

This repo contains a demo of mlflow package which is an open source platform for managing the end-to-end machine learning lifecycle.
To read more about mlflow visit [MLflow](https://mlflow.org/docs/latest/index.html)

## Steps to run:
  - Build a virtual environment to install the required packages.
  - Install the required packages listed in [req.txt](https://github.com/hardymunjal/mlflow-example/blob/main/req.txt) using command:
  
    `
    pip install -r req.txt
    `
  - After activating the virtual environment, run the mlflow tracking dashboard using command:
  
    `
    mlflow ui --default-artifact-root ./model_data/ --backend-store-uri ./model_data/
    `
    
    This runs a server on 5000 by default. You can read more about arguments of command [here](https://mlflow.org/docs/latest/tracking.html#tracking-ui)

  - Visit http://localhost:5000 to view the dashboard.
  
You can play around with the experiment "Dummy_Data_LR" details there.
