package com.awssamples.configproactiveeval.hook;

import static org.mockito.Mockito.spy;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

/**
 * Tests for the pre-create hook.
 */
public class PreCreateHookHandlerTest extends BaseHookHandlerStdTest {

  private PreCreateHookHandler handler;

  @Override
  @BeforeEach
  public void setup() {
    handler = spy(new PreCreateHookHandler());
    super.setup();
  }

  @Test
  public void test_exceptionCaught() {
    test_exceptionCaughtInPreCreatePreUpdateOperations(handler);
  }

  @Test
  public void test_nullPointerExceptionCaught() {
    test_nullPointerExceptionCaughtInPreCreatePreUpdateOperations(handler);
  }

  @Test
  public void test_invalidParameterValueExceptionCaught() {
    test_invalidParameterValueExceptionCaughtInPreCreatePreUpdateOperations(handler);
  }

  @Test
  public void test_nonCompliantResource() {
    test_nonCompliantResource(handler);
  }

  @Test
  public void test_compliantResource() {
    test_compliantResource(handler);
  }

  @Test
  public void test_insufficientDataConfiguredToPass() {
    test_insufficientDataConfiguredToPass(handler);
  }

  @Test
  public void test_insufficientDataConfiguredToFail() {
    test_insufficientDataConfiguredToFail(handler);
  }

  @Test
  public void test_insufficientDataConfiguredToFailWithFailureReason() {
    test_insufficientDataConfiguredToFailWithFailureReason(handler);
  }

  @Test
  public void test_insufficientDataConfiguredToDefault() {
    test_insufficientDataConfiguredToDefault(handler);
  }
}
