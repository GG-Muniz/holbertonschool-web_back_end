# Pagination

Project implementing server-side pagination in Python.

- Python: 3.9
- Style: pycodestyle 2.5.*
- Dataset: `Popular_Baby_Names.csv`

## Files
- `0-simple_helper_function.py`: `index_range(page, page_size)` helper.
- `1-simple_pagination.py`: `Server` with `get_page`.
- `2-hypermedia_pagination.py`: `Server` with `get_hyper`.
- `3-hypermedia_del_pagination.py`: `Server` with deletion-resilient `get_hyper_index`.

## Notes
- All functions and modules include docstrings and type hints.
- Page numbers are 1-indexed for `get_page` / `get_hyper`.
- `get_hyper_index` starts from a 0-based `index` and skips deleted entries. 