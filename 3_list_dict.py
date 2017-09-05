# introduce list, tuple
languages = ["Python", "C", "C++", "Java", "Perl"]
t = ("tuples", "are", "immutable")
print languages[0] + " is not " + languages[-1]
print t[2], t[1], t[0]

# introduce dict
"""
info = {
    'google'    : 'android',
    'apple'     : 'iso', # wrong
    'microsoft' : 'windows',
}
print info['google']
print info['apple']
print info['microsoft']
"""

# list x dict
"""
print info.items()
print info.keys()
print info.values()
corp = [ 'google', 'apple', 'microsoft' ]
os   = [ 'android', 'ios', 'windows' ]
print zip(corp, os)
print dict(zip(corp, os))
"""
