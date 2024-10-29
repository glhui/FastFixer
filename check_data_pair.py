import os
from os import listdir

total = 0
pair_error = 0
for problem in listdir(os.path.join('dataset', 'submit_data')):
    if not problem.startswith("problemID_"):
        continue
    print(f"process the {problem}...")
    wrong_submit = set(listdir(os.path.join('dataset', 'submit_data', problem, 'wrong')))
    correct_submit = set(listdir(os.path.join('dataset', 'submit_data', problem, 'correct')))

    correct_submit_replaced = {s.replace('correct', '') for s in correct_submit}
    wrong_submit_replaced = {s.replace('wrong', '') for s in wrong_submit}

    for wrong in wrong_submit_replaced:
        total += 1
        if wrong not in correct_submit_replaced:
            pair_error += 1
            print(f"{problem} {wrong} not in {correct_submit_replaced}")
print(f"total: {total}, pair_error: {pair_error}")