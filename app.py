import os
from flask import Flask, render_template, request
from models import Session, Lead
from ai import classify_lead, generate_reply
from scheduler import start_scheduler

app = Flask(__name__)
start_scheduler()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/submit", methods=["POST"])
def submit():
    data = request.form

    category = classify_lead(data["message"])
    reply = generate_reply(data["message"])
    print("AI AUTO REPLY:", reply)

    db = Session()
    lead = Lead(
        name=data["name"],
        email=data["email"],
        phone=data["phone"],
        product=data["product"],
        message=data["message"],
        category=category,
        status="new"
    )
    db.add(lead)
    db.commit()
    db.close()

    return "Inquiry received. We will contact you soon."

@app.route("/admin")
def admin():
    db = Session()
    leads = db.query(Lead).all()
    db.close()
    return render_template("admin.html", leads=leads)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)