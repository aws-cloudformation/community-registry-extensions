use pyo3::{
    PyErr,
    create_exception,
    import_exception,
    exceptions,
};
use cfn_guard::{Error, ErrorKind};

import_exception!(json, JSONDecodeError);
import_exception!(yaml, YAMLError);

create_exception!(cfn_guard_rs, JsonError, JSONDecodeError);
create_exception!(cfn_guard_rs, YamlError, YAMLError);
// Standard IO Error
create_exception!(cfn_guard_rs, IoError, exceptions::PyIOError);
// ParseError is used a lot
create_exception!(cfn_guard_rs, ParseError, exceptions::PyValueError);
// When a variable isn't found in the in the rule
create_exception!(cfn_guard_rs, MissingVariable, exceptions::PyAttributeError);
// Key already exists in map
create_exception!(cfn_guard_rs, MultipleValues, exceptions::PyValueError);
// Used in lots of locations. Type or variable has incompatible types
create_exception!(cfn_guard_rs, IncompatibleRetrievalError, exceptions::PyTypeError);
// Used in lots of locations. Types or variable assignments are incompatible
create_exception!(cfn_guard_rs, IncompatibleError, exceptions::PyTypeError);
// Used in lots of locations. Comparing incoming context with literals or dynamic results wasn't possible
create_exception!(cfn_guard_rs, NotComparable, exceptions::PyTypeError);
// Used in lots of locations. Could not retrieve data from incoming context.
create_exception!(cfn_guard_rs, RetrievalError, exceptions::PyException);
// There was no variable or value object to resolve.
create_exception!(cfn_guard_rs, MissingValue, exceptions::PyNameError);
// Standard FileNotFoundError
create_exception!(cfn_guard_rs, FileNotFoundError, exceptions::PyFileNotFoundError);

// Can't find where these errors are actually used
create_exception!(cfn_guard_rs, FormatError, exceptions::PyException);
create_exception!(cfn_guard_rs, RegexError, exceptions::PyException);
create_exception!(cfn_guard_rs, MissingProperty, exceptions::PyException);
create_exception!(cfn_guard_rs, ConversionError, exceptions::PyException);
create_exception!(cfn_guard_rs, Errors, exceptions::PyException);

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