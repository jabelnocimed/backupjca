
from sundry import to_bool

from compare_dirs import compare_dirs


def test_compare_dirs():

    for test_type in range(0, 8):

        use_mtime = to_bool(test_type & 1)
        quiet = to_bool(test_type & 2 == 2)
        use_hash = to_bool(test_type & 4 == 4)

        compare_count, micompare_count = compare_dirs("venv", "venv", use_mtime, quiet, use_hash)
        assert(compare_count > 0)
        assert(micompare_count == 0)

        compare_count, micompare_count = compare_dirs("test", "venv", use_mtime, quiet, use_hash)
        assert(compare_count > 0)
        assert(micompare_count > 0)

        compare_count, micompare_count = compare_dirs("venv", "test", use_mtime, quiet, use_hash)
        assert(compare_count > 0)
        assert(micompare_count > 0)


if __name__ == "__main__":
    test_compare_dirs()
