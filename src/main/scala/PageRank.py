class PageRank:
    def __init__(self, links, d=0.85, num_rounds=10):
        self.d = d
        self.num_rounds = num_rounds
        self.num_sites = len(links)
        self.outlinks = links
        self.inlinks = self.get_inlinks()
        self.scores = {site: 1.0 / self.num_sites for site in links}

    def get_inlinks(self):
        inlinks = {site: [] for site in self.outlinks}

        for site, neighbors in self.outlinks.items():
            for neighbor in neighbors:
                inlinks[neighbor].append(site)

        return inlinks

    def update_scores(self):
        for _ in range(self.num_rounds):
            new_scores = {}

            for site, neighbors in self.inlinks.items():
                score = sum([self.scores[neighbor] / len(self.outlinks[neighbor]) for neighbor in neighbors])
                new_scores[site] = (1.0 - self.d) / self.num_sites + self.d * score

            self.scores.update(new_scores)

    def get_ranks(self):
        return {site: round(score, 2) for site, score in self.scores.items()}


pg_rank = PageRank({
    0: [1, 2, 3],
    1: [0],
    2: [0],
    3: [0]
})
pg_rank.update_scores()
print(pg_rank.get_ranks())
