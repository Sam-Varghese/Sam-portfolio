# Just update the JSON files, and run this code to update the website as per JSON data

import json

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

open("./rough.html", "w").write(file_content)