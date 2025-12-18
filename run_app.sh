#!/bin/bash

# Activate virtual environment and run the Flask application
echo "🚀 Starting Student Performance Predictor..."
echo "📦 Activating virtual environment..."

source venv/bin/activate

echo "✅ Virtual environment activated!"
echo "🌐 Starting Flask server on http://localhost:8000"
echo "Press CTRL+C to stop the server"
echo ""

python app.py
