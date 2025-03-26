import streamlit as st
import os
from PIL import Image


def load_images(folder):
    image_files = ['product.png', 'idea.png', 'base.png', 'tryon.png', 'tryon3.png']
    images = [(img, Image.open(os.path.join(folder, img))) if os.path.exists(os.path.join(folder, img)) else (img, None)
              for img in image_files]
    return images


# Root directory where images are stored
root_folder = "Trousers_alle"

st.title("Bottom Tryon View <> Pinterest Flow")

if os.path.exists(root_folder):
    subfolders = sorted(os.listdir(root_folder))

    for subfolder in subfolders:
        folder_path = os.path.join(root_folder, subfolder)
        if os.path.isdir(folder_path):
            st.subheader(subfolder)
            images = load_images(folder_path)

            cols = st.columns(5)

            for col, (filename, img) in zip(cols, images):
                if img:
                    col.image(img, use_container_width=True)
                    col.write(filename)
else:
    st.error("No images found. Please run the image download script first.")
