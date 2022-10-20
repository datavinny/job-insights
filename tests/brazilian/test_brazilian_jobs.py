from src.brazilian_jobs import read_brazilian_file


PATH = "tests/mocks/brazilians_jobs.csv"


def test_brazilian_jobs():
    results = read_brazilian_file(PATH)
    assert type(results) == list
    for result in results:
        assert type(result) == dict

    assert "title" in results[0]
    assert "salary" in results[0]
    assert "type" in results[0]
