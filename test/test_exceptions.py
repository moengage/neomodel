from neomodel import StructuredNode, StringProperty, DoesNotExist, CypherException
import pickle


class Person(StructuredNode):
    name = StringProperty(unique_index=True)


def test_cypher_exception_can_be_displayed():
    print(CypherException("SOME QUERY", (), "ERROR", None, None))

def test_object_does_not_exist():
    try:
        Person.nodes.get(name="johnny")
    except Person.DoesNotExist as e:
        pickle_instance = pickle.dumps(e)
        assert pickle_instance
        assert pickle.loads(pickle_instance)
        assert isinstance(pickle.loads(pickle_instance), DoesNotExist)


def test_raise_does_not_exist():
    try:
        raise DoesNotExist("My Test Message")
    except DoesNotExist as e:
        pickle_instance = pickle.dumps(e)
        assert pickle_instance
        assert pickle.loads(pickle_instance)
        assert isinstance(pickle.loads(pickle_instance), DoesNotExist)
