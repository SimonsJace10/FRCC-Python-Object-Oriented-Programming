import urllib.request, urllib.parse, urllib.error

link = input("input a link to scrape data from\n")

page = urllib.request.urlopen(link)

char_count = 0

for line in page:
    for char in line:
        char_count += 1
    if char_count >= 3000:
        break
    print(line.decode().strip())

print("Char count: " + str(char_count))
