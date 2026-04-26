import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class Matcher:
    def __init__(self):
        with open("data/candidates.json") as f:
            self.candidates = json.load(f)

    def match(self, jd):
        docs = [jd["raw_text"]]

        for c in self.candidates:
            docs.append((" ".join(c["skills"]) + " " + c["bio"]).lower())

        vectorizer = TfidfVectorizer()
        vectors = vectorizer.fit_transform(docs)

        sims = cosine_similarity(vectors[0], vectors[1:])[0]

        results = []
        for i, c in enumerate(self.candidates):
            overlap = list(set(jd["skills"]) & set(map(str.lower, c["skills"])))
            skill_score = len(overlap) / max(len(jd["skills"]), 1)

            exp_min, exp_max = jd["experience"]
            exp_score = 1 if exp_min <= c["experience"] <= exp_max else 0.5

            match_score = (0.5*sims[i] + 0.3*skill_score + 0.2*exp_score) * 100

            results.append({
                "name": c["name"],
                "match_score": round(match_score,2),
                "explanation": {
                    "skills": overlap,
                    "exp_fit": exp_score,
                    "semantic": round(sims[i],2)
                }
            })

        return results
