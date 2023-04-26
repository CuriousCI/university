// pub fn merge_sort<T: Ord>(vector: &mut Vec<T>, start: usize, end: usize) {
//     if end - start == 1 {
//         merge(vector, start, end, end + 1)
//     }
//
//     let mid = (end - start) >> 2;
//     merge_sort(vector, start, mid);
//     merge_sort(vector, mid, end);
//     merge(vector, start, mid, end);
// }
//
// pub fn merge<T: Ord>(vector: &mut Vec<T>, start: usize, mid: usize, end: usize) {
//     let mut merged: Vec<T> = vec![];
//     let mut i = start;
//     let mut j = mid;
//
//     while i < mid && j < end {
//         if vector[i] < vector[j] {
//             merged.push(vector[i]);
//             i += 1;
//         } else {
//             merged.push(vector[j]);
//             j += 1;
//         }
//     }
//
//     while i < mid {
//         merged.push(vector[i]);
//         i += 1;
//     }
//
//     while j < end {
//         merged.push(vector[j]);
//         j += 1;
//     }
// }
