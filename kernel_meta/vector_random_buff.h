#ifdef __CCE_KT_TEST__
#define __aicore__ 
#else
#define __aicore__ [aicore]
#endif

extern "C" inline __aicore__ void vector_random_buff_kernel0() {
set_vector_mask((uint64_t)-1, (uint64_t)-1);
set_atomic_none();
   half reg_buf1[1] = {0};
     int8_t reg_buf2[1] = {0};
  __ubuf__   uint8_t* src_ub = (__ubuf__  uint8_t *)get_imm(0);
  // "aicore arch: Ascend910"
  reg_buf1[0] = (half)-9.711121e+00f;
  reg_buf2[0] = (int8_t)1;
  set_vector_mask(0x0, 0xffff);
  for (int32_t i = 0; i < 8; ++i) {
    vadds(((__ubuf__ half *)src_ub + ((i * 16384) + (((int32_t)reg_buf2[0]) * 16))), ((__ubuf__ half *)src_ub + ((i * 16384) + (((int32_t)reg_buf2[0]) * 16))), reg_buf1[0], (int64_t)6917537858093907969);
  }
  pipe_barrier(PIPE_ALL);
  int32_t need_random = ((int32_t)get_data_size() >> 16);
  pipe_barrier(PIPE_ALL);

}

