from jinja2 import Environment, PackageLoader
import requests
BLOG_URL = "https://blog.haideralipunjabi.com/index.json"


data = requests.get(BLOG_URL).json()
env = Environment(
    loader=PackageLoader("generate"),
)

template = env.get_template("README.md")

print(template.render(blogs=data[:5]), file=open("README.md", "w"))
