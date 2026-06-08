# Saksham AI

AI-Powered Educational Assistant for Personalized Learning

## Overview

Saksham AI is an educational AI system designed to convert study material into student-friendly explanations.

The system accepts educational PDFs and automatically:

* Extracts text and concepts
* Detects topics
* Adapts explanations according to student class level
* Generates learning objectives
* Creates memory tricks
* Builds simple flowcharts
* Generates conceptual questions and answers
* Explains diagrams from image-based PDFs
* Supports multilingual learning

The goal is to make learning easier for students from different academic levels while maintaining educational accuracy.

---

## Current Features

### PDF Processing

* PDF text extraction
* Multi-page support
* Character count analysis

### Content Understanding

* Document classification

  * Notes
  * Chapter
  * Assignment
  * Exam

* Topic extraction

* Concept extraction

* Difficult word identification

### Student Personalization

Supports:

* Class 6
* Class 7
* Class 8
* Class 9
* Class 10

Explanations are automatically adjusted according to the selected level.

### Language Support

* English
* Hindi
* Auto Language Detection

### Learning Support

* Simplified explanations
* Learning objectives
* Memory tricks
* Conceptual questions
* Answer generation
* Educational dictionary

### Diagram Mode

For image-heavy PDFs:

* Image extraction
* OCR-based text detection
* Diagram classification
* Diagram explanation

Supported examples:

* Plant Cell
* Animal Cell
* Human Heart
* Water Cycle
* Solar System
* Photosynthesis

### RAG Pipeline

Implemented Components:

* Chunking
* Embedding Generation
* FAISS Vector Search
* Context Retrieval
* Confidence Scoring

### Flowchart Generation

Automatic concept-based flowchart generation from extracted concepts.

---

## Tech Stack

### AI Models

* Llama 3.2 1B (Ollama)

### Embeddings

* all-MiniLM-L6-v2

### Vector Database

* FAISS

### OCR

* Tesseract OCR

### PDF Processing

* PyMuPDF (fitz)

### Programming Language

* Python

---

## Project Structure

src/

├── main.py

├── pdf_reader.py

├── classifier.py

├── topic_extractor.py

├── concept_extractor.py

├── learning_objectives.py

├── auto_flowchart.py

├── language_detector.py

├── student_level.py

├── teacher_engine.py

├── translator.py

├── rag_engine.py

├── embedder.py

├── vector_store.py

├── retriever.py

├── confidence_scorer.py

├── diagram_extractor.py

├── diagram_classifier.py

└── diagram_explainer.py

---

## Current Workflow

PDF Input

↓

Text Extraction

↓

Topic Detection

↓

Concept Extraction

↓

RAG Retrieval

↓

Student-Level Adaptation

↓

Explanation Generation

↓

Memory Tricks

↓

Questions & Answers

↓

Final Learning Output

---

## Future Development

* FastAPI Backend
* React Frontend
* Voice Input Support
* Speech-to-Text
* Interactive Chat Interface
* Offline Deployment on Edge Devices
* Better Diagram Understanding
* Multilingual Expansion
* Learning Analytics Dashboard
* Jetson Deployment Optimization

---

## Team Notes

Current repository contains the core educational AI pipeline.

Frontend and API integration are under development.

Collaborators should create separate branches for new features and open pull requests before merging into main.

---

## Status

Current Stage: Core AI Pipeline Implemented

Next Stage: Backend API + Frontend Integration
