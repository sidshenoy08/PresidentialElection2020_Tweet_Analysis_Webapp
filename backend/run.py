from app import create_app

# Use create_app() to get the Flask app
app = create_app()

if __name__ == "__main__":
    app.run(debug=True)