from string import Template

LISTING = Template(r"""
\item {\it $where, $when} -- \href{$url}{\it $title}, $authors
""")

LAYOUT = Template(r"""
$heading

\begin{itemize}
\itemsep0em

$listing

\end{itemize}
""")
