#! /usr/bin/env python3

import os
from yaml import Loader, load
from templates import document, education, heading, publications


DATA_DIR = "data"
LAYOUR_DIR = "layouts"
BUILD_DIR = "build"


with open(os.path.join(DATA_DIR, "achievements.yml"), "rt") as f:
    achievements_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "basic.yml"), "rt") as f:
    basic_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "courses.yml"), "rt") as f:
    courses_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "education.yml"), "rt") as f:
    education_data = load(f, Loader=Loader)
    section = heading.HEADING.substitute(heading="Education")
    listing = ""

    for e in education_data:
        listing += education.LISTING.substitute(school=e["name"],
                                                location=e["location"],
                                                duration=e["duration"],
                                                description=r"\\ ".join(e["description"]))

    education_string = education.LAYOUT.substitute(heading=section,
                                                    listing=listing)

with open(os.path.join(DATA_DIR, "experience.yml"), "rt") as f:
    experience_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "positions.yml"), "rt") as f:
    positions_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "projects.yml"), "rt") as f:
    projects_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "publications.yml"), "rt") as f:
    publications_data = load(f, Loader=Loader)
    section = heading.HEADING.substitute(heading="Publications")
    listing = ""

    for p in publications_data:
        if p["published"] == True:
            listing += publications.LISTING.substitute(where=p["where"],
                                                        when=p["when"],
                                                        url=p["url"],
                                                        title=p["title"],
                                                        authors=p["authors"])

    publications_string = publications.LAYOUT.substitute(heading=section,
                                                            listing=listing)

with open(os.path.join(DATA_DIR, "references.yml"), "rt") as f:
    references_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "skills.yml"), "rt") as f:
    skills_data = load(f, Loader=Loader)


def generate_document():
    content = f"""
    {education_string}

    {publications_string}
    """
    return document.LAYOUT.substitute(content=content)


if __name__ == "__main__":
    doc = generate_document()

    os.system("rm -rf build && mkdir -p build")

    with open(os.path.join(BUILD_DIR, "resume.tex"), "w+t") as fp:
        fp.write(doc)

    os.system(f"pdflatex -output-directory build {os.path.join(BUILD_DIR, 'resume.tex')}")
