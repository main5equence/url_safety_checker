from flask import Flask, render_template, request

app = Flask(__name__)

# Words that often appear in phishing or suspicious links
suspicious_words = ["login", "verify", "update", "secure", "paypal", "bank", "alert", "confirm"]

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        url = request.form["url"]

        assessment = []

        # Check for HTTPS
        if not url.startswith("https://"):
            assessment.append("❗ No HTTPS – the connection may be insecure.")

        # Check for suspicious words
        for word in suspicious_words:
            if word in url.lower():
                assessment.append(f"⚠️ Suspicious word detected: **{word}**")

        # If no warnings
        if not assessment:
            result = "✅ The link appears safe (at first glance)."
        else:
            result = "🚨 Warning!\n" + "\n".join(assessment)

    return render_template("index.html", result=result)

if __name__ == "__main__":
    import os
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
