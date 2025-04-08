def soal1(rating):
    ratingterendah = min(rating)
    ratingtertinggi = max(rating)
    ratarating = round(sum(rating) / len(rating), 1)
    return [ratingterendah, ratingtertinggi, ratarating]

rating = [5,4,2.5,5,3.6,1.1,3.6,4,4.2,1.5]
print(f"\nHasil: {soal1(rating)}")