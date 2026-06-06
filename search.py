from rapidfuzz import process, fuzz
from loader import DATASETS

def search_dataset(table: str, query: str):

    if table not in DATASETS:
        return []

    rows = DATASETS[table]

    query = query.strip()

    # Fast path: code search
    if query and query[0].isalpha() and any(c.isdigit() for c in query):
        results = []
        for r in rows:
            if r["Code"].startswith(query.upper()):
                results.append({
                    "Code": r["Code"],
                    "Headings": r["Headings"],
                    "Description": r["Description"],
                    "score": 100
                })
        return results[:20]

    # Fuzzy search across ALL fields
    choices = [r["search_blob"] for r in rows]

    matches = process.extract(
        query,
        choices,
        scorer=fuzz.token_set_ratio,
        limit=20
    )

    results = []
    for match, score, idx in matches:
        r = rows[idx]

        # slight boost if code matches partially
        if r["Code"].startswith(query.upper()):
            score += 10

        results.append({
            "Code": r["Code"],
            "Headings": r["Headings"],
            "Description": r["Description"],
            "score": score
        })

    # sort again after boosting
    results.sort(key=lambda x: x["score"], reverse=True)

    return results