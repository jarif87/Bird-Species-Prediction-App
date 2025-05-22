# Bird Species Prediction App

A Flask-based web app to predict bird species from uploaded images using a Keras model. Supports six species: American Goldfinch, Barn Owl, Carmine Bee-Eater, Downy Woodpecker, Emperor Penguin, Flamingo. Features a responsive, custom CSS design.

**Created by Sadik Al Jarif**

## Project Structure

```
project_root/
│
├── app.py                  # Flask app
├── model/
│   └── my_model.keras      # Keras model
├── templates/
│   └── index.html          # HTML template
├── static/
│   ├── css/
│   │   └── style.css       # Custom CSS
│   ├── uploads/            # Uploaded images
│   └── images/
│       └── white_bg.jpg    # Default image
├── README.md

```


## Prerequisites
- Python 3.8+: Check with `python3 --version`
- Dependencies: Flask, TensorFlow, NumPy, Pillow
- Files: `my_model.keras` in `model/`, `white_bg.jpg` in `static/images`

## Setup
1. **Clone Repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd bird-species-prediction

2. **Virtual Environment:**

```
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```
3. **Install Dependencies:**
- Create requirements.txt:
```
echo -e "flask\ntensorflow\nnumpy\nPillow" > requirements.txt
```
4. **Install:**

``` pip install -r requirements.txt```

5. **Prepare Files:**

- Place my_model.keras in model/:

```
mv /path/to/my_model.keras model/
```

6. **Place white_bg.jpg in static/images**

``` mv /path/to/white_bg.jpg static/images/```

# Usage

### Run App:

```
python3 app.py
```