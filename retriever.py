import pandas as pd

df = pd.read_csv("shl_catalog.csv")

def search_assessments(query):

    query_words = query.lower().split()

    scored_results = []

    for _, row in df.iterrows():

        name = str(row["name"]).lower()

        score = 0

        for word in query_words:
            if word in name:
                score += 1

        if score > 0:
            scored_results.append({
                "score": score,
                "name": row["name"],
                "url": row["url"],
                "test_type": "Assessment"
            })

    scored_results.sort(
        key=lambda x: x["score"],
        reverse=True
    )

    return scored_results[:10]