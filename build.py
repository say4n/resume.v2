#! /usr/bin/env python3

import argparse
import os
import subprocess

from yaml import Loader, load

from templates import (achievements, basic, courses, document, education,
                       experience, heading, positions, projects, publications,
                       references, skills, timestamp)

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
    grad = courses_data["Masters Coursework"]

    grad_listing = ""
    for u in grad:
        grad_listing += courses.GRAD_LISTING.safe_substitute(
            name=u["name"])

    grad_string = courses.GRAD_LAYOUT.safe_substitute(
        listing=grad_listing)

    undergrad_listing = ""
    for u in undergrad:
        if u["relevant"]:
            undergrad_listing += courses.UNDERGRAD_LISTING.safe_substitute(
                name=u["name"])

    undergrad_string = courses.UNDERGRAD_LAYOUT.safe_substitute(
        listing=undergrad_listing)

    courses_string = courses.LAYOUT.safe_substitute(heading=section,
                                                    grad=grad_string,
                                                    undergrad=undergrad_string)

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
    section = heading.HEADING.safe_substitute(heading="Experience")
    listing = ""

    for e in experience_data["research"]:
        listing += experience.LISTING.safe_substitute(location=e["location"],
                                                      designation=e["designation"],
                                                      duration=e["duration"],
                                                      url=e["url"])

    for w in experience_data["industry"]:
        listing += experience.LISTING.safe_substitute(location=w["location"],
                                                      designation=w["designation"],
                                                      duration=w["duration"],
                                                      url=w["url"])

    experience_string = experience.LAYOUT.safe_substitute(heading=section,
                                                          listing=listing)

with open(os.path.join(DATA_DIR, "positions.yml"), "rt") as f:
    positions_data = load(f, Loader=Loader)
    section = heading.HEADING.safe_substitute(heading="Positions Held")
    listing = ""

    for p in positions_data:
        listing += positions.LISTING.safe_substitute(designation=p["designation"],
                                                     organisation=p["organisation"],
                                                     description=p["description"],
                                                     date=p["date"])

    positions_string = positions.LAYOUT.safe_substitute(heading=section,
                                                        listing=listing)

with open(os.path.join(DATA_DIR, "projects.yml"), "rt") as f:
    projects_data = load(f, Loader=Loader)
    section = heading.HEADING.safe_substitute(heading="Select Projects")
    listing = ""

    for p in projects_data:
        listing += projects.LISTING.safe_substitute(name=p["name"],
                                                    url=p["url"],
                                                    description=p["description"])

    projects_string = projects.LAYOUT.safe_substitute(heading=section,
                                                      listing=listing)

with open(os.path.join(DATA_DIR, "achievements.yml"), "rt") as f:
    achievements_data = load(f, Loader=Loader)
    section = heading.HEADING.safe_substitute(heading="Honors and Awards")
    listing = ""

    for a in achievements_data:
        listing += achievements.LISTING.safe_substitute(title=a["title"],
                                                        date=a["date"])

    achievements_string = achievements.LAYOUT.safe_substitute(heading=section,
                                                              listing=listing)

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
    section = heading.HEADING.safe_substitute(heading="References")
    listing = ""

    for r in references_data:
        listing += references.LISTING.safe_substitute(name=r["name"],
                                                      email=r["email"],
                                                      designation=r["designation"],
                                                      organization=r["organization"])

    referees = references.LAYOUT.safe_substitute(heading=section)

with open(os.path.join(DATA_DIR, "skills.yml"), "rt") as f:
    skills_data = load(f, Loader=Loader)
    section = heading.HEADING.safe_substitute(heading="Skills")
    listing = ""

    for skill_type in skills_data:
        listing += skills.TYPE_HEADING.safe_substitute(type=skill_type.title())

        for level in skills_data[skill_type]:
            listing += skills.LISTING.safe_substitute(level=level.title(),
                                                      skills=", ".join(skills_data[skill_type][level]))

        listing += "\\\\"

    skills_string = skills.LAYOUT.safe_substitute(heading=section,
                                                  listing=listing)


def generate_document():
    content = f"""
{basic_string}
\\begin{{minipage}}{{\\textwidth}}
{education_string}
\\end{{minipage}}

\\vspace{{2mm}}

\\begin{{minipage}}{{\\textwidth}}
{experience_string}
\\end{{minipage}}

\\vspace{{2mm}}

\\begin{{minipage}}{{\\textwidth}}
{publications_string}
\\end{{minipage}}

\\vspace{{2mm}}

\\begin{{minipage}}{{\\textwidth}}
{courses_string}
\\end{{minipage}}

\\vspace{{2mm}}

\\begin{{minipage}}{{\\textwidth}}
{skills_string}
\\end{{minipage}}

\\vspace{{2mm}}

\\begin{{minipage}}{{\\textwidth}}
{achievements_string}
\\end{{minipage}}


\\vspace{{2mm}}


\\begin{{minipage}}{{\\textwidth}}
{projects_string}
\\end{{minipage}}

\\vspace{{2mm}}

\\begin{{minipage}}{{\\textwidth}}
{positions_string}
\\end{{minipage}}

\\vspace{{2mm}}

\\vfill

\\begin{{minipage}}{{\\textwidth}}
{timestamp.LAYOUT}
\\end{{minipage}}
"""
    return document.LAYOUT.safe_substitute(content=content)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--release",
        default=False,
        action='store_true',
        help="Create a GitHub release on build.")
    args = parser.parse_args()

    doc = generate_document()

    os.system("rm -rf build && mkdir -p build")

    with open(os.path.join(BUILD_DIR, "resume.tex"), "w+t") as fp:
        fp.write(doc)

    os.system(
        f"pdflatex -output-directory build {os.path.join(BUILD_DIR, 'resume.tex')}")

    if args.release:
        tag = subprocess.check_output(
            ['git', 'rev-parse', '--short', 'HEAD']).decode('ascii').strip()
        command = f"hub release create -a build/resume.pdf -m '{timestamp.timestring}' '{tag}'"

        os.system(command)
