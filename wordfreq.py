# REQ: pg16317.txt downloaded from https://www.gutenberg.org/cache/epub/16317/pg16317.txt

def get_counts(fname: str) -> dict[str,int]:
  """Get the word frequencies for a given text file"""

  with open(fname, "r", encoding="utf-8-sig") as f:
    corpus = f.readlines()

  # compute word counts
  counts = {}
  for line in corpus:
    words = line.split()
    for word in words:
      word = word.lower()
      if word not in counts:
        counts[word] = 0
      counts[word] += 1

  return counts

def get_freqs(counts:dict[str,int], low: int, high: int):
  """Order words by frequency, extract low to high."""
  return sorted(counts.items(), key=lambda x: x[1], reverse=True)[low-1:high]

if __name__ == "__main__":
  counts = get_counts("pg16317.txt")
  freqs = get_freqs(counts, 10, 20)
  print("Words ranked from 10th to 20th by frequency:")
  for w, c in freqs:
    print(f"{w}: {c}")