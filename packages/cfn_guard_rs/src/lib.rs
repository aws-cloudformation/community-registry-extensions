use pyo3::prelude::*;
use cfn_guard;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn run_checks_rs(data: &str, rules: &str, verbose: bool) -> PyResult<String> {
    let result = match cfn_guard::run_checks(data, rules, verbose)
    {
        Ok(t) => t,
        Err(e) => (e.to_string()),
    };
    Ok(result)
}

/// A Python module implemented in Rust.
#[pymodule]
fn cfn_guard_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(run_checks_rs, m)?)?;
    Ok(())
}
