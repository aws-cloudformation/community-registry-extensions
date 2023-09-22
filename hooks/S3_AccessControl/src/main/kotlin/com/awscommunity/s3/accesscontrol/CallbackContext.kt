package com.awscommunity.s3.accesscontrol

import software.amazon.cloudformation.proxy.StdCallbackContext

/**
 * Callback context class, that uses a POJO model (that is, a `data`
 * class in Kotlin).  If needed, this class can be used to persist,
 * across invocations for a given handler (such as, PreCreate for
 * example) information you need, so that you can consume this
 * information from your handler code by using a `ProgressEvent` object,
 * to which you pass an `OperationStatus.IN_PROGRESS` status and an
 * instance of this CallbackContext class with information (properties
 * and values) you need.
 *
 * This hook's scope does not use this functionality at this time; if
 * this were not to be the case, you could have prepended `data` to the
 * class declaration below and you'd have added properties, that you need to
 * persist across invocations, to `CallbackContext`; you could have then
 * been able to access and set values for such properties from within a given
 * handler's (e.g., a PreCreate handler) business logic.
 *
 * As an example, you could have declared this class as follows to set the
 * `example` property in the callback context:
 *
 *   data class CallbackContext(val example: String?) : StdCallbackContext()
 */
class CallbackContext : StdCallbackContext()
