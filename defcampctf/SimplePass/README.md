# SimplePassword
### (Junior - 1pts)
> Can you guess what is wrong with [the password](SimplePass)

------
It this binary we need to find the write password to get the flag

It is 64-bit linux ELF
```Shell
$ file SimplePass
SimplePass: ELF 64-bit LSB shared object, x86-64, version 1 (SYSV), dynamically linked, interpreter /lib64/ld-linux-x86-64.so.2, for GNU/Linux 3.2.0, BuildID[sha1]=caf8649b898078889978fa4a3be29437124c214c, not stripped
```
On checking with strings it is clear our flag is *DCTF{sha256(your_number)}*

So, and it even asks for password, on running it is that, but no output if wrong password

If right number given it will print *DCTF{sha256(your_number)}*

Then we need to find that number, the number is not a constant as it would be easily identifiable during disassembly

There multiple calls to *<_Z9Fibonaccii>* and it's return values are added, multiplied, bits shifted to form a number

Then that number is compared with one we provide

So either you can do all those steps or be smart and read from stack what number is generated

The number will be passed to a function to compare & while looking for that

I found a function *<_ZNSt7__cxx119to_stringEi>* right before call to compare

This function will convert int to string which right after all calculations from *<_Z9Fibonaccii>*

So I target to get that int from this function's input

That's what I did using gdb
```GDB
$ gdb ./SimplePass
(gdb) breakpoint main
Breakpoint 1 in main()
(gdb) disassemble
// find address of instruction which calls function for compare *<_ZNSt7__cxx119to_stringEi>*
(gdb) breakpoint *(address found)
Breakpoint 2 in <main+216>()
(gdb) run
Breakpoint 1 hit
(gdb) continue
Password?
// give any random input
Breakpoint 2 hit
```
These instructions provide input of one string pointer and one integer given in esi and rdi registers for *int_to_string*
```GDB
<main+204>:	lea    -0x40(%rbp),%rax
<main+208>:	mov    -0x64(%rbp),%edx
<main+211>:	mov    %edx,%esi
<main+213>:	mov    %rax,%rdi
<main+216>:	callq  <_ZNSt7__cxx119to_stringEi>
```
esi contains integer number that we need to give for success

This is because it uses mov instruction and not lea which gives address *pointer* for string

So we print the number and test in binary
```GDB
(gdb) print $edx
$1 = -366284240
```
Finally, number is confirmed then its sha256 is calculate and flag is obtained

------
Flag: DCTF{554a58cfad51e0d7df7e8287fa96223780a249b104de60425908abf0b83c69aa}
