#! /usr/bin/env python3

import os

from yaml import Loader, load

from templates import (basic, courses, document, education, heading,
                       publications)

DATA_DIR = "data"
LAYOUR_DIR = "layouts"
BUILD_DIR = "build"


with open(os.path.join(DATA_DIR, "basic.yml"), "rt") as f:
    basic_data = load(f, Loader=Loader)

    basic_string = basic.LAYOUT.safe_substitute(firstname=basic_data["name"]["first"],
                                            lastname=basic_data["name"]["last"],
                                            website=basic_data["website"],
                                            email=basic_data["email"],
                                            skype=basic_data["skype"],
                                            phone=basic_data["phone"],
                                            interests=basic_data["interests"])

with open(os.path.join(DATA_DIR, "courses.yml"), "rt") as f:
    courses_data = load(f, Loader=Loader)
    section = heading.HEADING.safe_substitute(heading="Relevant Coursework")
    moocs = courses_data["MOOCs"]
    undergrad = courses_data["Undergraduate Coursework"]

    undergrad_listing = ""
    for u in undergrad:
        if u["relevant"]:
            undergrad_listing += courses.UNDERGRAD_LISTING.safe_substitute(name=u["name"])

    undergrad_string = courses.UNDERGRAD_LAYOUT.safe_substitute(listing=undergrad_listing)

    mooc_listing = ""
    for m in moocs:
        mooc_listing += courses.MOOC_LISTING.safe_substitute(name=m["name"],
                                                        where=m["where"])

    mooc_string = courses.MOOC_LAYOUT.safe_substitute(listing=mooc_listing)

    courses_string = courses.LAYOUT.safe_substitute(heading=section,
                                                    undergrad=undergrad_string,
                                                    moocs=mooc_string)


with open(os.path.join(DATA_DIR, "education.yml"), "rt") as f:
    education_data = load(f, Loader=Loader)
    section = heading.HEADING.safe_substitute(heading="Education")
    listing = ""

    for e in education_data:
        listing += education.LISTING.safe_substitute(school=e["name"],
                                                location=e["location"],
                                                duration=e["duration"],
                                                description=r"\\ ".join(e["description"]))

    education_string = education.LAYOUT.safe_substitute(heading=section,
                                                    listing=listing)

with open(os.path.join(DATA_DIR, "experience.yml"), "rt") as f:
    experience_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "positions.yml"), "rt") as f:
    positions_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "projects.yml"), "rt") as f:
    projects_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "achievements.yml"), "rt") as f:
    achievements_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "publications.yml"), "rt") as f:
    publications_data = load(f, Loader=Loader)
    section = heading.HEADING.safe_substitute(heading="Publications")
    listing = ""

    for p in publications_data:
        if p["published"] == True:
            listing += publications.LISTING.safe_substitute(where=p["where"],
                                                        when=p["when"],
                                                        url=p["url"],
                                                        title=p["title"],
                                                        authors=p["authors"])

    publications_string = publications.LAYOUT.safe_substitute(heading=section,
                                                            listing=listing)

with open(os.path.join(DATA_DIR, "references.yml"), "rt") as f:
    references_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "skills.yml"), "rt") as f:
    skills_data = load(f, Loader=Loader)


def generate_document():
    content = f"""
    {basic_string}

    {education_string}

    {courses_string}

    {publications_string}
    """
    return document.LAYOUT.safe_substitute(content=content)


if __name__ == "__main__":
    doc = generate_document()

    os.system("rm -rf build && mkdir -p build")

    with open(os.path.join(BUILD_DIR, "resume.tex"), "w+t") as fp:
        fp.write(doc)

    os.system(f"pdflatex -output-directory build {os.path.join(BUILD_DIR, 'resume.tex')}")
