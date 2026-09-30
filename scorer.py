# import bm25s ?


def judge(question, expects, answer, results) -> bool:

    if not expects:
        return False

    # try splitting the expects answer by comma and seeing how many of them make it into the 
    # generated answer? if majority made it in i guess thats a good answer? 
    # bm25s could also be good i guess

    phrases = expects.split(', ')
    count = 0

    for phrase in phrases:
        if phrase.strip().lower() in answer.strip().lower():
            count += 1

    print()
    print()
    print('generated answer:', answer)
    print()
    print('right answer?', count == len(phrases))
    print()
    print()
    
    return count == len(phrases)