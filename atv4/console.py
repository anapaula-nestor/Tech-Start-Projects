from main import *

print("Welcome!")
count = 0
for i in read_marketplaces():
    print(str(count) + ' - ' + i)
    count += 1
mp = input("Please choose one marketplace above: ")

print("Categories registered for this marketplace:")
cat = read_categories()
count = 0
for i in cat:
    print(str(count) + ' - ' + i)
    count += 1

choice = int(input("Choose one category: "))
sub = read_subcategories(cat[choice])
print("Subcategories for " + cat[choice])
count = 0
for i in sub:
    print(str(count) + ' - ' + i)
    count += 1
