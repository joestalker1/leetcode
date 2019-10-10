package cp;

import java.util.*;

public class ShortPathWIthFewestEdge {
    private static class VertexWithDistance {
        public GraphVertex vertex;
        public Integer distance;

        public VertexWithDistance(GraphVertex vertex, Integer distance) {
            this.vertex = vertex;
            this.distance = distance;
        }
    }

    private static class DistanceWithFewestEdges {
        public Integer distance;
        public Integer minNumEdges;

        public DistanceWithFewestEdges(Integer distance, Integer minNumEdges) {
            this.distance = distance;
            this.minNumEdges = minNumEdges;
        }
    }

    static class GraphVertex implements Comparable<GraphVertex> {
        public DistanceWithFewestEdges distanceWithFewestEdges = new DistanceWithFewestEdges(Integer.MAX_VALUE, 0);
        public List<VertexWithDistance> edges = new ArrayList<>();
        public int id; // The id of this vertex.
        public GraphVertex pred = null; // The predecessor in the shortest path.

        @Override
        public int compareTo(GraphVertex o) {
            if (distanceWithFewestEdges.distance
                    != o.distanceWithFewestEdges.distance) {
                return Integer.compare(distanceWithFewestEdges.distance,
                        o.distanceWithFewestEdges.distance);
            }
            if (distanceWithFewestEdges.minNumEdges
                    != o.distanceWithFewestEdges.minNumEdges) {
                return Integer.compare(distanceWithFewestEdges.minNumEdges,
                        o.distanceWithFewestEdges.minNumEdges);
            }
            return Integer.compare(id, o.id);
        }

        @Override
        public boolean equals(Object obj) {
            if (obj == null || !(obj instanceof GraphVertex)) {
                return false;
            }
            if (this == obj) {
                return true;
            }
            GraphVertex that = (GraphVertex) obj;
            return id == that.id
                    && distanceWithFewestEdges.distance.equals(
                    that.distanceWithFewestEdges.distance)
                    && distanceWithFewestEdges.minNumEdges.equals(
                    that.distanceWithFewestEdges.minNumEdges);
        }

        @Override
        public int hashCode() {
            return Objects.hash(distanceWithFewestEdges.distance,
                    distanceWithFewestEdges.minNumEdges);
        }
    }

    public static void dijkstraShortestPath(GraphVertex s, GraphVertex t) {
        // Initialization of the distance of starting point.
        s.distanceWithFewestEdges = new DistanceWithFewestEdges(0, 0);
        SortedSet<GraphVertex> nodeSet = new TreeSet<>();
        nodeSet.add(s);
        while (!nodeSet.isEmpty()) {
           // Extracts the minimum distance vertex from heap.
            GraphVertex u = nodeSet.first();
            if (u.equals(t)) {
                break;
            }
            nodeSet.remove(nodeSet.first());
            // Relax neighboring vertices of u.
            for (VertexWithDistance v : u.edges) {
                int vDistance = u.distanceWithFewestEdges.distance + v.distance;
                int vNumEdges = u.distanceWithFewestEdges.minNumEdges + 1;
                if (v.vertex.distanceWithFewestEdges.distance > vDistance
                        || (v.vertex.distanceWithFewestEdges.distance == vDistance
                        && v.vertex.distanceWithFewestEdges.minNumEdges > vNumEdges)) {
                    nodeSet.remove(v.vertex);
                    v.vertex.pred = u;
                    v.vertex.distanceWithFewestEdges
                            = new DistanceWithFewestEdges(vDistance, vNumEdges);
                    nodeSet.add(v.vertex);
                }
            }
            // Outputs the shortest path with fewest edges.
            outputShortestPath(t);
        }
    }

    private static void outputShortestPath(GraphVertex v) {
        if (v != null) {
            outputShortestPath(v.pred);
            System.out.print(v.id + " ");
        }
    }
}