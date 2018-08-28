result = []
add = ''

with open('test.txt', encoding='utf-8') as f:
    line = f.read()
    prim = str(line[0])
    # for x in range(int(len(line)/10)):
    for x in range(30):
        x += 1
        i = 0
        try:
            prim += (line[i + x])
            for i in range(len(line)):
                if (i + x) <= len(line):
                    try:
                        result.append(str(line[i:i+x]))
                    except IndexError:
                        break
                else:
                    break
        except IndexError:
            print('Alarm!')
            break
    # print(result)
with open('analyzer_results.txt', 'w') as wr:
    wr.write(str(result))
statistics = {}
for i in result:
    if statistics.get(i) is not None:
        statistics[i] += 1
    else:
        statistics[i] = 1
with open('analyzer_results.txt', 'a') as wr:
    wr.write('\n')
    wr.write(str(statistics))