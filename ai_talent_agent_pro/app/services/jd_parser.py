import re

class JDParser:
    SKILLS_DB = ["python","flask","django","machine learning","deep learning","sql","java","react"]

    def parse(self, jd_text):
        jd = jd_text.lower()
        skills = [s for s in self.SKILLS_DB if s in jd]

        exp = re.findall(r'(\d+)[-–](\d+)', jd)
        exp_range = (0,5)
        if exp:
            exp_range = (int(exp[0][0]), int(exp[0][1]))

        return {"skills": skills, "experience": exp_range, "raw_text": jd}
