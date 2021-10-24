name: Deployment-app
on: 
  pull-request:
jobs: 
  build-and-deploy:
    matrix:
        os: [ubuntu-latest, macos-latest]
    runs-on: ${{ matrix.os }}
    steps:
    - run: echo "This has been triggered $ {{ githusb.event_name }}
    - run: echo "This job is runining on $ {{ runer.os }} server hosted on github!"
    - name: Check out repository code
      uses: actions/checkout@v2
    - name: Set up Python 3.9
      uses: actions/setup-python@v2
      with:
        python-version: 3.9
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install pylint
    - name: Lint with pylint
      run: |
        python lint_test.py
    - name: Build container
      run: |
        echo "Building a container image..."
        sleep 30
   - name: Deploy to cluster
       run: |
         echo "Deployning..."
         sleep 30
         echo "Conteiner has been deployd!"
        echo This job's status is ${{ jobs.status }}." 
     
