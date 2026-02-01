# VCC_Assignment
Quick setup of micro service on VM 

VM 1 (ML Inference Service)
- Ubuntu Server 24.04 (ARM64)
- Python + scikit-learn
- train.py  → trains model and saves model.pkl
- app.py    → Flask REST API (/predict)

VM 2 (Client)
- Ubuntu Server 24.04 (ARM64)
- Python + requests
- client.py → calls /predict on VM 1


## ⚙️ VM 1: Train Model and Run Microservice

### 1️⃣ Activate virtual environment
```bash
cd ~/ml-service
source venv/bin/activate
```

2️⃣ Train the model (one-time step)
```bash
python train.py
```
What this does:
Trains a simple Linear Regression model
Saves the trained model as model.pkl

3️⃣ Start the inference microservice
```bash
python app.py
```
****
Expected output:
 * Running on http://0.0.0.0:5000
Keep this process running.
This VM now exposes the ML model as a REST API.

VM 2: Run Client to Get Predictions

1️⃣ Activate virtual environment
```bash
cd ~/ml-client
source venv/bin/activate
```
```bash
python client.py
```

For example Expected output:
{'prediction': 14.0}


This confirms successful distributed ML inference across VMs.


