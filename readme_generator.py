import os
import time
from re import finditer

extenstion_name = {
    'py': 'Python',
}

readme_header = \
"""
## LeetCode 

My solutions to leetcode problems
"""

def parse_file_name(name):
    if "." in name:
        return name.split(".")
    else:
        raise RuntimeError("No extension in file")

def camel_case_to_text(identifier):
    matches = finditer('.+?(?:(?<=[a-z])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])|$)', identifier)
    return " ".join([m.group(0) for m in matches])

"""
Algorithms solution table builder
"""
algorithm_files = os.listdir("algorithms/")
algo_table_header = \
"""
### Algorithms


|#   | Title | Solution |
|----|-------|----------|
"""

algorithm_solutions = []
for solution in algorithm_files:
    metadata_change_time = time.ctime(os.path.getctime(f"algorithms/{solution}"))
    camelCaseName, ext = parse_file_name(solution)
    name = camel_case_to_text(camelCaseName)

    algorithm_solutions.append({
        "time": metadata_change_time,
        "name": name,
        "ext": ext,
        "path": f"algorithms/{solution}"
    })


algo_table_rows = []
for num, item in enumerate(sorted(algorithm_solutions, key=lambda x: x['time'])):
    lang = extenstion_name[item['ext']]
    row = f"| {num} | {item['name']} | [{lang}]({item['path']}) |"
    algo_table_rows.append(row)

algo_block = "".join([algo_table_header, "\n".join(algo_table_rows)])
readme_content = "\n".join([readme_header, algo_block])

with open("readme.md", "w") as readme:
    readme.write(readme_content)
