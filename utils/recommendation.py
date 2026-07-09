import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Load dataset
df = pd.read_csv("dataset/amazon_products_cleaned.csv")

# Missing values handle
df = df.fillna("")


# Combine important features
df["combined_features"] = (
    df["product_name"].astype(str) + " " +
    df["category"].astype(str) + " " +
    df["brand"].astype(str) + " " +
    df["description"].astype(str)
)


# TF-IDF Model
tfidf = TfidfVectorizer(stop_words="english")

tfidf_matrix = tfidf.fit_transform(df["combined_features"])


# Similarity Matrix
cosine_sim = cosine_similarity(tfidf_matrix)


def recommend(product_name, top_n=5):

    product_index = df[
        df["product_name"].str.lower() == product_name.lower()
    ].index


    if len(product_index) == 0:
        return "Product not found"


    index = product_index[0]


    similarity_scores = list(
        enumerate(cosine_sim[index])
    )


    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )


    selected_price = float(df.iloc[index]["price"])


    recommendations = []


    for i, score in similarity_scores[1:]:

        product_price = float(df.iloc[i]["price"])

        product_rating = float(df.iloc[i]["rating"])


        # Similar price range (+/-20%)
        if abs(product_price - selected_price) <= selected_price * 0.20:

            recommendations.append(
                df.iloc[i]
            )


    result = pd.DataFrame(recommendations)


    # Higher rating first
    result = result.sort_values(
        by="rating",
        ascending=False
    )


    return result.head(top_n)



if __name__ == "__main__":

    product = df.iloc[0]["product_name"]

    print("Selected Product:")
    print(product)

    print("\nRecommended Products:")

    print(recommend(product))