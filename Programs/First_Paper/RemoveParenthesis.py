import re

data = ["example (.com)", "MSys", "github (.com)", "keka (.com)"]
regex = r"\s*\([^()]*\)"

for string in data:
    result = re.sub(regex, "", string)
    print(result)