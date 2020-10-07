push the app as a python app
cf run-task k6poc2 "./k6 run --out json=my_test_result.json Script.js && python3 main.py" --name mytask4444
kicks off a test, calls the python script after running the test. 
this would allow us to upload results to a git repo after a test was executed, and notify of the completion. need to check for polling of the test, etc.