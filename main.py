from flask import Flask, render_template, request, redirect, send_file
from scrapper import get_remote_jobs

"""
The App work for below URL's: 
https://weworkremotely.com/remote-jobs/search?term=python

"""

app = Flask("JobScrapper")

db = {}

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/search")
def search():
    input = request.args.get("input")
    if input:
        input = input.lower()
        present_jobs = db.get(input)
        if present_jobs:
            jobs = present_jobs
        else:
            jobs = get_remote_jobs(input)
            db[input] = jobs
    else:
        return redirect("/")

    return render_template("job_search.html", input=input, jobs=jobs, job_count=len(jobs))


@app.route("/export")
def export():
    try:
        input = request.args.get("input")

        if not input:
            raise Exception()

        input = input.lower()
        remote_jobs = db.get(input)

        if not remote_jobs:
            raise Exception()

        save_to_file(remote_jobs)

        return send_file("remote_jobs.csv")
    except:
        return redirect("/")

app.run(host="127.0.0.1")

