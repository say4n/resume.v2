from string import Template

LISTING = Template(r"""
\item \href{$url}{\it $title} -- {\it $where, $when}, $authors
""")

LAYOUT = Template(r"""
$heading

\begin{itemize}
\itemsep0em

$listing

\end{itemize}
""")
