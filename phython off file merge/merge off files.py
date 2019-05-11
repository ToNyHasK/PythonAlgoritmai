import heapq

#4-way merge sort, sorted page files
outfile="mergedOFF.off"

with open("first.off") as f1,\
     open("second.off") as f2,\
     open("third.off") as f3,\
     open("fourth.off") as f4,\
     open(outfile,"w") as of:
    of.writelines(heapq.merge(f1, f2, f3, f4))