use std::cmp::max;

use crate::utils::is_prime_naive;

pub fn solve() {
    let n: u64 = 600851475143;
    let mut result = 1;
    let mut i = 1;
    let upper_limit = (n as f64).sqrt() as u64;

    while i <= upper_limit {
        if n % i == 0 {
            if is_prime_naive(i) {
                result = max(result, i);
            }
            if is_prime_naive(n / i) {
                result = max(result, n / i);
            }
        }
        i += 1;
    }

    println!("{:}", result);
}
