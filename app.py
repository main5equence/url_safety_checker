from flask import Flask, render_template, request

app = Flask(__name__)

suspicious_words = ["login", "verify", "update", "secure", "paypal", "bank", "alert", "confirm", "pay","trust"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]

        assessment = []

        if not url.startswith("https://"):
            assessment.append("❗ No HTTPS – the connection may be insecure.")

        for word in suspicious_words:
            if word in url.lower():
                assessment.append(f"⚠️ Suspicious word detected: **{word}**")

        if not assessment:
            result = "✅ The link appears safe (at first glance)."
        else:
            result = "🚨 Warning!\n" + "\n".join(assessment)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
