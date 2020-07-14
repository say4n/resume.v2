import datetime

now = datetime.datetime.now()
timestring = now.strftime("%B %d, %Y")

LAYOUT = r"""\vfill \scriptsize\textcolor{gray}{""" + \
    f"Last updated on {timestring}." + "}"
