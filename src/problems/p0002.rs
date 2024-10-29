pub fn solve() {
    let max_value = 4_000_000;
    let mut first = 1;
    let mut second = 2;
    let mut current = 0;
    let mut sum = 2;

    while current < max_value {
        current = second + first;
        first = second;
        second = current;

        if current % 2 == 0 {
            sum += current;
        }
    }

    println!("{:}", sum);
}
