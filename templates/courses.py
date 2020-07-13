from string import Template

MOOC_LISTING = Template(r"""
\item $name ($where)
""")

MOOC_LAYOUT = Template(r"""
\textbf{MOOCs}
\begin{itemize*}[itemjoin={{ $\cdot$}}]
\itemsep0em

$listing

\end{itemize*}
""")

UNDERGRAD_LISTING = Template(r"""
\item $name
""")

UNDERGRAD_LAYOUT = Template(r"""
\textbf{Undergraduate Coursework}
\begin{itemize*}[itemjoin={{ $\cdot$}}]
\itemsep0em

$listing

\end{itemize*}
""")

LAYOUT = Template(r"""
$heading\\

$undergrad
\vspace{2mm}
$moocs\\
""")