use std::time::Instant;

use euler::problems::p0001;

fn main() {
    let problem_number = std::env::args().nth(1).expect("expect a problem number");

    let start_time = Instant::now();

    match problem_number.as_str() {
        "1" => p0001::solve(),
        _ => println!("Unknown problem number"),
    }

    let duration = start_time.elapsed();

    println!(
        "problem {:} took {:}ms",
        problem_number,
        duration.as_millis()
    );
}
