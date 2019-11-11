import collections


###########################
# 1.
###########################
def sum(num):
    result = 0
    for n in range(1, num + 1):
        result += n
    return result


###########################
# 2.
###########################
print(97 ** 0.5)

###########################
# 3.
###########################

###########################
# 4.
###########################
print("Rats live on no evil star"[::-1])

###########################
# 5.
###########################
# "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
lists = str.split()
ans = ""
ans = lists.sort(key=len)
result = lists.join()
print(ans)

###########################
# 6.
###########################
print("\n" + "Q6." + "\n")


def count_char(s):
    listring = list(s)
    return collections.Counter(listring)


def count_char_new(s):
    l = list(s)
    freq = {}
    for ch in l:
        freq.setdefault(ch, 0)
        freq[ch] += 1
    return freq


print(count_char("aaabb"))

###########################
# 7,
###########################
print("\n" + "Q7." + "\n")
with open("./data/population-abstract2010-2015.csv")as pop:
    for line in pop:
        print(line)
#    while True:
#        line = pop.readline()
#        if not line:
#            break
#        print(line)
# print(population)

###########################
# 8.
###########################
print("\n" + "Q8." + "\n")
population = {}
with open("./data/population-abstract2010-2015.csv") as popu:
    header = popu.readline()
    while True:
        l = popu.readline()
        if not l:
            break
        column = l.split(",")
        population[column[1]] = int(column[2]) - int(column[3])
print(population)

###########################
# 9.
###########################
print("\n" + "Q9." + "\n")
population_sorted = sorted(population.items(), key=lambda x: abs(x[1]), reverse=True)

for count, t in enumerate(population_sorted):
    if count == 10:
        break
    print(str(count + 1) + "位:" + t[0] + "（" + str(abs(t[1])) + "人）")

###########################
# 10.
###########################
print("\n" + "Q10." + "\n")
with open("./data/population-abstract2010-2015.tsv", "w") as out:
    for key, value in population.items():
        out.write(key + "\t" + str(value) + "\n")
    print("DONE!!")
