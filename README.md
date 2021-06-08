<h2 align="center"> BMSCE Auto Feedback </h2>
<p align="center">
  <strong>
  For when you need to fill out feedback in the last minute. 🏃💨
  </strong>
</p>

## Setup

- Clone the repository
- Run `pip install selenium`
- Set the RATING `feedback.py` or leave it as is. (default is 'Excellent')
- Run `python feedback.py`

NOTE: In case you get an issue due the webdriver not being present in PATH:

1) Try following [some tutorial to add it to your path](https://zwbetz.com/download-chromedriver-binary-and-add-to-your-path-for-automated-functional-testing/) 

    (OR)

2) Add the path to the webdriver. eg.`driver = webdriver.Chrome('~/path/to/your/webdriver')`

### Output

```
❯ python feedback.py
Starting bmsce-auto-feedback
Attempting sign in.
-- Enter USN: 1BM18CS096
-- Enter Password: 
Signed in.
In feedback page.
Found 6 courses that need feedback.
Submitting feedback...
-- Feedback for MACHINE LEARNING submitted.
-- Feedback for CRYPTOGRAPHY AND NETWORK SECURITY submitted.
-- Feedback for OBJECT ORIENTED MODELLING AND DESIGN submitted.
-- Feedback for MANAGEMENT AND ENTREPRENEURSHIP submitted.
-- Feedback for BIG DATA ANALYTICS submitted.
-- Feedback for HEALTH AND NUTRITION submitted.
And we're done.
```
