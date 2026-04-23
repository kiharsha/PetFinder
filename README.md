# PetFinder: Image-Based Lost Pet Retrieval System

## Overview
PetFinder is an image-based pet classification and retrieval system designed to assist in locating lost pets and supporting pet adoption. The system enables users to upload images of lost or found pets (specifically cats and dogs) and search for visually similar pets using deep learning–based image matching.

This project leverages MobileNetV2 for feature extraction and cosine similarity for content-based image retrieval, wrapped in a full-stack Django web application. The system was designed, implemented, tested, and deployed end-to-end as an academic course project.

## Objectives
- Enable image-based search for lost and found pets
- Match the same pet across images captured under different conditions
- Provide a lightweight and easy-to-use pet search platform
- Demonstrate the use of pretrained CNN embeddings for real-world retrieval tasks

## System Architecture
The application follows a client–server architecture:
- Frontend: Django templates
- Backend: Django views and models
- Database: SQLite
- ML Model: MobileNetV2 (feature extraction)
- Matching: Cosine similarity over embeddings

Workflow:
1. User uploads a pet image
2. Image is processed through MobileNetV2
3. Feature embedding is extracted
4. Embedding is stored or compared against existing embeddings
5. Top-k similar pets are retrieved

## Model Details
- Model: MobileNetV2
- Usage: Feature extraction (classification head removed)
- Rationale: Lightweight, efficient, and suitable for deployment
- Similarity Metric: Cosine similarity

## Dataset
- Images of cats and dogs collected from publicly available online sources
- Includes multiple breeds and image variations
- Designed to evaluate real-world matching challenges

## Technologies Used
- Python
- Django
- SQLite
- TensorFlow / Keras
- OpenCV, PIL
- NumPy

## How to Run the Project
1. Clone the repository
   git clone https://github.com/your-username/petfinder.git
   cd petfinder

2. Create and activate a virtual environment
   python -m venv venv
   source venv/bin/activate  (Linux/Mac)
   venv\Scripts\activate (Windows)

3. Install dependencies
   pip install -r requirements.txt

4. Run database migrations
   python manage.py migrate

5. Start the server
   python manage.py runserver

Access the application at http://127.0.0.1:8000/

## Evaluation
- Metric: Top-k retrieval accuracy
- Analysis: Quantitative metrics and qualitative inspection
- Observations: Strong performance for distinct pets; challenges with visually similar pets

## Contributions
- Project ideation and design
- Dataset collection and preprocessing
- System implementation and testing
- Integration of MobileNetV2
- Evaluation and deployment

## Future Work
- Fine-tuning on pet-specific datasets
- Metadata-enhanced search
- Scalable nearest-neighbor retrieval
- Mobile and edge deployment

## Acknowledgement
Large Language Models were used for assistance with documentation clarity and structure. All system design, implementation, experimentation, and deployment were performed by the author.

## Contact
Author: Kiran Vydhyam
Email: kvydhyam@purdue.edu
