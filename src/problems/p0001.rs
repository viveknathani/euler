pub fn solve() {
    let mut sum = 0;
    let mut i = 0;

    while i < 1000 {
        if i % 3 == 0 || i % 5 == 0 {
            sum += i;
        }
        i += 1;
    }

    println!("{:?}", sum);
}
