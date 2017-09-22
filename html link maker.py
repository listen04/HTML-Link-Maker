while True:
    file = open("websites.txt", "a")
    website = input("url: ")
    name = input("name: ")
    file.write('<a href="' + website + '">' + name + "</a> &ensp; \n")
    file.close()
