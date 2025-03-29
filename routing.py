from flask import Flask

app=Flask(__name__)

@app.route('/name')
def My_Name():
    file=open('Name.txt', 'r')
    name=file.read()
    file.close()
    return name

@app.route('/jobdescription')
def My_Job_Description():
    file=open('Job_Description.txt', 'r')
    job_description=file.read()
    file.close()
    return job_description
