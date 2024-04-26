''''
Design Underground System
An underground railway system is keeping track of customer travel times between different stations. 
They are using this data to calculate the average time it takes to travel from one station to another.
這家地鐵系統正在記錄不同車站之間的乘客旅行時間，他們使用這些數據來計算從一個車站到另一個車站的平均旅行時間。
'''
class UndergroundSystem:

    def __init__(self):
        self.travel_times = {}
        self.check_ins = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, check_in_time = self.check_ins.pop(id)
        travel = (start_station, stationName)
        travel_time = t - check_in_time

        if travel in self.travel_times:
            total_time, count = self.travel_times[travel]
            self.travel_times[travel] = (total_time + travel_time, count + 1)
        else:
            self.travel_times[travel] = (travel_time, 1)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        travel = (startStation, endStation)
        total_time, count = self.travel_times[travel]
        return total_time / count
    
def test_underground_system():
    undergroundSystem = UndergroundSystem()
    undergroundSystem.checkIn(10, "Leyton", 3)
    undergroundSystem.checkOut(10, "Paradise", 8)
    average1 = undergroundSystem.getAverageTime("Leyton", "Paradise")
    print("Average Time 1:", average1)

    undergroundSystem.checkIn(5, "Leyton", 10)
    undergroundSystem.checkOut(5, "Paradise", 16)
    average2 = undergroundSystem.getAverageTime("Leyton", "Paradise")
    print("Average Time 2:", average2)

    undergroundSystem.checkIn(2, "Leyton", 21)
    undergroundSystem.checkOut(2, "Paradise", 30)
    average3 = undergroundSystem.getAverageTime("Leyton", "Paradise")
    print("Average Time 3:", average3)

test_underground_system()
