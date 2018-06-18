import re

text="HI ,hello I m Pycharm project,From python language"
found=re.search("I .* project",text)
print(found)