from string import Template

LISTING = Template(r"""
$title. & \hfill $date \\
""")

LAYOUT = Template(r"""
$heading\\

\tabulinesep=1mm
\begin{tabu} to \textwidth {@{}X[7.5] X[2.5]}

$listing\\

\end{tabu}

""")
