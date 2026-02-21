# Installation & Setup Guide

## System Requirements

- **Operating System**: Windows, macOS, or Linux
- **Python Version**: 3.7 or higher (Python 3.12 recommended)
- **Disk Space**: ~50MB (including virtual environment)
- **RAM**: 512MB minimum
- **Browser**: Any modern browser (Chrome, Firefox, Safari, Edge)

## Installation Steps

### Step 1: Download the Project

Clone or download the project folder:
```
Rent vs Buy/
```

### Step 2: Navigate to Project Directory

Open PowerShell (Windows) or Terminal (Mac/Linux):

**Windows**:
```powershell
cd "c:\Users\YourUsername\OneDrive\VS code projects\Rent vs Buy"
```

**Mac/Linux**:
```bash
cd ~/path/to/Rent\ vs\ Buy
```

### Step 3: Create Virtual Environment (Optional but Recommended)

**Windows**:
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

**Mac/Linux**:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 4: Install Dependencies

```bash
pip install -r requirements.txt
```

**Note**: Flask and Werkzeug are only needed for the web interface. The core analysis works without them.

### Step 5: Verify Installation

Test the installation:

```bash
python rent_vs_buy.py
```

You should see a detailed analysis report printed to the console.

---

## Running the Application

### Option 1: Web Interface (Recommended)

Start the Flask application:

**Windows**:
```powershell
python app.py
```

**Mac/Linux**:
```bash
python app.py
```

Then open your browser and navigate to:
```
http://localhost:5000
```

**To stop**: Press `Ctrl+C` in the terminal

### Option 2: Command-Line Examples

Run 6 example scenarios:

```bash
python examples.py
```

Output will display detailed analysis for each scenario.

### Option 3: Run Tests

Verify everything works correctly:

```bash
python -m unittest test_rent_vs_buy.py -v
```

### Option 4: Python Interactive Shell

Use the library directly:

**Windows/Mac/Linux**:
```bash
python
>>> from rent_vs_buy import RentVsBuyAnalysis
>>> analysis = RentVsBuyAnalysis(500000, 100000)
>>> results = analysis.compare_scenarios(10, 2000)
>>> print(f"Recommendation: {results['recommendation']}")
Recommendation: RENT
>>> exit()
```

---

## Troubleshooting

### Issue: "Python command not found"

**Solution**: 
- Install Python from https://www.python.org
- Make sure to check "Add Python to PATH" during installation
- Restart your terminal after installation

### Issue: "ModuleNotFoundError: No module named 'flask'"

**Solution**:
```bash
pip install Flask==3.0.0
```

### Issue: "Port 5000 is already in use"

**Solution**: Modify `app.py` line at the bottom:
```python
if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Change to 5001
```

Then access: `http://localhost:5001`

### Issue: "Permission denied" (Mac/Linux)

**Solution**:
```bash
chmod +x app.py
python app.py
```

### Issue: Dependencies won't install

**Solution**: Try upgrading pip first:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

---

## IDE Setup (Optional)

### Visual Studio Code

1. **Install Python Extension**:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search "Python"
   - Install by Microsoft

2. **Select Python Interpreter**:
   - Press Ctrl+Shift+P
   - Type "Python: Select Interpreter"
   - Choose the `.venv` environment

3. **Create Launch Configuration** (`.vscode/launch.json`):
```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "name": "Web App",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/app.py",
            "console": "integratedTerminal"
        },
        {
            "name": "Examples",
            "type": "python",
            "request": "launch",
            "program": "${workspaceFolder}/examples.py",
            "console": "integratedTerminal"
        }
    ]
}
```

---

## Using Behind a Proxy

If you're behind a corporate proxy:

```bash
pip install --proxy [user:passwd@]proxy.server:port -r requirements.txt
```

Or configure pip permanently in `~/.pip/pip.conf`:
```ini
[global]
proxy = [user:passwd@]proxy.server:port
```

---

## Uninstalling/Cleaning Up

To remove the virtual environment:

**Windows**:
```powershell
Remove-Item -Recurse -Force .\.venv
```

**Mac/Linux**:
```bash
rm -rf .venv
```

---

## Next Steps

1. **Try the Web Application**:
   ```bash
   python app.py
   ```

2. **Enter Your Own Numbers**:
   - Input your purchase price, down payment, and rent
   - Adjust market assumptions as needed
   - Get your personalized recommendation

3. **Explore Examples**:
   ```bash
   python examples.py
   ```

4. **Read Documentation**:
   - `README.md` - Overview and features
   - `QUICKSTART.md` - Fast getting started
   - `API_DOCUMENTATION.md` - Detailed API reference

---

## Performance Tips

- **First Run**: May take a few seconds to initialize Flask
- **Subsequent Runs**: Analysis completes in <100ms
- **Web Interface**: Load in browser after server starts
- **Large Analysis Periods**: 50+ years may take slightly longer

---

## Getting Help

### Common Questions

**Q: How do I change the analysis period?**
A: In the web interface, set "Analysis Period (years)" field. For Python, pass `years=` parameter.

**Q: Can I save my results?**
A: You can screenshot the web results or modify the code to export as JSON/CSV.

**Q: What if my down payment is 0%?**
A: The application supports any valid down payment percentage, including FHA loans (3-5%).

**Q: Can I compare multiple scenarios?**
A: Run the web app multiple times with different parameters, or use Python to loop through scenarios.

---

## Support Resources

- **Python Docs**: https://www.python.org/doc
- **Flask Docs**: https://flask.palletsprojects.com
- **Project Issues**: Check the source code comments

---

## License & Usage

This project is open source. Use it freely for personal analysis and educational purposes.

---

**Installation Complete!** 🎉

You're now ready to analyze rent vs. buy scenarios. Start with:
```bash
python app.py
```

Then open `http://localhost:5000` in your browser.
