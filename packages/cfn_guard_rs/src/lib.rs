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
    // cfn-guard-rs currently doesn't allow for parsing files
    m.add("_CfnGuardJsonError", _py.get_type::<errors::CfnGuardJsonError>())?;
    m.add("_CfnGuardYamlError", _py.get_type::<errors::CfnGuardYamlError>())?;
    m.add("_CfnGuardIoError", _py.get_type::<errors::CfnGuardIoError>())?;
    m.add("_CfnGuardFileNotFoundError", _py.get_type::<errors::CfnGuardFileNotFoundError>())?;

    // unused errors
    m.add("_CfnGuardFormatError", _py.get_type::<errors::CfnGuardFormatError>())?;
    m.add("_CfnGuardRegexError", _py.get_type::<errors::CfnGuardRegexError>())?;
    m.add("_CfnGuardMissingProperty", _py.get_type::<errors::CfnGuardMissingProperty>())?;
    m.add("_CfnGuardConversionError", _py.get_type::<errors::CfnGuardConversionError>())?;
    m.add("_CfnGuardErrors", _py.get_type::<errors::CfnGuardErrors>())?;
    
    // masked and captured by rule processing
    m.add("_CfnGuardMultipleValues", _py.get_type::<errors::CfnGuardMultipleValues>())?;
    m.add("_CfnGuardIncompatibleRetrievalError", _py.get_type::<errors::CfnGuardIncompatibleRetrievalError>())?;
    m.add("_CfnGuardIncompatibleError", _py.get_type::<errors::CfnGuardIncompatibleError>())?;
    m.add("_CfnGuardNotComparable", _py.get_type::<errors::CfnGuardNotComparable>())?;
    m.add("_CfnGuardRetrievalError", _py.get_type::<errors::CfnGuardRetrievalError>())?;
    m.add("_CfnGuardMissingVariable", _py.get_type::<errors::CfnGuardMissingVariable>())?;

    // Exceptions that may get passed back
    m.add("CfnGuardParseError", _py.get_type::<errors::CfnGuardParseError>())?;
    m.add("CfnGuardMissingValue", _py.get_type::<errors::CfnGuardMissingValue>())?;
    
    m.add_function(wrap_pyfunction!(run_checks_rs, m)?)?;
    Ok(())
}
