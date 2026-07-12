<<<<<<< HEAD
from flask import Flask, render_template
import pandas as pd
import json
import re

app = Flask(__name__)

# Load CSV
df = pd.read_csv("dataset/amazon_products_cleaned.csv")
df = df.fillna("")


def extract_price(value):
    """Convert ₹1,999 or 1999.0 into integer."""
    value = str(value)
    value = re.sub(r"[^\d.]", "", value)

    try:
        return int(float(value))
    except:
        return 0


products = []

for index, row in df.iterrows():

    # Category Mapping
    category = str(row["category"]).lower()

    if "shoe" in category or "fashion" in category or "clothing" in category:
        dashboard_category = "Fashion"
        icon = "fa-shoe-prints"

    elif "electronic" in category or "computer" in category or "mobile" in category:
        dashboard_category = "Electronics"
        icon = "fa-mobile-screen-button"

    elif "home" in category or "furniture" in category:
        dashboard_category = "Home & Furniture"
        icon = "fa-chair"

    else:
        dashboard_category = "Grocery"
        icon = "fa-apple-whole"

    products.append({

        "id": index + 1,

        "name": row["product_name"],

        "category": dashboard_category,

        "sub": row["brand"],

        "price": extract_price(row["price"]),

        "mrp": extract_price(row["actual_price"]),

        "rating": float(row["rating"]) if str(row["rating"]).replace(".", "", 1).isdigit() else 4.0,

        "reviews": extract_price(row["rating_count"]),

        "icon": icon,

        "description": row["description"]

    })


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        products_json=json.dumps(products)
    )


if __name__ == "__main__":
=======
from flask import Flask, render_template
import pandas as pd
import json
import re

app = Flask(__name__)

# Load CSV
df = pd.read_csv("dataset/amazon_products_cleaned.csv")
df = df.fillna("")


def extract_price(value):
    """Convert ₹1,999 or 1999.0 into integer."""
    value = str(value)
    value = re.sub(r"[^\d.]", "", value)

    try:
        return int(float(value))
    except:
        return 0


products = []

for index, row in df.iterrows():

    # Category Mapping
    category = str(row["category"]).lower()

    if "shoe" in category or "fashion" in category or "clothing" in category:
        dashboard_category = "Fashion"
        icon = "fa-shoe-prints"

    elif "electronic" in category or "computer" in category or "mobile" in category:
        dashboard_category = "Electronics"
        icon = "fa-mobile-screen-button"

    elif "home" in category or "furniture" in category:
        dashboard_category = "Home & Furniture"
        icon = "fa-chair"

    else:
        dashboard_category = "Grocery"
        icon = "fa-apple-whole"

    products.append({

        "id": index + 1,

        "name": row["product_name"],

        "category": dashboard_category,

        "sub": row["brand"],

        "price": extract_price(row["price"]),

        "mrp": extract_price(row["actual_price"]),

        "rating": float(row["rating"]) if str(row["rating"]).replace(".", "", 1).isdigit() else 4.0,

        "reviews": extract_price(row["rating_count"]),

        "icon": icon,

        "description": row["description"]

    })


@app.route("/")
def dashboard():
    return render_template(
        "dashboard.html",
        products_json=json.dumps(products)
    )


if __name__ == "__main__":
>>>>>>> 87c0f61b754d0f9694856135e0d5c59efb2bd60b
    app.run(debug=True)