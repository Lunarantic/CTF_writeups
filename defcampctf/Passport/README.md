# Passport
### (Junior - 1pts)
  
> Provide a valid passport file inorder to pass.
> Target: [passport](http://passport.dctfq18.def.camp/)
------
When you visit the site you see a hyperlink for a demo file

And, an upload form for a file

When you pass demo itself it says:
```
This is demo Passport! You have to find its evil twin.
```
When you send any arbitary file:
```
Your Passport is invalid. Our MD5SUM detected a false document.
```
Now, it is clear that they check first whether the MD5SUM is equal to demo file
```
cee9a457e790cf20d4bdaa6d69f01e41
```
On searching the internet came across a [link](https://crypto.stackexchange.com/a/15889)

On verification it is evident that following strings have same md5 hashes
```
0e306561559aa787d00bc6f70bbdfe3404cf03659e704f8534c00ffb659c4c8740cc942feb2da115a3f4155cbb8607497386656d7d1f34a42059d78f5a8dd1ef
0e306561559aa787d00bc6f70bbdfe3404cf03659e744f8534c00ffb659c4c8740cc942feb2da115a3f415dcbb8607497386656d7d1f34a42059d78f5a8dd1ef
```
Thus, one of them has to be demo; which it even is

After uploading the other one as a file we receive the flag
------
DCTF{04c8d0052e3ffd8d21934e392c272a0494f23433901941c93fab82b50be27c1a}
