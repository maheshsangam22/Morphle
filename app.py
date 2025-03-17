from flask import Flask
import os
import time
import psutil
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get system information
    full_name = "Your Full Name"  # Replace with your full name
    username = os.getlogin()
    server_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    
    # Get the top command output (simulating this)
    top_output = '\n'.join([f"PID: {p.info['pid']}, Name: {p.info['name']}" for p in psutil.process_iter(['pid', 'name'])])

    # Create the response content
    response_content = f"""
    <html>
        <body>
            <h1>System Information</h1>
            <p><strong>Name:</strong> {full_name}</p>
            <p><strong>Username:</strong> {username}</p>
            <p><strong>Server Time (IST):</strong> {server_time}</p>
            <h2>Top Output:</h2>
            <pre>{top_output}</pre>
        </body>
    </html>
    """
    
    return response_content

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
