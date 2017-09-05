# calculate grade
score = 75
grade = None
if score >= 80:
    grade = 'A'
elif score >= 70:
    grade = 'B'
elif score >= 60:
    grade = 'C'
elif score >= 50:
    grade = 'D'
else:
    grade = 'F'
print "Score %d => Grade %s" % ( score, grade )

# find max
a = 10
b = 15
maxx = a if (a > b) else b
print "max is %s" % maxx
