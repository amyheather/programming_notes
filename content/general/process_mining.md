# Processing mining

From Sammi:

My fairly limited understanding is that pm4py offers slightly more advanced algorithms and more of a focus on the predictive end of things, while bupaR has really nice visuals and is a very strong, solid package for process mining but is maybe not so strong in terms of its prediction capabilities. There's also the pm4py R package which is an R interface to PM4py if you needed some of its features.
In particular I think pm4py is more geared up for conformance checking (checking your processes in your event logs match with what the process should be), though I think it's possible to do in R too.

One big limitation to bear in mind is pm4py's licence. It's only free for teaching, research and open source work (commercial or not), and any scripts using pm4py have to be published openly and licenced with the AGPL 3.0 licence (https://processintelligence.solutions/pm4py - about halfway down this page). So it might not suit if there's a desire to keep the code closed. I don't think bupaR has the same restrictions. I assume it would apply to the r pm4py too, though.

bupaR also has animations if that's something that appeals, which I don't think pm4py has an equivalent for.

Having used both, my preference is for bupaR, but I've not really dived into the more advanced end of pm4py.
I do have a notebook comparing bupaR with my animation package vidigi - it gives a quick overview of most of the available bupaR plot types. https://hsma-tools.github.io/vidigi/examples/feat_vidigi_vs_bupar/vidigi_vs_bupar.html#creating-outputs

I believe there is a process mining centre of excellence on AnalystX that might have some useful resources, but I can't access AnalystX myself these days to check  That might also might have links to the NHS England process mining team, but if not I can see if I can dig out their email too, as they might be able to advise further.