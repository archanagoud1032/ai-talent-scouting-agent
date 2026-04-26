from flask import Blueprint, request, jsonify, render_template

from app.services.jd_parser import JDParser
from app.services.matcher import Matcher
from app.services.engagement import EngagementAgent
from app.services.scorer import Scorer

main = Blueprint("main", __name__)

@main.route("/")
def home():
    return render_template("index.html")

@main.route("/process", methods=["POST"])
def process():
    jd_text = request.form.get("jd")

    parser = JDParser()
    matcher = Matcher()
    engagement = EngagementAgent()
    scorer = Scorer()

    parsed_jd = parser.parse(jd_text)
    candidates = matcher.match(parsed_jd)

    results = []

    for c in candidates:
        interest = engagement.evaluate(c)
        scored = scorer.compute(c, interest)
        results.append(scored)

    results.sort(key=lambda x: x["final_score"], reverse=True)

    return jsonify(results)