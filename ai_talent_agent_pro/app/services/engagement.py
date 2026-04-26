import random

class EngagementAgent:
    def evaluate(self, c):
        sentiment = random.choice(["high","medium","low"])
        response_time = random.randint(1,24)
        salary_alignment = random.choice([True,False])

        return {"sentiment": sentiment, "response_time": response_time, "salary_alignment": salary_alignment}
