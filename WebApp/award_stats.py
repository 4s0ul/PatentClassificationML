def award_stats(awards):
    sum_of_awards = sum(awards)
    avg_award = sum_of_awards // len(awards)
    return sum_of_awards, avg_award