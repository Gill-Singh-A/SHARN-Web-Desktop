# SHARN Student Cloud
A Simple CTF Challenge that expects user to see Client Side Login Algorithm, Path Traversal and Command Injection.
## Requirements
Language Used = Python3<br />
Modules/Packages used:
* os
* flask
<!-- -->
Install the dependencies:
```bash
pip install -r requirements.txt
```
## Setup
* Add Part 1 of the Flag in **/etc/passwd** (for Path Traversal)
```bash
echo part_1_of_the_flag >> /etc/passwd
```
* Add Part 2 of the Flag in Environment Variables (for Command Injection)
```bash
export flag_part_2="part_2_of_the_flag"
```
## Solution
* After seeing Robot on Index page, we head to */robots.txt*
* There are 2 Routes listed there
    * /remote_file_access_login: Login Route
    * /parts: Gives us hints where the parts of the Flags are stored
* After going to */remote_file_access_login*, we find the login logic in the **JavaScript** Code. We get the following Credentials for login:
    * User: kaptaan
    * Password: main_daku_ek_number_da_han
* After Login, we see list of Files
* After selecting 1 file, we get to know that it sends a get request to */getFileContent* with parameter *file*
* Here file is vulnerable to ***Path Traversal*** and ***Command Injection***.
* We do ***Path Traversal*** to **/etc/passwd** to get the First Part of the Flag.
* We do ***Command Injection*** to get the **Environment Variables**, which gives us the second part of the Flag.