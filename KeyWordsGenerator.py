import random

keywords = [
"Array", "Encapsulation", "Inheritance", "Abstracation", "Polymorphism",
"Single Inheritance", "Multiple Inheritance", "MultiLevel Inheritance", "Hierarchichal Inheritance",
"Auxiliary Space", "HybridInheritance",
"Big O Notation",
"Binary Search",
"Class",
"DSA",
"Hashing",
"Inheritance",
"Mountain Array",
"Object",
"Object Oriented Analysis",
"Object Oriented Design",
"Object Oriented Design Principles",
"Object Oriented Design Patterns",
"Object Oriented Programming",
"Prefix Sum",
"Space Complexity",
"Time Complexity",
]

keywords.sort()

def random_color():
    # Generate a random hex color
    return "#{:06x}".format(random.randint(0, 0xFFFFFF))

def random_font_size():
    # Return a font size between 100% and 200%
    return f"{random.randint(100, 300)}%"

with open("KeyWords.md", "w") as fp:
    fp.write("# Adding keywords here so that I can check them later at some point of time what things I learnt or gone through.\n\n")
    
    keyword_html = [
        f'<code style="font-size: {random_font_size()}; color: {random_color()};">{keyword}</code>'
        for keyword in keywords
    ]
    
    fp.write(" ".join(keyword_html))
