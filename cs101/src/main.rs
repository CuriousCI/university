use algorithms::naive_sorting::insertion_sort;

fn main() {
    let mut v = vec![
        10, 1290, 21904, 290, -19, 910, 09201, 8012, 980122220, 09, -12801, -29, 2901,
    ];

    insertion_sort(&mut v);

    println!("{:?}", v);
}
