# AI-Powered Talent Scouting & Engagement Agent

## Overview

This project is an AI-driven recruitment system that automates job description analysis, candidate matching, conversational engagement, and ranking. It helps recruiters quickly identify suitable and interested candidates using a dual scoring system.

---

## Features

* Job Description parsing and skill extraction
* Candidate profile matching using skill similarity
* Explainable match scoring
* Simulated conversational engagement with candidates
* Interest scoring based on responses
* Final ranked shortlist generation

---

## Working Flow

1. Recruiter inputs Job Description
2. System extracts required skills and experience
3. Candidate profiles are matched from dataset
4. AI agent engages candidates through simulated conversation
5. Interest score is calculated
6. Final ranking is generated using combined score

---

## Scoring System

### Match Score

Based on:

* Skill overlap
* Experience relevance

### Interest Score

Based on:

* Candidate response in simulated conversation
* Engagement level

### Final Score

Weighted combination of both scores:

```
Final Score = Match Score + Interest Score
```

---

## Sample Input

### Job Description

Looking for Python Flask developer with Machine Learning, 0-2 years experience

---

## Tech Stack

* Python
* Flask / FastAPI
* NLP libraries (spaCy / Transformers)
* MySQL / MongoDB
* HTML, CSS, JavaScript (optional frontend)

---

## Project Structure

```
ai-talent-scouting-agent/
│
├── app.py
├── requirements.txt
├── models/
├── utils/
├── routes/
├── database/
├── templates/
├── static/
└── README.md
```

---

## Setup Instructions

```bash
git clone https://github.com/your-username/ai-talent-scouting-agent.git
cd ai-talent-scouting-agent
```

```bash
python -m venv venv
venv\Scripts\activate
```

```bash
pip install -r requirements.txt
python app.py
```

---

## Output

The system generates a ranked shortlist of candidates with:

* Match Score
* Interest Score
* Final Ranking

---

## Future Improvements

* Real-time chat using LLMs
* LinkedIn integration
* Advanced semantic matching
* Bias detection in recruitment
* Dashboard for recruiters

---

## Author

AI Talent Scouting & Engagement System Project

---

## working link

https://aitalentagentprozip--rasalaarchu1.replit.app

---
