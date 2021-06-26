from string import Template

LISTING = Template(r"""

\textbf{\href{$url}{$designation}}, $location & $duration \\

""")

LAYOUT = Template(r"""

$heading\\

\tabulinesep=1.2mm
\begin{tabu} to \textwidth {@{} X[8.25] X[1.75,r]}

$listing\\

\end{tabu}
""")
