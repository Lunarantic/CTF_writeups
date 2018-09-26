# Not your average RSA

> You've overheard a discussion between two classmates arguing whether the size really matters.
> What does this have to do with RSA?

> [params.txt](params.txt)
------
Within this challenge there is single file given with RSA parameters n, e, c

We know, by RSA algorithm
```
m = c^d mod(n)
c = m^e mod(n)
```
We need to find m here

So, we need to find d

For d we need *phi(n)*
```
phi(n) = (p-1)(q-1)
where,
p and q are prime numbers
And, n = pq
```
So, we go check [factordb](http://www.factordb.com/index.php?query=58900433780152059829684181006276669633073820320761216330291745734792546625247) if factors are available

we get
```python
>>> p = 176773485669509339371361332756951225661
>>> q = 333197218785800427026869958933009188427
>>> phi_n = p * q
>>> print(phi_n)
58900433780152059829684181006276669632563849616305906563893514443102586211160
```
Now, we need to find d, which multiplicative inverse of e mod(phi(n)).

Thus, we go on using [d_find.py](d_find.py)
```Shell
$ python d_find.py 58900433780152059829684181006276669632563849616305906563893514443102586211160 65537
13699426463079754153895905688064380048051799131808763503874587494945034432713
```
Now, finally for flag [c_decode.py](c_decode.py)
```Shell
$ python c_decode.py 56191946659070299323432594589209132754159316947267240359739328886944131258862 13699426463079754153895905688064380048051799131808763503874587494945034432713 58900433780152059829684181006276669633073820320761216330291745734792546625247
timctf{th0sE_rOoKIe_numB3rz}
```

And, voila the flag is:
timctf{th0sE_rOoKIe_numB3rz}
