# URLShortener
Shortens urls by creating hash and storing them in a json file.

### Dependencies
- Python 2.7
- Python libraries: flask
### Installation
install libraries:
```console
pip install flask
```
run app.py:
```console
python app.py
```
### APIs
- POST: Create shortened api (http://127.0.0.1:5000/addUrl/)
- GET: 302 redirect to url (http://127.0.0.1:5000/go/<url>)
- GET: Check server status (http://127.0.0.1:5000/check/)
