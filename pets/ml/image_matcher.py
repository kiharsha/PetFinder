import os
import numpy as np
from tensorflow.keras.applications.mobilenet_v2 import MobileNetV2, preprocess_input
from tensorflow.keras.preprocessing import image
from sklearn.metrics.pairwise import cosine_similarity

model = MobileNetV2(weights='imagenet', include_top=False, pooling='avg')

FEATURE_CACHE={}

def extract_features(img_path):
    img = image.load_img(
        img_path,
        target_size=(224, 224),
        color_mode='rgb'   
    )
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    features = model.predict(img_array)
    features = features.flatten()
    features = features / np.linalg.norm(features)
    return features

def match_image(input_image_path, gallery_image_paths, threshold=0.65):
    input_features = extract_features(input_image_path)

    best_score = 0
    best_match_path = None

    print("\n--- IMAGE MATCHING DEBUG ---")
    print(f"Input image: {input_image_path}")
    print(f"Number of gallery images: {len(gallery_image_paths)}\n")

    for path in gallery_image_paths:
        if path not in FEATURE_CACHE:
            FEATURE_CACHE[path] = extract_features(path)

        gallery_features = FEATURE_CACHE[path]

        score = cosine_similarity(
            [input_features], [gallery_features]
        )[0][0]

        print(f"Comparing with: {path}")
        print(f"Similarity score: {score:.4f}\n")

        if score > best_score:
            best_score = score
            best_match_path = path

    print(f">>> BEST MATCH SCORE: {best_score:.4f}")
    print(f">>> BEST MATCH PATH: {best_match_path}")
    print("--- END DEBUG ---\n")

    if best_score >= threshold:
        return True, best_match_path, best_score
    else:
        return False, None, best_score
