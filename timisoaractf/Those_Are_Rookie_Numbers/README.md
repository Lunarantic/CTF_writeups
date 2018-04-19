You've overheard a discussion between two classmates arguing whether the size really matters.
What does this have to do with RSA?

Within this challenge there is single file given with RSA parameters n, e, c.
We know, by RSA algorithm.
m = c^d mod(n)
c = m^e mod(n)
We need to find m here.

So, we need to find d.
For d we need phi(n).
phi(n) = (p-1)(q-1)
where,

p and q are prime numbers.
And, n = pq

So, we go check factorizedb if we can factors.
http://www.factordb.com/index.php?query=58900433780152059829684181006276669633073820320761216330291745734792546625247
we get;
p = 176773485669509339371361332756951225661
q = 333197218785800427026869958933009188427

So, now we get phi(n) = 58900433780152059829684181006276669632563849616305906563893514443102586211160

Now, we need to find d, which multiplicative inverse of e mod(phi(n)).
Thus, we go on using a python code saved as d_find.py
we get, d = 13699426463079754153895905688064380048051799131808763503874587494945034432713

Now, for final c decode we use our c_decode.py

And, voila the flag is:
timctf{th0sE_rOoKIe_numB3rz}
