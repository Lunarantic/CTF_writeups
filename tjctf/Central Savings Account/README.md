# Central Savings Account

> I seem to have forgotten the password for my savings account. What am I gonna do?

> The flag is not in standard flag format.

------
Challenge here is a web based.

Upon opening the link we can clearly see a textbox asking for password and submit button.

It's clear that this is going to check our input in some pattern and validate it.

Upon looking the page-source we see there is an script a [main.js](main.js) which would definately have some part.

In that script upon skimming through it we see a function creating MD5 hash from input int text box and check it's against *698967f805dea9ea073d188d73ab7390*

For MD5 you can easily find many crackers online; using any of them we come to know it is MD5 hash for *avalon*

And, as the challenge itself said that flag is not in standard form then this must be part of format *tjctf{_text_}*

------
Flag: tjctf{avalon}
