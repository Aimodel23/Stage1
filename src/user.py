from flask import Flask, request, jsonify
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)

@app.route('/user/reserve', methods=['POST'])
def reserve_storage():
    try:
        data = request.json
        amount = data.get('amount')
        if not amount:
            return jsonify({'error': 'No amount specified'}), 400

        # Simulating storage reservation process
        # You need to implement actual storage reservation logic here
        return jsonify({'message': f'Reserved {amount} GB of storage'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/user/search', methods=['GET'])
def search_storage():
    try:
        query = request.args.get('query')
        if not query:
            return jsonify({'error': 'No query specified'}), 400

        # Simulating storage search process
        # You need to implement actual storage search logic here
        return jsonify({'results': f'Found storage matching {query}'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
