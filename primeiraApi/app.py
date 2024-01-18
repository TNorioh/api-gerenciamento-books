from flask import Flask, jsonify, request

app = Flask(__name__)
books = [
    {
        'id': 1,
        'titulo': 'O Menino do Pijama Listrado',
        'autor': 'John Boyne'
    },
    {
        'id': 2,
        'titulo': 'Tormento',
        'autor': 'John Boyne'
    },
    {
        'id': 3,
        'titulo': 'Noah Foge de Casa',
        'autor': 'John Boyne'
    }

]

# CONSULTAR LIVROS
@app.route('/books', methods=['GET'])
def consult_book():
    return jsonify(books)

# CONSULTAR (ID)
@app.route('/books/<int:id>', methods=['GET'])
def obt_book_id(id):
    for book in books:
        if book.get('id') == id:  
            return jsonify(book)
# EDITAR
@app.route('/books/<int:id>', methods=['PUT'])
def edit_book_id(id):
    change_book = request.get_json()
    for indice,book in enumerate(books):
        if book.get('id') == id: 
            books[indice].update(change_book)
            return jsonify(book[indice])

# CRIAR
@app.route('/books', methods=['POST'])
def include_book():
    new_book = request.get_json()
    books.append(new_book)
    return jsonify(books)

# EXCLUIR 
@app.route('/books/<int:id>', methods=['DELETE'])
def delete_book(id):
    for indice, book in enumerate(books):
        if book.get('id') == id:  
            del books[indice]

        return jsonify(books)    

app.run(port=5000, host='localhost', debug=True)
