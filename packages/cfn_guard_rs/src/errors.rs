use pyo3::{
    PyErr,
    create_exception,
    import_exception,
    exceptions,
};
use cfn_guard::{Error, ErrorKind};

import_exception!(json, JSONDecodeError);
import_exception!(yaml, YAMLError);

create_exception!(cfn_guard_rs, CfnGuardJsonError, JSONDecodeError);
create_exception!(cfn_guard_rs, CfnGuardYamlError, YAMLError);
create_exception!(cfn_guard_rs, CfnGuardIoError, exceptions::PyIOError);
create_exception!(cfn_guard_rs, CfnGuardFileNotFoundError, exceptions::PyFileNotFoundError);

// ParseError
create_exception!(cfn_guard_rs, CfnGuardParseError, exceptions::PyValueError);
// Value cannot be resolved
create_exception!(cfn_guard_rs, CfnGuardMissingValue, exceptions::PyNameError);

// Captured by rule evaluations
create_exception!(cfn_guard_rs, CfnGuardMissingVariable, exceptions::PyAttributeError);
create_exception!(cfn_guard_rs, CfnGuardMultipleValues, exceptions::PyValueError);
create_exception!(cfn_guard_rs, CfnGuardIncompatibleRetrievalError, exceptions::PyTypeError);
create_exception!(cfn_guard_rs, CfnGuardIncompatibleError, exceptions::PyTypeError);
create_exception!(cfn_guard_rs, CfnGuardNotComparable, exceptions::PyTypeError);
create_exception!(cfn_guard_rs, CfnGuardRetrievalError, exceptions::PyException);

// Can't find where these errors are actually used
create_exception!(cfn_guard_rs, CfnGuardFormatError, exceptions::PyException);
create_exception!(cfn_guard_rs, CfnGuardRegexError, exceptions::PyException);
create_exception!(cfn_guard_rs, CfnGuardMissingProperty, exceptions::PyException);
create_exception!(cfn_guard_rs, CfnGuardConversionError, exceptions::PyException);
create_exception!(cfn_guard_rs, CfnGuardErrors, exceptions::PyException);

pub struct CfnGuardError(pub Error);

impl From<Error> for CfnGuardError {
    fn from(err: Error) -> Self {
        Self(err)
    }
}

impl From<CfnGuardError> for PyErr {
    fn from(err: CfnGuardError) -> Self {
        let e = &err.0;
        match &e.0 {
            ErrorKind::JsonError(err) => CfnGuardJsonError::new_err(format!("{}", err)),
            ErrorKind::YamlError(err) => CfnGuardYamlError::new_err(format!("{}", err)),
            ErrorKind::FormatError(err) => CfnGuardFormatError::new_err(format!("{}", err)),
            ErrorKind::IoError(err) => CfnGuardIoError::new_err(format!("{}", err)),
            ErrorKind::ParseError(err) => CfnGuardParseError::new_err(format!("{}", err)),
            ErrorKind::RegexError(err) => CfnGuardRegexError::new_err(format!("{}", err)),
            ErrorKind::MissingProperty(err) => CfnGuardMissingProperty::new_err(format!("{}", err)),
            ErrorKind::MissingVariable(err) => CfnGuardMissingVariable::new_err(format!("{}", err)),
            ErrorKind::MultipleValues(err) => CfnGuardMultipleValues::new_err(format!("{}", err)),
            ErrorKind::IncompatibleRetrievalError(err) => CfnGuardIncompatibleRetrievalError::new_err(format!("{}", err)),
            ErrorKind::IncompatibleError(err) => CfnGuardIncompatibleError::new_err(format!("{}", err)),
            ErrorKind::NotComparable(err) => CfnGuardNotComparable::new_err(format!("{}", err)),
            ErrorKind::ConversionError(err) => CfnGuardConversionError::new_err(format!("{}", err)),
            ErrorKind::Errors(_err) => CfnGuardErrors::new_err("multiple errors"),
            ErrorKind::RetrievalError(err) => CfnGuardRetrievalError::new_err(format!("{}", err)),
            ErrorKind::MissingValue(err) => CfnGuardMissingValue::new_err(format!("{}", err)),
            ErrorKind::FileNotFoundError(err) => CfnGuardFileNotFoundError::new_err(format!("{}", err)),
        }
    }
}