{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "c917c43e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n"
     ]
    }
   ],
   "source": [
    "import threading\n",
    "from flask import Flask, request, render_template_string\n",
    "\n",
    "# Create Flask app\n",
    "app = Flask(__name__)\n",
    "\n",
    "# HTML form\n",
    "login_form = \"\"\"\n",
    "<!DOCTYPE html>\n",
    "<html>\n",
    "<head><title>Login Form</title></head>\n",
    "<body>\n",
    "    <h2>Login</h2>\n",
    "    <form method=\"POST\" action=\"/login\">\n",
    "        <label>Username:</label>\n",
    "        <input type=\"text\" name=\"username\" required><br><br>\n",
    "        <label>Password:</label>\n",
    "        <input type=\"password\" name=\"password\" required><br><br>\n",
    "        <input type=\"submit\" value=\"Login\">\n",
    "    </form>\n",
    "</body>\n",
    "</html>\n",
    "\"\"\"\n",
    "\n",
    "@app.route('/')\n",
    "def home():\n",
    "    return render_template_string(login_form)\n",
    "\n",
    "@app.route('/login', methods=['POST'])\n",
    "def login():\n",
    "    username = request.form['username']\n",
    "    return f\"<h3>Login successful! Welcome, {username}.</h3>\"\n",
    "\n",
    "# Function to run Flask in background\n",
    "def run_app():\n",
    "    app.run(port=5000)\n",
    "\n",
    "# Start Flask in a thread so Jupyter doesn't block\n",
    "thread = threading.Thread(target=run_app)\n",
    "thread.start()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
