from flask import Flask, request, render_template_string
import json, random, re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load candidates
with open("data/candidates.json") as f:
    candidates = json.load(f)

# HTML UI inside Python (no template issues)
HTML = """
<!DOCTYPE html>
<html>
<head>
<title>AI Talent Agent</title>
<style>
body {font-family: Arial; background:#eef2f7; padding:40px;}
.container {background:white; padding:25px; border-radius:10px;}
textarea {width:100%; height:120px;}
button {margin-top:10px; padding:10px 20px; background:black; color:white;}
table {width:100%; margin-top:20px; border-collapse:collapse;}
th,td {padding:10px; border-bottom:1px solid #ddd;}
.bar {height:8px; background:#ddd;}
.fill {height:100%; background:green;}
</style>
</head>
<body>

<div class="container">
<h2>AI Talent Scouting Agent</h2>

<form method="POST">
<textarea name="jd" placeholder="Paste Job Description here..."></textarea>
<br>
<button type="submit">Analyze</button>
</form>

{% if results %}
<table>
<tr>
<th>Rank</th><th>Name</th><th>Match</th><th>Interest</th><th>Final</th><th>Skills</th>
</tr>

{% for c in results %}
<tr>
<td>{{loop.index}}</td>
<td>{{c.name}}</td>
<td>
<div class="bar"><div class="fill" style="width:{{c.match_score}}%"></div></div>
{{c.match_score}}
</td>
<td>
<div class="bar"><div class="fill" style="width:{{c.interest_score}}%"></div></div>
{{c.interest_score}}
</td>
<td>
<div class="bar"><div class="fill" style="width:{{c.final_score}}%"></div></div>
{{c.final_score}}
</td>
<td>{{c.skills}}</td>
</tr>
{% endfor %}
</table>
{% endif %}

</div>
</body>
</html>
"""

def parse_jd(jd):
    jd = jd.lower()
    skills_db = ["python","flask","django","machine learning","java","sql"]
    skills = [s for s in skills_db if s in jd]

    exp = re.findall(r'(\\d+)[-–](\\d+)', jd)
    exp_range = (0,5)
    if exp:
        exp_range = (int(exp[0][0]), int(exp[0][1]))

    return {"skills": skills, "experience": exp_range, "text": jd}

def match(jd):
    docs = [jd["text"]]
    for c in candidates:
        docs.append((" ".join(c["skills"]) + " " + c["bio"]).lower())

    vec = TfidfVectorizer()
    vectors = vec.fit_transform(docs)

    sims = cosine_similarity(vectors[0], vectors[1:])[0]

    results = []
    for i,c in enumerate(candidates):
        overlap = list(set(jd["skills"]) & set(map(str.lower,c["skills"])))
        skill_score = len(overlap)/max(len(jd["skills"]),1)

        exp_min, exp_max = jd["experience"]
        exp_score = 1 if exp_min<=c["experience"]<=exp_max else 0.5

        match_score = (0.5*sims[i]+0.3*skill_score+0.2*exp_score)*100

        results.append({
            "name":c["name"],
            "match_score":round(match_score,2),
            "skills":", ".join(overlap)
        })

    return results

@app.route("/", methods=["GET","POST"])
def home():
    results = None

    if request.method == "POST":
        jd = request.form["jd"]

        parsed = parse_jd(jd)
        matches = match(parsed)

        final = []
        for m in matches:
            interest = random.randint(30,90)
            score = 0.6*m["match_score"] + 0.4*interest

            final.append({
                "name": m["name"],
                "match_score": m["match_score"],
                "interest_score": interest,
                "final_score": round(score,2),
                "skills": m["skills"]
            })

        final.sort(key=lambda x:x["final_score"], reverse=True)
        results = final

    return render_template_string(HTML, results=results)

if __name__ == "__main__":
    app.run(debug=True)
