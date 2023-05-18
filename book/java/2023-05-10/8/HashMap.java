import java.util.HashSet;
import java.util.Optional;
import java.util.Collection;
import java.util.Set;
import java.util.stream.Collectors;

public class HashMap<K, V> {
    private HashSet<Pair<K, V>> set;

    public HashMap() {
        set = new HashSet<>();
    }

    public void put(K key, V value) {
        set.add(new Pair<>(key, value));
    }

    public Optional<V> get(K key) {
        var pair = set.stream().filter((p) -> p.getFirst() == key).findFirst();

        if (pair.isEmpty())
            return Optional.empty();

        return Optional.of(pair.get().getSecond());

    }

    public Optional<V> remove(K key) {
        var pair = set.stream().filter((p) -> p.getFirst() == key).findFirst();

        if (pair.isEmpty())
            return Optional.empty();

        set.remove(pair.get());
        return Optional.of(pair.get().getSecond());
    }

    public Set<K> keySet() {
        return set.stream().map((p) -> p.getFirst()).collect(Collectors.toSet());
    }

    public int size() {
        return set.size();
    }
}
