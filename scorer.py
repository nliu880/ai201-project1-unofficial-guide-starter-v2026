import config
import questions

question = questions.QUESTIONS


def judge(questions, expects, answer, results) -> bool:

    if not expects:
        return False
    
    return expects.strip().lower() in (answer or "".lower)