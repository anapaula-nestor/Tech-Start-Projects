from historic import *
from log import *

print("Welcome!")
count = 0
marketplaces = read_column("Marketplace")
for mp in marketplaces:
    print(str(count) + ' - ' + mp)
    count += 1
save_log("Console: List of Marketplaces visualized")
mp = int(input("Please choose one marketplace above: "))

save_log("Console: Marketplace selected: " + marketplaces[mp])
print("Categories registered for this marketplace:")
cat = read_categories(marketplaces[mp])
count = 0
for item in cat:
    print(str(count) + ' - ' + item)
    count += 1
save_log(f"Console: Categories for {marketplaces[mp]} visualized: {cat}")

choice = int(input("Choose one category: "))
sub = read_subcategories(marketplaces[mp], cat[choice])
print("Subcategories for " + cat[choice])
count = 0
for i in sub:
    print(str(count) + ' - ' + i)
    count += 1
save_log(f"Console: Subcategories of {cat[choice]} opened for {marketplaces[mp]} visualized: {sub}")