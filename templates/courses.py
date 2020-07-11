from string import Template

MOOC_LISTING = Template(r"""
\item $name ($where) $\cdot$
""")

MOOC_LAYOUT = Template(r"""
\textbf{MOOCs}
\begin{itemize*}
\itemsep0em

$listing

\end{itemize*}
""")

UNDERGRAD_LISTING = Template(r"""
\item $name $\cdot$
""")

UNDERGRAD_LAYOUT = Template(r"""
\textbf{Undergraduate Coursework}
\begin{itemize*}
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