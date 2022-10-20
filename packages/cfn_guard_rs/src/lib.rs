use pyo3::prelude::*;
use cfn_guard::{run_checks, ValidateInput};
mod errors;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn run_checks_rs(data: &str, rules: &str, verbose: bool) -> Result<String, errors::CfnGuardError> {
    let result = run_checks(ValidateInput { content: data, file_name: ""}, ValidateInput { content: rules, file_name: ""}, verbose)?;
    Ok(result)
}

/// A Python module implemented in Rust.
#[pymodule]
fn cfn_guard_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add("JsonError", _py.get_type::<errors::JsonError>())?;
    m.add("YamlError", _py.get_type::<errors::YamlError>())?;
    m.add("FormatError", _py.get_type::<errors::FormatError>())?;
    m.add("IoError", _py.get_type::<errors::IoError>())?;
    m.add("RegexError", _py.get_type::<errors::RegexError>())?;
    m.add("ParseError", _py.get_type::<errors::ParseError>())?;
    m.add("MissingProperty", _py.get_type::<errors::MissingProperty>())?;
    m.add("MissingVariable", _py.get_type::<errors::MissingVariable>())?;
    m.add("MultipleValues", _py.get_type::<errors::MultipleValues>())?;
    m.add("IncompatibleRetrievalError", _py.get_type::<errors::IncompatibleRetrievalError>())?;
    m.add("IncompatibleError", _py.get_type::<errors::IncompatibleError>())?;
    m.add("NotComparable", _py.get_type::<errors::NotComparable>())?;
    m.add("ConversionError", _py.get_type::<errors::ConversionError>())?;
    m.add("Errors", _py.get_type::<errors::Errors>())?;
    m.add("RetrievalError", _py.get_type::<errors::RetrievalError>())?;
    m.add("MissingValue", _py.get_type::<errors::MissingValue>())?;
    m.add("FileNotFoundError", _py.get_type::<errors::FileNotFoundError>())?;
    m.add_function(wrap_pyfunction!(run_checks_rs, m)?)?;
    Ok(())
}
