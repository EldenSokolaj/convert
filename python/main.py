import convert

table = convert.table(["start.ratio"])

try:
    vals = table.convert(5, "mile/hour", "m/second", trim = 3, work = True)
    print(vals[0], vals[1][len(vals[1]) - 1])
    print(vals[1])
except Exception as e:
    print("Error:", e)
