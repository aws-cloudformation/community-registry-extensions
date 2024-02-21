package com.awscommunity.config.proactiveeval;

import software.amazon.cloudformation.proxy.StdCallbackContext;

/**
 * Configure the callback context.
 */
@lombok.Getter
@lombok.Setter
@lombok.ToString
@lombok.EqualsAndHashCode(callSuper = true)
public class CallbackContext extends StdCallbackContext {
}
