from string import Template

LISTING = Template(r"""
\item \href{$url}{\textit{$name}} -- $description $\cdot$
""")

LAYOUT = Template(r"""
$heading\\

\begin{itemize*}[leftmargin=*]
\itemsep0em

$listing

\end{itemize*}\\
""")