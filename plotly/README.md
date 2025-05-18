
# 🛑 Stop Sign Detector (AI-powered)

This is a simple web application built using **Dash** and **PyTorch** that allows users to upload an image and get a prediction from a trained **ResNet-18** model on whether the image contains a **STOP** sign or **NOT STOP**.

## 🚀 Features

- Upload any image and get real-time predictions.
- Deep learning model trained on ResNet-18.
- Visual feedback: the prediction is overlaid directly on the uploaded image.
- User-friendly UI using Dash and Bootstrap.

---

## 🧠 Model Information

- **Architecture**: ResNet-18
- **Classes**: `STOP` (class 0), `NOT STOP` (class 1)
- **Custom Classification Head**: `model.fc = nn.Linear(512, 2)`
- The model is trained and saved as `model.pt`.

---

## 📦 Dependencies

Install all required dependencies using:

```bash
pip install dash dash-bootstrap-components torch torchvision pillow
```

You should also have a trained PyTorch model saved as `model.pt`

---

## 📁 Project Structure

```
stop-sign-detector/
├── app.py                 # Main Dash app
├── model.pt               # Trained PyTorch model (external, must be provided)
└── README.md              # You're here!
```

---

## 🧪 How It Works

1. User uploads an image via drag & drop or file selection.
2. Image is transformed using `torchvision.transforms`.
3. Image is passed through a pre-trained ResNet-18 model.
4. The app outputs one of two labels: `STOP` or `NOT STOP`.
5. The result is drawn on the image and displayed back to the user.

---

## ▶️ Run the App

```bash
python app.py
```

Then open your browser and navigate to: [http://127.0.0.1:8050](http://127.0.0.1:8050)

---

## 📝 Notes

- Ensure the model file is correctly loaded. If you encounter an error, double-check the `model.pt` path.
- The app runs on CPU (`map_location=torch.device('cpu')`) for broader compatibility.

