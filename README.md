# 🐾 Pet Image Classifier (Cat vs Dog)

## 📌 Project Overview

This project is a deep learning-based image classification system that identifies whether an uploaded image is a **cat 🐱 or a dog 🐶**.
It uses a Convolutional Neural Network (CNN) trained on a custom dataset and is deployed using a Streamlit web application.

---

## 🎯 Objectives

* Build a CNN model for image classification
* Train and evaluate the model using a custom dataset
* Convert the trained model into ONNX format
* Deploy the model using Streamlit for real-time predictions

---

## 🛠️ Technologies Used

* Python
* TensorFlow / Keras
* ONNX & ONNX Runtime
* Streamlit
* NumPy, Matplotlib, Pillow

---

## 📂 Dataset

* Custom dataset with two classes:

  * Cats
  * Dogs
* Images are preprocessed (resized to 150×150 and normalized)

---

## 🧠 Model Architecture

* Convolutional Layers (Conv2D)
* MaxPooling Layers
* Fully Connected Dense Layers
* Sigmoid Activation (Binary Classification)

---

## ⚙️ Features

* Image upload interface
* Real-time prediction
* Displays classification result (Cat/Dog)
* Lightweight ONNX model for fast inference

---

## 📊 Model Performance

* Training Accuracy: ~72%
* Validation Accuracy: ~71%

---

## 🚀 How to Run

### 1. Install dependencies

```
pip install streamlit onnxruntime pillow numpy
```

### 2. Run the app

```
streamlit run app.py
```

---

## 📸 Usage

1. Upload an image (jpg/png)
2. Model processes the image
3. Output displays whether it is a cat or dog

---

## 📁 Project Structure

```
project/
│── app.py
│── model.onnx
│── dataset/
│   ├── cats/
│   └── dogs/
```

---

## 💡 Future Improvements

* Add more classes (rabbit, hamster, etc.)
* Improve accuracy with more data
* Deploy online (Streamlit Cloud)
* Add real-time camera detection

---

## 🙌 Conclusion

This project demonstrates the implementation of deep learning for image classification along with model deployment using modern tools like ONNX and Streamlit.

---

