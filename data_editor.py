result = []
with open('sql_q.txt', encoding='UTF-8') as f:
    for x, line in enumerate(list(f), 1):
        if not line.startswith('('):
            result.append(line)
        else:
            res_line = f'({x-2}, {line[1:]}'
            result.append(res_line)
with open('res_sql.txt', encoding='UTF-8', mode='w') as f:
    for line in result:
        f.write(line)