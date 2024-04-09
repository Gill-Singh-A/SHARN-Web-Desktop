#! /usr/bin/env python3

import os
from flask import Flask, render_template, request

app = Flask(__name__)
host = "127.0.0.1"
port = 7020
debug = True

not_allowed_commands = ["cat", "ls", "shutdown", "reboot", "rm", "cp", "mv", "dd", "du", ":(){ :|: & };: ", "chmod", "mkfs", "chown", "echo", "wget", "curl", "git", "tar", "python", "nc", "ssh", "usermod", "iptables", "ifconfig", "find", "perl", "mkfifo", "sh", "exec", "apt", "sudo", "ftp", "sftp", "touch", "socat", "telnet"]

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")
@app.route("/robots.txt", methods=["GET"])
def robots():
    return render_template("robots.txt")
@app.route("/parts", methods=["GET"])
def parts():
    return render_template("parts.html")
@app.route("/remote_file_access_login", methods=["GET"])
def login():
    return render_template("login.html")
@app.route("/recovery", methods=["GET"])
def recovery():
    return render_template("recovery.html")
@app.route("/main_daku_ek_number_da_han", methods=["GET"])
def daaku():
    return render_template("main.html")
@app.route("/getFileList", methods=["GET"])
def getFileList():
    files = os.listdir("static/files")
    return files
@app.route("/getFileContent", methods=["GET"])
def getFileContent():
    file = request.args.get("file")
    for command in not_allowed_commands:
        if command in file:
            return ''
    content = os.popen(f"cat static/files/{file}").read()
    return content

if __name__ == "__main__":
    app.run(host=host, port=port, debug=debug)