from string import Template

LISTING = Template(r"""
\textbf{$designation at $organisation} & \multirow{2}{*}{$date}\\
$description
""")

LAYOUT = Template(r"""
$heading\\

\tabulinesep=1mm
\begin{tabu} to \textwidth {@{} X[9] X[1, r]}

$listing\\

\end{tabu}
""")
