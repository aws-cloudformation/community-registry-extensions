use pyo3::{
    PyErr,
    create_exception,
    import_exception,
    exceptions,
};
use cfn_guard::Error;

import_exception!(json, JSONDecodeError);
import_exception!(yaml, YAMLError);

create_exception!(cfn_guard_rs, CfnGuardJsonError, JSONDecodeError);
create_exception!(cfn_guard_rs, CfnGuardYamlError, YAMLError);
create_exception!(cfn_guard_rs, CfnGuardIoError, exceptions::PyIOError);
create_exception!(cfn_guard_rs, CfnGuardFileNotFoundError, exceptions::PyFileNotFoundError);
create_exception!(cfn_guard_rs, CfnGuardIllegalArguments, exceptions::PyValueError);
create_exception!(cfn_guard_rs, CfnGuardInternalError, exceptions::PyException);

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
        match &err.0 {
            Error::JsonError(err) => CfnGuardJsonError::new_err(format!("{}", err)),
            Error::YamlError(err) => CfnGuardYamlError::new_err(format!("{}", err)),
            Error::FormatError(err) => CfnGuardFormatError::new_err(format!("{}", err)),
            Error::IoError(err) => CfnGuardIoError::new_err(format!("{}", err)),
            Error::ParseError(err) => CfnGuardParseError::new_err(format!("{}", err)),
            Error::RegexError(err) => CfnGuardRegexError::new_err(format!("{}", err)),
            Error::MissingProperty(err) => CfnGuardMissingProperty::new_err(format!("{}", err)),
            Error::MissingVariable(err) => CfnGuardMissingVariable::new_err(format!("{}", err)),
            Error::MultipleValues(err) => CfnGuardMultipleValues::new_err(format!("{}", err)),
            Error::IncompatibleRetrievalError(err) => CfnGuardIncompatibleRetrievalError::new_err(format!("{}", err)),
            Error::IncompatibleError(err) => CfnGuardIncompatibleError::new_err(format!("{}", err)),
            Error::NotComparable(err) => CfnGuardNotComparable::new_err(format!("{}", err)),
            Error::ConversionError(err) => CfnGuardConversionError::new_err(format!("{}", err)),
            Error::Errors(_err) => CfnGuardErrors::new_err("multiple errors"),
            Error::RetrievalError(err) => CfnGuardRetrievalError::new_err(format!("{}", err)),
            Error::MissingValue(err) => CfnGuardMissingValue::new_err(format!("{}", err)),
            Error::FileNotFoundError(err) => CfnGuardFileNotFoundError::new_err(format!("{}", err)),
            Error::IllegalArguments(err) => CfnGuardIllegalArguments::new_err(format!("{}", err)),
            Error::InternalError(err) => CfnGuardInternalError::new_err(format!("{}", err)),
        }
    }
}
