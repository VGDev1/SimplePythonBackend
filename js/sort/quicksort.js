const items = [5, 3, 7, 6, 2, 9, 16];
function swap(items, leftIndex, rightIndex) {
    var temp = items[leftIndex];
    items[leftIndex] = items[rightIndex];
    items[rightIndex] = temp;
}
function partition(items, left, right) {
    var pivot = items[Math.floor((right + left) / 2)], // jävla js
        i = left,
        j = right;
    while (i <= j) {
        while (items[i] < pivot) {
            i++;
        }
        while (items[j] > pivot) {
            j--;
        }
        if (i <= j) {
            swap(items, i, j);
            i++;
            j--;
        }
    }
    return i;
}

function _quickSort(items, left, right) {
    let index;
    if (items.length > 1) {
        index = partition(items, left, right);
        if (left < index - 1) {
            _quickSort(items, left, index - 1);
        }
        if (index < right) {
            _quickSort(items, index, right);
        }
    }
    return items;
}

function quickSort(items) {
    return _quickSort(items, 0, items.length - 1);
}

quickSort(items);

exports.quickSort = quickSort;
