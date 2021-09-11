def solution(id_list, report, k):
    N = len(id_list)
    matrix = [[0]*N for _ in range(N)]
    names = {}
    for i, name in enumerate(id_list):
        names[name] = i

    counts = [0] * N
    for r in report:
        name_from, name_to = r.split(" ")
        num_from = names[name_from]
        num_to = names[name_to]
        if matrix[num_from][num_to] == 0:
            matrix[num_from][num_to] = 1
            counts[num_to] += 1

    # print(matrix)
    # print(counts)
    counts = [1 if c >= k else 0 for c in counts]
    # print(counts)

    answer = []
    for row in matrix:
        total = 0
        for i in range(N):
            if row[i] and counts[i]:
                total += 1
        answer.append(total)    
    return answer


id_list = ["muzi", "frodo", "apeach", "neo"]
report = ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
k = 2

results = solution(id_list, report, k)
print(results)
