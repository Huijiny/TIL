def solution(table, languages, preference):
    answer = ''
    tab = {}
    for t in table:
        job = t.split(" ")[0]
        langs = t.split(" ")[1:]
        langs.reverse()
        tab[job] = langs
    # print(tab)
    max_total = 0
    for job, langs in tab.items():
        total = 0
        for language in languages:
            if not language in langs:
                lan_grade = 0
            else:
                lan_grade = langs.index(language) + 1
            total += (preference[languages.index(language)] * lan_grade)
        if max_total < total:
            max_total = total
            answer = job
        if max_total == total:
            if job < answer:
                answer = job
    return answer


print(
    solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5])
)