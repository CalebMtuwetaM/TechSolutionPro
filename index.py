from app import app

# This file serves as the entry point for Vercel
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)