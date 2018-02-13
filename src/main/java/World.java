import java.util.Collection;

/**
 * 1. Мир есть все то, что имеет место.
 * 1.1 Мир есть совокупность фактов, а не предметов.
 * 1.11 Мир определен фактами и тем, что это все факты.
 */
public abstract class World implements Collection<Fact>{
    Collection<IsTheCase> all;
}
