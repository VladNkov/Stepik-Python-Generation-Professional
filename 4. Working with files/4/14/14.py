import json, csv
from datetime import datetime
with open('exam_results.csv', encoding='utf-8') as in_file, open('best_scores.json', 'w', encoding='utf-8') as out_file:
    data = list(csv.DictReader(in_file, delimiter=','))
    data = sorted(data, key=lambda x: x['email'])

    results_dict = {}
    answer = []
    for d in data:
        student = f"{d['name']} {d['surname']}"
        results_dict.setdefault(student, []).append({
            'score': int(d['score']), 'date_and_time': d['date_and_time'], 'email': d['email']
        })

    for student, result in results_dict.items():
        best_score = max(result, key=lambda x: (x['score'], datetime.strptime(x['date_and_time'], '%Y-%m-%d %H:%M:%S')))
        answer.append({'name': student.split(' ')[0],
                       'surname': student.split(' ')[1],
                       'best_score': int(best_score['score']),
                       'date_and_time': best_score['date_and_time'],
                       'email': best_score['email']
                       })

    json.dump(answer, out_file, indent=4, ensure_ascii=False)