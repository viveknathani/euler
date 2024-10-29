use std::time::Instant;

use euler::problems::{p0001, p0002};

fn main() {
    let problem_number = std::env::args().nth(1).expect("expect a problem number");

    let start_time = Instant::now();

    match problem_number.as_str() {
        "1" => p0001::solve(),
        "2" => p0002::solve(),
        _ => println!("Unknown problem number"),
    }

    let duration = start_time.elapsed();

    println!(
        "problem {:} took {:}ms",
        problem_number,
        duration.as_millis()
    );
}
