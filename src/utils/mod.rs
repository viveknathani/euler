pub fn is_prime_naive(n: u64) -> bool {
    if n == 0 || n == 1 {
        return false;
    }

    let mut i = 2;
    while i <= n / 2 {
        if n % i == 0 {
            return false;
        }
        i += 1;
    }

    true
}
