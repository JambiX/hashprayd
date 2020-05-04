# hashprayd

Performs hash spray on a domain using crackmapexec to make lateral movement easier :)

### Requiremetns:
```
python 3
crackmapexec
```
### Usage:
```
--module, -m, Module to run in crackmapexec, default is SMB
--target, -t, Target machine or subnet with form: xx.xx.xx.xx/xx
--domain, -d, Domain, default is local
--users, -u', Users file
--hashes', '-H', Hashes file
```
#### Files structure:</br>
<b>users.txt:</b> ------- <b>hashes.txt:</b></br>
user1 -------- hash-of-user1</br>
user2 -------- hash-of-user2</br>
user3 -------- hash-of-user3</br>
.....

Enjoy :)
