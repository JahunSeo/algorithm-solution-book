from collections import defaultdict

def solution(fees, records):

    cars = defaultdict(int) # 차량 번호: 누적 시간
    parking = {} # 차량번호: 입차 시간

    for r in records:
        time, car, status = r.split(" ")
        hh, mm = time.split(":")
        adj_time = int(hh) * 60 + int(mm)
        # print(time, hh, mm, adj_time)
        if status == "IN":
            parking[car] = adj_time
        else:
            if car not in parking:
                return False
            use_time = adj_time - parking[car]
            # print("keep", car, use_time)
            cars[car] += use_time
            del parking[car]

    # print(parking)
    time_limit = 23 * 60 + 59
    for car in parking:
        use_time = time_limit - parking[car]
        cars[car] += use_time

    costs = []
    for car in cars:
        total_time = cars[car]
        if (total_time-fees[0] >= 0):
            cost = fees[1] + (-(-(total_time-fees[0]) // fees[2])) * fees[3]
        else :
            cost = fees[1]
        # print("hey", car, total_time, cost)
        costs.append((int(car), cost))

    costs.sort()    
    answer = [c[1] for c in costs]
    return answer

fees = [180, 5000, 10, 600] # 기본 시간, 기본 요금, 단위 시간, 단위 요금
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

print(solution(fees, records))