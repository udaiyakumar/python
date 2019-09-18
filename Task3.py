courses ={'python': 1500, "Java":1000,'c':500,'c++':1200}
for key, value in sorted(courses.items(), key=lambda item: item[1]):
     print("%s: %s" % (key, value))
