import dynamic
import potential

# dynRes = dynamic.getWay("data/dataset1_Python+P7.csv", 500, csv=True)
potRes1 = potential.getWay("data/dataset1_Python+P7.csv", 500, csv=True)
print('Potential1', potRes1)
potRes2 = potential.getWay("data/dataset2_Python+P7.csv", 500, csv=True)
print('Potential2', potRes2)
# print('Dynamic', dynRes)
