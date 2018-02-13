package lpht;

import java.util.Collection;

/**
 * 2. То, что имеет место, что является фактом, - это существование атомарных фактов.
 */
public class AtomicFact extends Fact {
    IsTheCase theCase;
    Collection<Object> objects;
}
