def normalize_weights(weights):
    total = (
        weights.cognitive +
        weights.time +
        weights.learning +
        weights.emotion
    )

    if total == 0:
        raise ValueError("Sum of weights cannot be zero")

    return {
        "cognitive": weights.cognitive / total,
        "time": weights.time / total,
        "learning": weights.learning / total,
        "emotion": weights.emotion / total,
    }


def evaluate_books(data):
    weights = normalize_weights(data.weights)

    results = []

    for book in data.books:
        # Cognitive score (lower complexity better)
        cognitive_score = (5 - book.complexity) / 4

        # Time score
        reading_time = book.pages / data.reading_speed
        if reading_time <= data.available_hours:
            time_score = 1
        else:
            time_score = data.available_hours / reading_time

        # Learning score
        learning_score = book.learning_depth / 5

        # Emotion score
        emotion_score = book.emotional_intensity / 5

        total_score = (
            weights["cognitive"] * cognitive_score +
            weights["time"] * time_score +
            weights["learning"] * learning_score +
            weights["emotion"] * emotion_score
        )

        results.append({
            "name": book.name,
            "scores": {
                "cognitive": cognitive_score * weights["cognitive"],
                "time": time_score * weights["time"],
                "learning": learning_score * weights["learning"],
                "emotion": emotion_score * weights["emotion"],
            },
            "total_score": round(total_score, 4)
        })

    results.sort(key=lambda x: x["total_score"], reverse=True)

    for i, r in enumerate(results):
        r["rank"] = i + 1

    return results