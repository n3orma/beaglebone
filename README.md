# Steps

## Step 1: Update the system

```bash
sudo apt update
sudo apt upgrade
```

---

## Step 2: Install Flask

```bash
sudo apt install python3-flask
```

---

## Step 3: Create the project directory

```bash
mkdir led_web
cd led_web
mkdir templates
```

---

## Step 4: Create the Python application

```bash
nano app.py
```

Copy and paste the Python code into `app.py`, then save the file.

---

## Step 5: Create the HTML page

```bash
nano templates/index.html
```

Copy and paste the HTML code into `index.html`, then save the file.

---

## Step 6: Run the Flask application

```bash
python3 app.py
```

The server will start on port **5000**.

---

## Step 7: Find the BeagleBone Black IP address

```bash
hostname -I
```

Note the IP address displayed.

---

## Step 8: Open the web application

Open a web browser on your computer and enter:

```
http://<BeagleBone-IP>:5000
```

For example:

```
http://192.168.1.105:5000
```

or, when connected through USB networking:

```
http://192.168.7.2:5000
```

---

## Step 9: Control the built-in LED

- Click **LED ON** to turn the LED on.
- Click **LED OFF** to turn the LED off.

---

## Step 10: Stop the application

Return to the terminal and press:

```text
Ctrl + C
```
