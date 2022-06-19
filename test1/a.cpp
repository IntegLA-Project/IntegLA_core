
void integLA_double_axpy(double alpha, double* x, double
}* y)
{
  assert(xsize == y.size);
#if USE_CPU
  cblas_daxpy(...); // doubleとfloatは簡単
#if USE_GPU
  cublas_daxpy(...);
#endif
}

void integLA_float_axpy(float alpha, float *x, float *y) {
  assert(xsize == y.size);
#if USE_CPU
  cblas_saxpy(...);
#if USE_GPU
#pragma omp target... // cublasはバグってたり無かったりする
  for (size_t i = 0; i < size; i++) {
    y[i] = alpha * x[i] + y[i];
  }
}
#endif
}

void integLA_int_axpy(int alpha, int *x, int *y) {
  assert(xsize == y.size);
#if USE_CPU
#pragma omp parallel for
  for (size_t i = 0; i < size; i++) { // 疎行列だとこう簡単じゃない
    y[i] = alpha * x[i] + y[i];
  }
#if USE_GPU
#pragma omp target... // reductionが入ったりする
  for (size_t i = 0; i < size; i++) {
    y[i] = alpha * x[i] + y[i];
  }
#endif
}