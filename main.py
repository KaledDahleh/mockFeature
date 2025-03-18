import re

saved_posts = [
    {"title": "Perfect Apple Pie Recipe!", "content": "Ingredients and instructions for baking pies"},
    {"title": "Funny Meme Compilation", "content": "Meme video for laughs"},
    {"title": "Calculus Integration Techniques", "content": "Guide on solving integrals"}
]

categories = {
    'Cooking': r'pie|bake|recipe|cook',
    'Entertainment': r'meme|funny|video|joke',
    'Education': r'calculus|integral|math|physics'
}

categorized_posts = {key: [] for key in categories}

for post in saved_posts:
    for category, pattern in categories.items():
        if re.search(pattern, post["title"], re.I):
            categorized_posts[category].append(post)

print(categorized_posts)
