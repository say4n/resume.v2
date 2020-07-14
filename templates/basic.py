from string import Template

LAYOUT = Template(r"""
\begin{table}
\setlength\tabcolsep{0pt}
\small
\begin{tabu} to \linewidth {X X[r]}
	\multirow{4}{*}{\fontsize{36}{44}\selectfont{{\bf $firstname} $lastname}} & \href{$website}{$website} \\ & \href{mailto:$email}{$email} \\ & \href{skype:$skype}{$skype}\\ & \href{tel:$phone}{$phone}
\end{tabu}

\begin{center}
(Interests: $interests)
\end{center}
\end{table}
""")