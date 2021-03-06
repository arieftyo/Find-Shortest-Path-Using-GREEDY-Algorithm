import heapq

dst = {}
tjn = {}

grp = {}
grp["Nagasaki"] = [["Yokohama", 80], ["Hiroshima", 97], ["Akihabara", 146]]
grp["Kyoto"] = [["Yokohama", 99], ["Osaka", 211]]
grp["Hiroshima"] = [["Nagasaki", 97], ["Osaka", 101], ["Akihabara", 138]]
grp["Fuji"] = [["Kumamoto", 87]]
grp["Kumamoto"] = [["Fuji", 87], ["Nagano", 92]]
grp["Nagano"] = [["Kumamoto", 92], ["Funabashi", 142]]
grp["Matsuyama"] = [["Osaka", 90]]
grp["Funabashi"] = [["Osaka", 85], ["Chiba", 98], ["Nagano", 142]]
grp["Chiba"] = [["Funabashi", 98], ["Nara", 86]]
grp["Osaka"] = [["Chiba", 86]]
grp["Tokyo"] = [["Yokohama" , 140], ["Saitama", 118], ["Sakai", 75]]
grp["Yokohama"] = [["Atsugi" , 151], ["Tokyo" , 140], ["Kyoto" , 99], ["Nagasaki" , 80]]
grp["Sakai"] = [["Tokyo" , 75], ["Atsugi", 71]]
grp["Atsugi"] = [["Sakai" , 71], ["Yokohama", 151]]
grp["Saitama"] = [["Tokyo", 118], ["Sendai", 118]]
grp["Sendai"] = [["Saitama", 111], ["Fukuyama", 70]]
grp["Fukuyama"] = [["Sendai", 70], ["Kashiwa", 75]]
grp["Kashiwa"] = [["Fukuyama", 75], ["Akihabara", 120]]
grp["Akihabara"] = [["Hiroshima", 138], ["Kashiwa", 120], ["Nagasaki", 97]]


heuristics = {
    "Tokyo"          : 366,
    "Osaka"          : 0,
    "Akihabara"      : 160,
    "Kashiwa"        : 242,
    "Nara"           : 161,
    "Kyoto"          : 178,
    "Matsuyama"      : 77,
    "Chiba"          : 151,
    "Kumamoto"       : 226,
    "Sendai"         : 244,
    "Fukuyama"       : 241,
    "Fuji"           : 234,
    "Atsugi"         : 380,
    "Hiroshima"      : 98,
    "Nagasaki"       : 193,
    "Yokohama"       : 253,
    "Saitama"        : 329,
    "Funabashi"      : 80,
    "Nagano"         : 199,
    "Sakai"          : 374
}

def createPrint(origin, dest):
         temp = []
         while dest != origin:
            temp.append(dest)
            dest = tjn[dest]
            print(temp)
            
def greedy(origin, dest):
    print(origin)
    z = []
    heapq.heapify(z)
    heapq.heappush(z,[heuristics[origin], origin])
    dst[origin] = 0
    while z:
        now = heapq.heappop(z)
        if now[1] == dest:
            break
        for n in grp[now[1]]:
            if n[0] not in dst or dst[n[0]] > dst[now[1]] + n[1]: 
                print(dst[now[1]]+n[1])
                heapq.heappush(z,[heuristics[n[0]],n[0]])
                dst[n[0]] = dst[now[1]] + n[1]
                tjn[n[0]] = now[1]          
    createPrint(origin,dest)
    print("\n")

greedy("Tokyo", "Osaka")
greedy("Fuji", "Osaka")

