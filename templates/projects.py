from string import Template

LISTING = Template(r"""
\item \href{$url}{\textit{$name}} -- $description
""")

LAYOUT = Template(r"""
$heading\\

\begin{itemize*}[leftmargin=*, itemjoin={{ $\cdot$}}]
\itemsep0em

$listing

\end{itemize*}\\
""")