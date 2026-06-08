def calculate_confidence(distances):

    if not distances:
        return 0

    valid_distances = []

    for d in distances:

        if d < 1000:
            valid_distances.append(d)

    if not valid_distances:
        return 0

    avg_distance = (
    sum(valid_distances)
    / len(valid_distances)
    )

    confidence = int(
    max(
        0,
        min(
            100,
            (1.2 - avg_distance) * 100
        )
    )
)

    return confidence


def confidence_label(score):

    if score >= 80:
        return "High"

    elif score >= 60:
        return "Medium"

    else:
        return "Low"