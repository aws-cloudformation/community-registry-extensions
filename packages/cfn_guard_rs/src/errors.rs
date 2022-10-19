use pyo3::PyErr;
use pyo3::create_exception;
use pyo3::exceptions::PyException;
use cfn_guard::{Error, ErrorKind};

create_exception!(cfn_guard_rs, JsonError, PyException);
create_exception!(cfn_guard_rs, YamlError, PyException);
create_exception!(cfn_guard_rs, FormatError, PyException);
create_exception!(cfn_guard_rs, IoError, PyException);
create_exception!(cfn_guard_rs, ParseError, PyException);
create_exception!(cfn_guard_rs, RegexError, PyException);
create_exception!(cfn_guard_rs, MissingProperty, PyException);
create_exception!(cfn_guard_rs, MissingVariable, PyException);
create_exception!(cfn_guard_rs, MultipleValues, PyException);
create_exception!(cfn_guard_rs, IncompatibleRetrievalError, PyException);
create_exception!(cfn_guard_rs, IncompatibleError, PyException);
create_exception!(cfn_guard_rs, NotComparable, PyException);
create_exception!(cfn_guard_rs, ConversionError, PyException);
create_exception!(cfn_guard_rs, Errors, PyException);
create_exception!(cfn_guard_rs, RetrievalError, PyException);
create_exception!(cfn_guard_rs, MissingValue, PyException);
create_exception!(cfn_guard_rs, FileNotFoundError, PyException);

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
            ErrorKind::JsonError(err) => JsonError::new_err(format!("{}", err)),
            ErrorKind::YamlError(err) => YamlError::new_err(format!("{}", err)),
            ErrorKind::FormatError(err) => FormatError::new_err(format!("{}", err)),
            ErrorKind::IoError(err) => IoError::new_err(format!("{}", err)),
            ErrorKind::ParseError(err) => ParseError::new_err(format!("{}", err)),
            ErrorKind::RegexError(err) => RegexError::new_err(format!("{}", err)),
            ErrorKind::MissingProperty(err) => MissingProperty::new_err(format!("{}", err)),
            ErrorKind::MissingVariable(err) => MissingVariable::new_err(format!("{}", err)),
            ErrorKind::MultipleValues(err) => MultipleValues::new_err(format!("{}", err)),
            ErrorKind::IncompatibleRetrievalError(err) => IncompatibleRetrievalError::new_err(format!("{}", err)),
            ErrorKind::IncompatibleError(err) => IncompatibleError::new_err(format!("{}", err)),
            ErrorKind::NotComparable(err) => NotComparable::new_err(format!("{}", err)),
            ErrorKind::ConversionError(err) => ConversionError::new_err(format!("{}", err)),
            ErrorKind::Errors(_err) => Errors::new_err("multiple errors"),
            ErrorKind::RetrievalError(err) => RetrievalError::new_err(format!("{}", err)),
            ErrorKind::MissingValue(err) => MissingValue::new_err(format!("{}", err)),
            ErrorKind::FileNotFoundError(err) => FileNotFoundError::new_err(format!("{}", err)),
        }
    }
}