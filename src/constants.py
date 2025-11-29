from src.sorting.bubble_sort import bubble_sort
from src.sorting.bucket_sort import bucket_sort
from src.sorting.counting_sort import counting_sort
from src.sorting.heap_sort import heap_sort
from src.sorting.quick_sort import quick_sort
from src.sorting.radix_sort import radix_sort

ALL_SORTS = SORTS = {
    "bubble": bubble_sort,
    "bucket": bucket_sort,
    "quick": quick_sort,
    "heap": heap_sort,
    "counting": counting_sort,
    "radix": radix_sort,
}

SORTS_FLOAT = {
    "bubble": bubble_sort,
    "bucket": bucket_sort,
    "heap": heap_sort,
}
