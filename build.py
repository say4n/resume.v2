#! /usr/bin/env python3

import os
from yaml import load, Loader
from templates import heading, education


DATA_DIR = "data"
LAYOUR_DIR = "layouts"

with open(os.path.join(DATA_DIR, "achievements.yml"), "rt") as f:
    achievements_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "basic.yml"), "rt") as f:
    basic_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "courses.yml"), "rt") as f:
    courses_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "education.yml"), "rt") as f:
    education_data = load(f, Loader=Loader)
    education_string = heading.HEADING.substitute(heading="Education") + "\n"

    for e in education_data:
        education_string += education.LISTING.substitute(school=e["name"],
                                                        location=e["location"],
                                                        duration=e["duration"],
                                                        description=r"\\ ".join(e["description"]))

with open(os.path.join(DATA_DIR, "experience.yml"), "rt") as f:
    experience_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "positions.yml"), "rt") as f:
    positions_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "projects.yml"), "rt") as f:
    projects_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "publications.yml"), "rt") as f:
    publications_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "references.yml"), "rt") as f:
    references_data = load(f, Loader=Loader)

with open(os.path.join(DATA_DIR, "skills.yml"), "rt") as f:
    skills_data = load(f, Loader=Loader)
