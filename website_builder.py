# Just update the JSON files, and run this code to update the website as per JSON data

import json
from datetime import datetime
from htmlmin import minify
from csscompressor import compress
import jsmin

achievements_data = open("./achievements.json").read()
achievements_data = json.loads(achievements_data)

file_content = open("./index.html").read()

achievements_string = ""

for i in range(len(achievements_data["achievementsTitle"])):
    achievements_string += """
    <div id="achievement">
                <div class="title">{}</div>
                <div class="image">
                    <img loading="lazy"
                        src="{}"
                        alt=""
                    />
                </div>
                <div class="desc">
                    {}
                </div>
            </div>
    """.format(achievements_data["achievementsTitle"][i], achievements_data["achievementsImage"][i], achievements_data["achievementsDescription"][i])

certifications_data = open("./certifications.json").read()
certifications_data = json.loads(certifications_data)
certifications_string = ""

for i in range(len(certifications_data["titles"])):
    certifications_string += """
    <div id="achievement">
                <div class="title">{}</div>
                <div class="image">
                    <a href="{}" target="_blank">
                        <img loading="lazy" src="{}" alt=""
                    /></a>
                </div>
            </div>
    """.format(certifications_data["titles"][i], certifications_data["deployedCertificatesPath"][i], certifications_data["imagePaths"][i])

def replacer(original_string, start_flag, append_content):

    string_lst = original_string.split(start_flag)
    return string_lst[0] + start_flag + append_content + start_flag +string_lst[2]

projects_data = open("./projects.json").read()
projects_data = json.loads(projects_data)

projects_string = ""

for i in range(len(projects_data["titles"])):
    projects_string += """
    <div id="achievement">
                <div class="title">{}</div>
                <div class="image">
                    <img
                        src="{}"
                        alt=""
                    />
                </div>
                <div class="desc">
                    {}
                </div>
                <a href = "{}" target="_blank">
                <div class="button">View</div></a>
            </div>
    """.format(projects_data["titles"][i], projects_data["imagePaths"][i], projects_data["desc"][i], projects_data["links"][i])

# Updating achievements

file_content=replacer(file_content, "<!-- Achievements flag -->", achievements_string)

# Updating certifications

file_content = replacer(file_content, "<!-- Certifications flag -->", certifications_string)

# Updating projects

file_content = replacer(file_content, "<!-- Projects flag -->", projects_string)

# Updating date

def get_current_time():
    now = datetime.now()
    suffix = "th" if 11 <= now.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(now.day % 10, "th")
    formatted_time = now.strftime("%d{} %B, %Y %I %p").format(suffix)
    return formatted_time + ", IST"

file_content = replacer(file_content, "<!-- Current time stamp -->", get_current_time())

# Minifying HTML

file_content = minify(file_content)

# Minifying CSS

final_css_content = compress(open("./style.css").read())

# Minifying Js

final_js_content = "<script>"+jsmin.jsmin(open("./index.js").read()) + "</script>"

file_content = replacer(file_content, "<!-- JS Code -->",final_js_content)

open("./index.html", "w").write(file_content)
print("HTML code minified")
open("./style.css", "w").write(final_css_content)
print("CSS code minified")

print("Website updated sir.")