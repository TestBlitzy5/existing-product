from flask import Flask

# Create Flask application instance
app = Flask(__name__)

# Define constants for server configuration
hostname = '127.0.0.1'
port = 3000

# Define route handler for all paths
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def hello_world(path):
    # Return 'Hello, World!' for any request path
    return 'Hello, World!\n', 200, {'Content-Type': 'text/plain'}

# Start the server when this file is run directly
if __name__ == '__main__':
    # Print startup message equivalent to the Node.js version
    print(f'Server running at http://{hostname}:{port}/')
    # Run the Flask application
    app.run(host=hostname, port=port)