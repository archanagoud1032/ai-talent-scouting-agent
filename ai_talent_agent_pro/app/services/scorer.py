class Scorer:
    def compute(self, c, e):
        score = 0

        if e["sentiment"]=="high": score+=60
        elif e["sentiment"]=="medium": score+=40
        else: score+=20

        if e["response_time"]<6: score+=20
        if e["salary_alignment"]: score+=20

        final = 0.6*c["match_score"] + 0.4*score

        return {
            "name": c["name"],
            "match_score": c["match_score"],
            "interest_score": score,
            "final_score": round(final,2),
            "explanation": c["explanation"]
        }
