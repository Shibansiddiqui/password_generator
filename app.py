from flask import Flask, render_template, request, send_file
import random
import string
import os
app = Flask(__name__)

script_dir =os.path.dirname(os.path.realpath(__file__))
pass_path = os.path.join(script_dir, 'password.txt')

@app.route('/')
def home():
    return render_template('index.html', username='', password='')


@app.route('/generate', methods=['POST'])
def generate_password():
    username = request.form['username']

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Welcome to the PyPassword Generator!")
    nr_letters = 8
    nr_symbols = 8
    nr_numbers = 8

    password_list = []

    for char in range(1, nr_letters + 1):
        password_list.append(random.choice(letters))

    for char in range(1, nr_symbols + 1):
        password_list += random.choice(symbols)

    for char in range(1, nr_numbers + 1):
        password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    return render_template('index.html', username=username, password=password)


@app.route('/download_password/<username>/<password>')
def download_password(username, password):
    folder_name = 'mysite'  # Name of the folder
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)  # Create the folder if it doesn't exist

    filename = os.path.join(folder_name, pass_path)  # Specify the file path
    with open(filename, 'w') as file:
        file.write(f'Username: {username}\nPassword: {password}\n')
    return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
