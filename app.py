import streamlit as st
import onnxruntime as ort
import numpy as np
from PIL import Image

# Load ONNX model
session = ort.InferenceSession("model.onnx")
input_name = session.get_inputs()[0].name

st.title("🐾 Pet Classifier (Cat vs Dog)")
st.write("Upload an image to classify")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    img = Image.open(uploaded_file).convert("RGB")
    st.image(img, caption="Uploaded Image", use_column_width=True)

    # Preprocess image
    img = img.resize((150, 150))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0).astype(np.float32)

    # Prediction
    outputs = session.run(None, {input_name: img_array})
    prediction = outputs[0][0][0]

    # Result
    if prediction > 0.5:
        st.success("🐶 Dog")
    else:
        st.success("🐱 Cat")