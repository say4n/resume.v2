from string import Template

LAYOUT = Template(r"""
\documentclass[11pt]{article} % Set default font size to 12pt

% lists
\usepackage{fullpage}
\usepackage[inline]{enumitem}

% Text color
\usepackage{xcolor}

% Hyperlinks
\usepackage{hyperref}

% Raleway font
\usepackage[light, semibold]{raleway}
\renewcommand{\familydefault}{\sfdefault}

% Fontawesome icons
\usepackage{fontawesome}

% Narrower page margins
\usepackage[a4paper, margin=0.5in]{geometry}

% Fancy undelines
\usepackage[normalem]{ulem}

% Lists with no bullets and aligned to edge
\setlist[itemize]{leftmargin=0em, label={}}

% Tables for layout (yuck!)
\usepackage{tabularx}
\usepackage{multirow}

\usepackage{textcase}

% Don't number pages
\pagenumbering{gobble} % Don't number pages
\setlength{\parindent}{0pt} % Don't indent paragraphs

\begin{document}

$content

\end{document}

""")
