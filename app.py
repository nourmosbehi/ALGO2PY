from flask import Flask, render_template, request, jsonify, send_from_directory
from converter import convert_algorithm_to_python, convert_python_to_algorithm
import os

app = Flask(__name__, static_folder='static')
app.secret_key = os.urandom(24)

# Serve static files
@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Serve photos
@app.route('/photos/<filename>')
def serve_photos(filename):
    return send_from_directory('photos', filename)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/converter', methods=['GET', 'POST'])
def converter():
    if request.method == 'POST':
        input_text = request.form.get('input_text')
        conversion_type = request.form.get('conversion_type')
        
        if not input_text:
            return jsonify({'error': 'No input provided'}), 400
            
        try:
            if conversion_type == 'algo_to_python':
                output = convert_algorithm_to_python(input_text)
            else:
                output = convert_python_to_algorithm(input_text)
                
            return jsonify({'output': output})
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    return render_template('converter.html')

if __name__ == '__main__':
    app.run(debug=True)