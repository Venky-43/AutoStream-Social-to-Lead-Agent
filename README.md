## AutoStream – Social-to-Lead Agentic Workflow

## 📌 Overview

This project is a Conversational AI Agent built as part of the Machine Learning Intern Assignment for ServiceHive.
The agent represents a fictional SaaS product called AutoStream, which provides automated video editing tools for content creators.

The goal of the project is to demonstrate how a real-world social conversation can be converted into a qualified business lead using:

## Intent detection

Retrieval-Augmented Generation (RAG)

Stateful agent workflows

Safe backend tool execution

## 📂 Project Structure

autostream-agent/
│
├── agent/
│   ├── intents.py        
│   ├── rag.py            
│   ├── tools.py         
│   ├── state.py          
│   └── graph.py          
│
├── backend/
│   └── api.py           
│
├── frontend/
│   ├── index.html       
│   ├── style.css
│   └── script.js
│
├── data/
│   └── knowledge_base.json
│
├── main.py              
├── requirements.txt
└── README.md

## ▶️ How to Run the Project Locally

## 1. Clone the Repository

git clone <>
cd autostream-agent

## 2. Create Virtual Environment (Recommended)

python -m venv venv
venv\Scripts\activate

## 3. Install Dependencies

python -m pip install --upgrade pip
python -m pip install -r requirements.txt

## 4. Start Backend Server

uvicorn backend.api:api --reload

Backend will run at:
http://127.0.0.1:8000

## 5. Run Frontend

Open the file below in a browser:

frontend/index.html

## 💬 Sample Conversation

User: Hi
Agent: Hello! How can I help you with AutoStream today?

User: What are your pricing plans?
Agent: Basic Plan: $29/month – 10 videos/month, 720p resolution
       Pro Plan: $79/month – Unlimited videos, 4K resolution, AI captions, 24/7 support

User: I want to try the Pro plan
Agent: Great! I’ll just need a few details to get you started.

User: Venky
Agent: Please share your email address.

User: venky@gmail.com
Agent: Which platform do you create content on?

User: YouTube
Agent: Thanks venky! Your free trial for AutoStream is being set up 🚀

## Backend output:

Lead captured successfully: Venky, Venky@gmail.com, YouTube

## 👤 Author

Venkannababu Kothapalli
Machine Learning Intern Applicant – ServiceHive


