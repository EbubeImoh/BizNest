import sys
from flask import Flask, request, jsonify

# Adjust import path to access agents module
# This assumes the app is run from the 'biznest' directory (e.g., python backend/app.py)
# Or, if run from 'biznest/backend/', sys.path.append('..') would be more appropriate.
# For now, let's try making it robust by adding the project root to sys.path
import os
# Assuming this script is in biznest/backend/app.py
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
# Check if 'biznest' is the last part of the path, if so, add the parent of 'biznest'
if os.path.basename(project_root) == 'biznest':
    sys.path.insert(0, os.path.dirname(project_root)) 
else: # Fallback: assume current execution is from a directory that has 'biznest' as a subdirectory
    sys.path.insert(0, project_root)


from biznest.agents.base_agent import BaseAgent

app = Flask(__name__)

# Initialize agents
agents = {
    "alex": BaseAgent(name="Alex", role="Accountant", avatar_url="placeholder_alex.png"),
    "bob": BaseAgent(name="Bob", role="HR Specialist", avatar_url="placeholder_bob.png")
}

@app.route('/api/agent/<string:agent_name>/command', methods=['POST'])
def handle_agent_command(agent_name: str):
    if agent_name not in agents:
        return jsonify({"error": f"Agent '{agent_name}' not found."}), 404

    data = request.get_json()
    if not data or 'command' not in data:
        return jsonify({"error": "Missing 'command' in request body."}), 400

    command = data['command']
    agent = agents[agent_name]
    
    try:
        agent_response = agent.process_command(command)
        return jsonify({"reply": agent_response}), 200
    except Exception as e:
        return jsonify({"error": f"Error processing command: {str(e)}"}), 500

if __name__ == '__main__':
    # Note: For actual deployment, use a WSGI server like Gunicorn or Waitress
    # Running with debug=True is for development purposes only
    app.run(debug=True, port=5000)
