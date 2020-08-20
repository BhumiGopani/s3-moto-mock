## s3-moto-mock
Demo of how to mock AWS services using Boto&Moto 

## Please install all the requirements:
`pip3 install -r requirements.txt`

## Please check the versions and upgrade virtual env
`python3
pip3 --version
pip3 install --upgrade virtualenv`

## Create virtual env
`virtualenv -p python3 moto_demo`

## Activate virtual env
`source moto_demo/bin/activate`

## To execute the code, try:
`pytest --html=report.html`

## To view the reports:
`report.html`

# Reference
https://www.youtube.com/watch?v=jdey8FvEBM0

# To run pre-commit for all the files
`pre-commit run --all-files`