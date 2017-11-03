# tobii vs webgazer

Historical from when there was a (small) possibility of using webgazer instead of tobii due to the - now unfounded - fear of tobii being too hard to make work.

*TL;DR*

- Tobii:
	- pros:
		- *much* more accurate (10px vs ~ 100px or so)
		- industry standard
		- already shelled out for the hardware
	- cons:
		- will take a while to make bridge
		- by then may want to make the project about Desktop-browser app connectivity anyway / TIME issue
		- in terms of impact the bridge itelf would end up more important than any actual online reading app that ends up being created

- WebGazer:
	- pros:
		- web ready; building a Tobii web-bridge will be a *long* slog, SDK is new and no prior attempts at this out there ...
		- overall will allow work to focus on actual problem faster and for more time
	- cons:
		- we already bought the 4C
		- this is much less accurate (also has high variance), hence possibly lower ceiling for any end product

*Detailed Discussion:*

Integrating **Tobii** with the web will require a decent amount of work. Tobii used to have at least some form of internal endpoints that allowed their Desktop app to send data to web applications, but their existence has long since stopped even being hinted at. Even if this were not the case, they've moved to a new SDK, one for which those internal endpoints haven't been mentioned. Community members have obviously made noises about the usefulness of it being made web-friendly, but no-one within or without Tobii has started (completed?) the task of making that possible.

Doing so on my part would not be uninteresting, but it would represent a qualitative change in the work for at least a decent amount of time. It would necessesitate that I work on a - perphaps tangential - problem for a while yet before getting the chance to tackle the the meat of actual online reading optimization through web tracking. Furthermore, considering no one out there has actually bridged this eye tracker to the web, that would probably end up being the most notable part of the thesis itself. Not sure if that's desirable or even worth mentioning, I do so only because thinking of things from that point of view it seems that working on Desktop-Browser application integration would end up the endgame of the project. I'm not necessarily averse to that, I might add. 

On the other hand, if I use **WebGazer** I'll be presented with a different set of pros and cons. The most obvious con worth mentioning is that we've already shelled the $100+ required for the hardware, so not taking full advantage of it seems pretty pointless. One the pro side, WebGazer allows direct work on eye tracking for the web - I will, from day 1, be working on better allowing people to interact with articles on the web using eye tracking. There will still be under-the-hood work though - I'll certainly have to fork the library and put somewhat of my own spin on it, as right now the emphasis could be tuned still. Related to this is the accuracy issue - some might argue that a 100 px or so accuracy is simply not enough for tackling online reading. In layman's terms I'd put the accuracy at easily being able to judge which picture the user is looking at in Google Image search results. This is obviously much, much less accurate than Tobii, but I think it can be salvaged if we're willing to compromise on needing *exact* line by line detail of what someone's reading. There's also a longer discussion to be had on whether line-by-line information is even necessary for a use case such as our's - i.e. perhaps it is only the 3-4 lines or so worth of general focus region that matters? I recognize that even if the answer to the latter question is yes, it would still be ideal to test the finer grained focus and *then* reject it, rather than doing so simply out of technical inability. A rebuttal to this might be that by the time we gain technical comfort with Tobii on the web, either the tenor of the project may have changed completely anyway, or time would have become an issue. 

**Overall** the situation I'd prefer is obviously that I bang out a web bridge for tobii in 2 weeks and end up working on the actual online reading part by the end of the term. That would be more than ideal, yet slightly unrealistic from my current vantage point. Perhaps I just need to sit down with someone who truly understands desktop applications / how browsers work under the hood. To me right now, though, the porting task does seem genuinely big.

This should probably be an issue of some sort, but I think it's worth documenting all of the above anyway.
