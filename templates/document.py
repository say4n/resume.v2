from string import Template

LAYOUT = Template(r"""
% !TEX TS-program = arara
% arara: pdflatex: {shell: true}

\documentclass[12pt]{article} % Set default font size to 11pt

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
\usepackage[margin=0.75in]{geometry}

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