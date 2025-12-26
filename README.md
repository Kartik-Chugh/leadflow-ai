# LeadFlow AI – AI-Powered Lead Capture & Automation System

## Problem Statement
Material brands (flooring, laminates, lighting, etc.) invest heavily in marketing but lose a significant number of leads due to delayed responses, lack of prioritization, and absence of follow-up systems. This project addresses the problem of **lost leads** by building a lightweight, automated lead management workflow.

---

## Solution Overview
LeadFlow AI is a web-based automation system that:
- Captures website inquiries
- Uses AI to classify leads as **Hot / Warm / Cold**
- Stores leads in a database
- Provides an admin dashboard for sales teams
- Ensures graceful fallback when AI services are unavailable

The system is designed using **free and open-source tools**, with a focus on reliability and simplicity.

---

## Key Features
- Website inquiry form
- AI-based lead classification (Hugging Face – free inference API)
- Automated prioritization of leads
- Admin dashboard to view leads
- Background follow-up scheduler
- Secure handling of API keys using environment variables

---

## Tech Stack
- **Backend:** Python, Flask
- **Database:** SQLite
- **AI:** Hugging Face Zero-Shot Classification (free tier)
- **Automation:** APScheduler
- **Frontend:** HTML (Jinja templates)
- **Deployment:** Render (planned)

---

## System Architecture (High Level)
1. User submits inquiry via website form  
2. Backend stores inquiry in database  
3. AI service classifies inquiry (Hot/Warm/Cold)  
4. Admin dashboard displays leads  
5. Scheduler handles follow-up reminders  

*(Detailed architecture diagram provided below)*

---

## Project Structure
