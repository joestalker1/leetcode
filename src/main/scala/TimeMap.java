import java.util.HashMap;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;

class TimeMap {
    private Map<String, SortedMap<Integer, String>> keyToTimestamptedValues;

    /** Initialize your data structure here. */
    public TimeMap() {
        keyToTimestamptedValues = new HashMap<>();
    }

    public void set(String key, String value, int timestamp) {
        SortedMap<Integer, String> timestampToKey = keyToTimestamptedValues.getOrDefault(key, new TreeMap<>());
        timestampToKey.put(timestamp, value);
        keyToTimestamptedValues.put(key, timestampToKey);
    }

    public String get(String key, int timestamp) {
        SortedMap<Integer, String> timestampToValues = keyToTimestamptedValues.get(key);
        if(timestampToValues.containsKey(timestamp))
            return timestampToValues.get(timestamp);
        SortedMap<Integer, String> map =  timestampToValues.headMap(timestamp);
        if(map.isEmpty())
            return "";
        int latestTimestamp = map.lastKey();
        return timestampToValues.get(latestTimestamp);
    }

//    ["TimeMap","set","set","get","get","get","get","get"]
//            [[],["love","high",10],["love","low",20],["love",5],["love",10],["love",15],["love",20],["love",25]]

    public static void main(String ... args){
        TimeMap map = new TimeMap();
        map.set("love", "high", 10);
        map.set("love", "low", 20);
        map.get("love", 5);
    }
}
