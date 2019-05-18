import java.util.Collections;
import java.util.List;
import java.util.Map;
import java.util.HashMap;
import java.util.PriorityQueue;
import java.util.Comparator;
import java.util.ArrayList;

public class TopKFrequentWords {
    static class WordFreq {
        WordFreq(String w, int f) {
            this.word = w;
            this.frequency = f;
        }

        String word;
        int frequency;
    }

    static Comparator<WordFreq> minFreqMaxWord =
            (o1, o2) -> (o1.frequency == o2.frequency) ? o2.word.compareTo(o1.word) : o1.frequency - o2.frequency;


    public List<String> topKFrequent(String[] words, int k) {
        if (words == null || k == 0 || k > words.length) {
            return Collections.EMPTY_LIST;        }

        Map<String, Integer> m = new HashMap<>();
        for (String word : words) {
            m.put(word, m.getOrDefault(word, 0) + 1);
        }
        PriorityQueue<WordFreq> pq = new PriorityQueue<>(minFreqMaxWord);
        for (String word : m.keySet()) {
            int freq = m.get(word);
            pq.offer(new WordFreq(word, freq));
            if (pq.size() > k) pq.poll();
        }
        List<String> res = new ArrayList<>();
        while (!pq.isEmpty()) {
            res.add(pq.poll().word);
        }
        Collections.reverse(res);
        return res;
    }

    public static void main(String... args) {
        TopKFrequentWords alg = new TopKFrequentWords();
        System.out.println(alg.topKFrequent(new String[]{"the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"}, 4));
        System.out.println(alg.topKFrequent(new String[]{"a", "aa", "aaa"}, 2));
    }
}
