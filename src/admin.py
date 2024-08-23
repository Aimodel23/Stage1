from flask import Flask, request, jsonify, send_from_directory
import os
from werkzeug.utils import secure_filename
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/admin/storage', methods=['GET'])
def get_storage_info():
    try:
        total, used, free = os.popen('df -h /').read().split('\n')[1].split()[1:4]
        return jsonify({
            'total': total,
            'used': used,
            'free': free
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/admin/update', methods=['POST'])
def update_algorithm():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file part'}), 400
        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No selected file'}), 400
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_DIRECTORY'], filename))
            return jsonify({'message': 'File successfully uploaded'}), 200
        return jsonify({'error': 'Invalid file type'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'py', 'txt'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

if __name__ == '__main__':
    app.run(debug=True)
