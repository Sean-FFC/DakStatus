from flask import Flask, request, jsonify, render_template, redirect, url_for
import json, os

app = Flask(__name__)
STATUS_FILE = 'status.json'

# Ensure the status file exists
if not os.path.exists(STATUS_FILE):
    with open(STATUS_FILE, 'w') as f:
        json.dump({"status": "FREE"}, f)

@app.route('/')
def index():
    with open(STATUS_FILE) as f:
        current = json.load(f).get("status", "FREE")
    return render_template('index.html', current_status=current)

@app.route('/get_status')
def get_status():
    with open(STATUS_FILE) as f:
        return jsonify(json.load(f))

@app.route('/update_status', methods=['POST'])
def update_status():
    status = request.form.get('status')
    custom = request.form.get('custom')
    final_status = custom if status == "Other" and custom else status
    with open(STATUS_FILE, 'w') as f:
        json.dump({"status": final_status}, f)
    return redirect(url_for('updated'))

@app.route('/updated')
def updated():
    return render_template('updated.html')

# 👇 This is the correct run block for Replit
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
