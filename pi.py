text = """
    How I want a drink, alcoholic of course, after the heavy chapters involving
    quantum mechanics. All of thy geometry, Herr Planck, is fairly hard.
"""

# TODO
text = text.replace(',','')
text = text.replace('.','')
text = list(map(len, text.split()))
print("".join(map(str,text)))