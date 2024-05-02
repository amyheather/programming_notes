# Latex

```{toctree}
:hidden: True

self
linux
machine_learning
open_science
```

# Unicode error
To find a unicode error (e.g. for error 202F, it's a narrow no-break space, which is hard to spot), input the following - 
```
\makeatletter
\def\UTFviii@defined#1{\ifx#1\relax!!FIXME!!\else\expandafter#1\fi}
\makeatother
```

# URL
Options include:
* `\url{}`
* `\href{}{}`